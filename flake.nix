{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/master";
    flake-utils.url = "github:numtide/flake-utils";
    mach-nix.url = "github:DavHau/mach-nix?ref=3.3.0";
  };

  outputs = { self, nixpkgs, flake-utils, mach-nix }:
    flake-utils.lib.eachDefaultSystem (system:
      let
        python = "python310"; # <--- change here
        pkgs = nixpkgs.legacyPackages.${system};
        # https://github.com/DavHau/mach-nix/issues/153#issuecomment-717690154
        mach-nix-wrapper = import mach-nix { inherit pkgs python; };
        requirements =
          builtins.readFile ./frontend/untexifyweb/requirements.txt;
        pythonBuild = mach-nix-wrapper.mkPython { inherit requirements; };
      in {
        inherit pythonBuild;
        devShell = pkgs.mkShell {
          buildInputs = [
            # dev packages
            (pkgs.${python}.withPackages
              (ps: with ps; [ pip black pyflakes isort ])) # <--- change here
            pkgs.nodePackages.pyright
            pkgs.glpk

            # app packages
            pythonBuild
          ];
        };
      });
}
