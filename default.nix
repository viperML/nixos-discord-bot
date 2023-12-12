{ pkgs ? import <nixpkgs> {}}: rec {
  default = package;
  package = pkgs.python3.pkgs.callPackage ./package.nix {};
  dev-package = package.overrideAttrs (_: {src=null;});
}
