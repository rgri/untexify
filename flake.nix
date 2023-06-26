{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    poetry2nix.url = "github:nix-community/poetry2nix";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, poetry2nix, utils, ... }@inp:
    utils.lib.eachDefaultSystem (system:
      let pkgs = import nixpkgs { inherit system; };
      in {
        devShell = pkgs.mkShell {
          buildInputs = [ (poetry2nix.mkPoetryEnv { projectDir = ./.; }) ];
        };
      });

}
