{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    noogle.url = "github:nix-community/noogle";
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "aarch64-linux"];

      perSystem = {pkgs, ...}: {
        packages = import ./default.nix {inherit pkgs;};
      };

      flake.nixosModules.default = import ./nixos-module.nix;
    };
}
