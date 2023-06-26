{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    poetry2nix.url =
      "github:nix-community/poetry2nix/4f91d45e39cf64b642c6d2725c7bd50d6fcb544b";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, poetry2nix, utils, ... }@inp:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        overlays = [ poetry2nix.overlay ];
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            (pkgs.poetry2nix.mkPoetryEnv {
              projectDir = ./.;
              overrides = pkgs.poetry2nix.overrides.withDefaults (self: super: {
                # …
                # workaround https://github.com/nix-community/poetry2nix/issues/568
                structlog = super.structlog.overridePythonAttrs (old: {
                  buildInputs = (old.buildInputs or [ ])
                    ++ [ pkgs.python310.flit-core ];
                });
              });
            })
          ];

        };
      });

}
