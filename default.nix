{ pkgs ? import <nixpkgs> { } }:
let untexifyEnv = pkgs.poetry2nix.mkPoetryEnv { projectDir = ./.; };
in untexifyEnv.env
