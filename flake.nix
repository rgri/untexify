{
  description = "Flake to manage python workspace";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    utils.url = "github:numtide/flake-utils";
  };

  outputs = { self, nixpkgs, utils, ... }@inp:
    utils.lib.eachDefaultSystem
    (system: let pkgs = import nixpkgs { inherit system; }; in rec { });

}
