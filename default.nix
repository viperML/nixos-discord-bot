{
  pkgs ? import <nixpkgs> {},
  mkPoetryApplication,
  overrides
}:
rec {
  default = bot;
  bot = mkPoetryApplication {
    projectDir = ./.;
    inherit overrides;
  };
}
