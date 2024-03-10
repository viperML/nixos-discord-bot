{
  buildPythonPackage,
  lib,
  setuptools-scm,
  discordpy,
  dataclasses-json,
}:
let
  pyproject = builtins.fromTOML (builtins.readFile ./pyproject.toml);
in
buildPythonPackage {
  pname = pyproject.project.name;
  version = pyproject.project.version;

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

  nativeBuildInputs = [ setuptools-scm ];

  propagatedBuildInputs = [
    discordpy
    dataclasses-json
  ];

  meta.mainProgram = "nixos-discord-bot";
}
