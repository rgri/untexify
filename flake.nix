{
  description = "Application packaged using poetry2nix";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/";
  inputs.poetry2nix = { url = "github:nix-community/poetry2nix"; };

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication;
        pkgs = nixpkgs.legacyPackages.${system};
      in {
        packages = {
          myapp = mkPoetryApplication {
            projectDir = self;
            overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend
              (self: super: {
                lazy-loader = super.lazy-loader.overridePythonAttrs (old: {
                  buildInputs = (old.buildInputs or [ ]) ++ [ super.flit-core ];
                });
                beniget = super.beniget.overridePythonAttrs (old: {
                  buildInputs = (old.buildInputs or [ ])
                    ++ [ super.setuptools-scm ];
                });
              });
          };
          default = self.packages.${system}.myapp;
        };

        devShells.default =
          pkgs.mkShell { packages = [ poetry2nix.packages.${system}.poetry ]; };
      });
}
