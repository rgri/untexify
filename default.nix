{ pkgs ? import <nixpkgs> { } p2n ? (builtins.fetchFromGitHub {};)}:
let untexifyEnv = pkgs.poetry2nix.mkPoetryEnv { projectDir = ./.; };
in untexifyEnv.env
