{
  description = "Application packaged using poetry2nix";

  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/";
  inputs.poetry2nix = { url = "github:nix-community/poetry2nix"; };
  inputs.poetry2nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs = { self, nixpkgs, flake-utils, poetry2nix }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        inherit (poetry2nix.legacyPackages.${system}) mkPoetryApplication;
        pkgs = nixpkgs.legacyPackages.${system};
        system = "x86_64-linux";
        pythonPkgs = (import (builtins.fetchTarball {
          sha256 = "1dvqwqki44v6s6adlmdy0lw3lm0z53ml6cd6i6wymni2ns1wpzy1";
          url =
            "https://github.com/NixOS/nixpkgs/archive/6e3a86f2f73a466656a401302d3ece26fba401d9.tar.gz";
        })) { inherit system; };
      in {
        devShells.default = pkgs.mkShell {
          SECRET_KEY = "dummy";
          LD_LIBRARY_PATH = "${pythonPkgs.stdenv.cc.cc.lib}/lib";
          packages = [
            pythonPkgs.python3Full
            pkgs.poetry
            pkgs.pyenv
            pkgs.nodePackages.npm
            pkgs.nodePackages.rollup
            #FIXME: You don't need two installs of pyright.
            pkgs.nodePackages.pyright
            pkgs.nodePackages.mermaid-cli
          ];
        };
      });
}
