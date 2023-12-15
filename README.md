Discord bot for the unofficial NixOS discord server.

https://discord.gg/RbvHtGa

# Development

`nix develop .#dev-package`, or use the direnv preset.

Requires a `DISCORD_TOKEN`, loaded by direnv from the `.env` file.

# Features
- [x] Move conversations
- [ ] Qualify new users with certain role after X condition (e.g. give a role after 15 days)
- [ ] Ban some words in some channel (e.g. ban `nix` in #offtopic)
