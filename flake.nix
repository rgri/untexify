{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    poetry2nix.url = "github:nix-community/poetry2nix";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, poetry2nix, nixpkgs, utils, ... }@inp:
    utils.lib.eachDefaultSystem (system:
      let
        pkgs = import nixpkgs { inherit system; };
        p2n = import poetry2nix { inherit system; };
      in {
        devShell = pkgs.mkShell {
          buildInputs = [ (p2n.mkPoetryEnv { projectDir = ./.; }) ];
        };
      });

}
