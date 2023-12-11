{ pkgs ? import <nixpkgs> {}}: rec {
  package = pkgs.python3.pkgs.callPackage ./package.nix {};
  dev-package = package.overrideAttrs (_: {src=null;});
}
