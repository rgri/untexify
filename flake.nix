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
      in {
        devShells.default = pkgs.mkShell {
          packages = [
            pkgs.poetry
            pkgs.pyenv
            pkgs.python39Packages.python
            pkgs.nodePackages.npm
            pkgs.nodePackages.rollup
            #FIXME: You don't need two installs of pyright.
            pkgs.nodePackages.pyright
            pkgs.nodePackages.mermaid-cli
          ];
        };
      });
}
