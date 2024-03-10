{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    noogle = {
      url  ="github:nix-community/noogle";
    };
  };

  outputs = inputs @ {flake-parts, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "aarch64-linux"];

      perSystem = {pkgs, inputs', ...}: {
        packages = {
          default = pkgs.python3.pkgs.callPackage ./package.nix {};
          inherit (inputs'.noogle.packages) data-json;
        };
      };

      flake.nixosModules.default = import ./nixos-module.nix;
    };
}
