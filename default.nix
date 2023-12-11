{ pkgs ? import <nixpkgs> {}}: {
  package = pkgs.python3.pkgs.callPackage ./package.nix {};
}
