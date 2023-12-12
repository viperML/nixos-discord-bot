{
  config,
  lib,
  pkgs,
  ...
}: let
  cfg = config.services.nixos-discord-bot;
in {
  options.services.nixos-discord-bot = {
    enable = lib.mkEnableOption "nixos discord bot";

    package = lib.mkOption {
      type = lib.types.package;
      description = "package for the bot";
      default = pkgs.nixos-discord-bot;
    };

    tokenFile = lib.mkOption {
      type = lib.types.str;
      description = "path to discord token for loading credential. should be a secret from outside the nix store.";
    };
  };

  config = lib.mkIf cfg.enable {
    systemd.services.nixos-discord-bot = {
      wantedBy = ["multi-user.target"];
      after = ["network-online.target"];
      requires = ["network-online.target"];

      serviceConfig = {
        ExecStart = lib.getExe cfg.package;
        DynamicUser = true;
        LoadCredential = "discord_token:${cfg.tokenFile}";
      };
    };
  };
}
