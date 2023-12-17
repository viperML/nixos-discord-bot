{
  pkgs ? import <nixpkgs> {},
  mkPoetryApplication,
  overrides
}:
rec {
  default = bot;
  bot = mkPoetryApplication {
    projectDir = ./.;
    meta.mainProgram = "start";
    inherit overrides;
  };
}
