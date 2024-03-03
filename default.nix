{ pkgs ? import <nixpkgs> {}, noogle-data ? null}: rec {
  default = package;
  package = pkgs.python3.pkgs.callPackage ./package.nix { inherit noogle-data; };
}
