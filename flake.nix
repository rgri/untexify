{
  inputs.flake-utils.url = "github:numtide/flake-utils";
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/";
  inputs.nixpkgsOld.url =
    "github:Nixos/nixpkgs/6e3a86f2f73a466656a401302d3ece26fba401d9";
  inputs.poetry2nix = { url = "github:nix-community/poetry2nix"; };
  inputs.poetry2nix.inputs.nixpkgs.follows = "nixpkgs";

  outputs = { self, nixpkgs, flake-utils, poetry2nix, nixpkgsOld }@inputs:
    flake-utils.lib.eachDefaultSystem (system:
      let
        # see https://github.com/nix-community/poetry2nix/tree/master#api for more functions and examples.
        pkgs = nixpkgs.legacyPackages.${system};
        pkgsOld = nixpkgsOld.legacyPackages.${system};
        system = "x86_64-linux";
      in {
        devShells.default = pkgs.mkShell {
          LD_LIBRARY_PATH = nixpkgs.lib.makeLibraryPath [
            pkgsOld.gcc-unwrapped.lib
            pkgs.gcc-unwrapped.lib
          ];
          packages = [
            pkgsOld.python3Full
            pkgs.poetry
            pkgs.pyenv
            #FIXME: You don't need two installs of pyright.
            pkgs.nodePackages.mermaid-cli
          ];
        };
      });
}
