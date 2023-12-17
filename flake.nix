{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
    flake-parts.url = "github:hercules-ci/flake-parts";
    poetry2nix = {
      url = "github:nix-community/poetry2nix";
      inputs.nixpkgs.follows = "nixpkgs";
    };
  };

  outputs = inputs @ {nixpkgs, flake-parts, poetry2nix, ...}:
    flake-parts.lib.mkFlake {inherit inputs;} {
      systems = ["x86_64-linux" "aarch64-linux"];

      perSystem = {pkgs, ...}: let
          poetry = poetry2nix.lib.mkPoetry2Nix { inherit pkgs; };
          overrides = poetry.overrides.withDefaults (self: super:
            let
              extraDeps = {
                jishaku = [ super.setuptools ];
                import-expression = [ super.setuptools ];
                frozenlist = [ super.expandvars ];
              };
            in  
              nixpkgs.lib.mapAttrs (name: value: 
                super.${name}.overridePythonAttrs(old: {
                  buildInputs = (old.buildInputs or []) ++ value;
                })
              ) extraDeps
            );
      in
      {
        devShells.default = (poetry.mkPoetryEnv {
          projectDir = ./.;
          inherit overrides;
        }).env.overrideAttrs(old: {
          buildInputs = (old.buildInputs or []) ++ [ pkgs.poetry ];
        });

        packages = import ./default.nix {
          inherit pkgs;
          inherit (poetry) mkPoetryApplication;
          inherit overrides;
        };
      };

      flake.nixosModules.default = import ./nixos-module.nix;
    };
}
