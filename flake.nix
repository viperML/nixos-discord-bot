{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "aarch64-linux"];

      perSystem = {pkgs, ...}: {
        packages = import ./default.nix {inherit pkgs;};
        devShells.default = (pkgs.python3.withPackages(ps: with ps; [
          discordpy
        ])).env;
      };

      flake.nixosModules.default = import ./nixos-module.nix;
    };
}
