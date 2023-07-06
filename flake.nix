{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils, ... }@inp:
    utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          buildInputs = [
            (pkgs.poetry2nix.mkPoetryEnv {
              projectDir = ./.;
              overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend
                (self: super: {
                  gast = super.gast.overridePythonAttrs (old: {
                    nativeBuildInputs = (old.nativeBuildInputs or [ ])
                      ++ [ self.setuptools-scm ];
                  });
                  beniget = super.beniget.overridePythonAttrs (old: {
                    buildInputs = (old.buildInputs or [ ])
                      ++ [ super.setuptools-scm ];
                  });

                });
            })
          ];

        };
      });

}
