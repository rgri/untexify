{
  description = "Tensorflow + CUDA development environment";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs";
  inputs.poetry2nix.url = "github:nix-community/poetry2nix";

  outputs = { self, nixpkgs, flake-utils, poetry2nix }:
    {
      # Nixpkgs overlay providing the application
      overlay = nixpkgs.lib.composeManyExtensions [
        poetry2nix.overlay
        (final: prev: {
          pythonEnv = prev.poetry2nix.mkPoetryEnv {
            projectDir = ./.;
            preferWheels = true;
          };
        })
      ];
    } // (flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs {
          inherit system;
          overlays = [ self.overlay ];
          config.allowUnfree = true;
        };
      in
      rec {
        devShell = pkgs.mkShell {
          name = "tf-dev-environment";
          nativeBuildInputs = [ pkgs.poetry ];

          shellHook = ''
            export LD_LIBRARY_PATH=${pkgs.stdenv.cc.cc.lib}/lib:${pkgs.cudatoolkit_11}/lib:${pkgs.cudnn_cudatoolkit_11}/lib:${pkgs.cudatoolkit_11.lib}/lib:$LD_LIBRARY_PATH

            alias jupyter="poetry run jupyter"
          '';
        };
    }));
}
