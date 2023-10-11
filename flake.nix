{
  description = "Application packaged using poetry2nix";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/";
  inputs.nixpkgsOld.url =
    "github:Nixos/nixpkgs/6e3a86f2f73a466656a401302d3ece26fba401d9";

  outputs = { self, nixpkgs, flake-utils, poetry2nix, nixpkgsOld }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication;
        pkgs = nixpkgs.legacyPackages.${system};
        pkgsOld = nixpkgsOld.legacyPackages.${system};
        system = "x86_64-linux";
      in {
        devShells.default = let

          appEnv = pkgs.poetry2nix.mkPoetryEnv {
            python = pkgs.python3Full;
            overrides = pkgs.poetry2nix.defaultPoetryOverrides.extend
              (self: super: {
                lazy-loader = super.lazy-loader.overridePythonAttrs (old: {
                  buildInputs = (old.buildInputs or [ ]) ++ [ super.flit-core ];
                });

                werkzeug = super.werkzeug.overridePythonAttrs (old: {
                  buildInputs = (old.buildInputs or [ ]) ++ [ super.flit-core ];
                });
                django-bootstrap5 = super.django-bootstrap5.overridePythonAttrs
                  (old: {
                    buildInputs = (old.buildInputs or [ ])
                      ++ [ super.hatchling ];
                  });
                tensorflow-io-gcs-filesystem =
                  super.tensorflow-io-gcs-filesystem.overridePythonAttrs (old: {
                    buildInputs = (old.buildInputs or [ ])
                      ++ [ super.tensorflow-bin ];
                  });
                ml-dtypes = super.ml-dtypes.overridePythonAttrs (old: {
                  buildInputs = (old.buildInputs or [ ])
                    ++ [ super.setuptools super.pybind11 ];
                });
                contourpy = super.contourpy.overridePythonAttrs (old: {
                  nativeBuildInputs = (old.nativeBuildInputs or [ ])
                    ++ [ super.meson-python ];
                });
              });
            projectDir = ./.;
          };

        in appEnv.env.overrideAttrs (oldAttrs: {
          buildInputs = [
            pkgs.pyenv
            #FIXME: You don't need two installs of pyright.
            pkgsOld.nodePackages.pyright
          ];

          SECRET_KEY = "dummy";
        });
      });
}
