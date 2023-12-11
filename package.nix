{
  buildPythonPackage,
  lib,
  discordpy,
  setuptools-scm,
}:
buildPythonPackage {
  pname = "nixos-discord-bot";
  version = "0.1.0";

  pyproject = true;
  strictDeps = true;

  src = lib.fileset.toSource {
    root = ./.;
    fileset =
      lib.fileset.intersection
      (lib.fileset.fromSource (lib.sources.cleanSource ./.))
      (lib.fileset.unions [
        ./nixos_discord_bot
        ./pyproject.toml
      ]);
  };

  nativeBuildInputs = [
    setuptools-scm
  ];

  propagatedBuildInputs = [
    discordpy
  ];
}
