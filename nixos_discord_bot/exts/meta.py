from __future__ import annotations
from typing import Union, TYPE_CHECKING
from discord.ext import commands
import discord

if TYPE_CHECKING:
    from nixos_discord_bot import Bot


class Meta(commands.Cog):

    @commands.command(aliases=["m"])
    @commands.guild_only()
    @commands.cooldown(1, 3, commands.BucketType.user) # people shouldn't be spamming this
    async def move(self, ctx: commands.Context, thread_or_channel: Union[discord.TextChannel, discord.Thread]):
        """
        Direct an offtopic message to the appropriate channel
        """

        if ctx.message.reference is None:
            return await ctx.reply("Reply to the message in question before running `move`", delete_after=20)
        
        msg = ctx.message.reference.cached_message or await ctx.fetch_message(ctx.message.reference.message_id) # type: ignore

        embed = discord.Embed(title="\N{CHEERING MEGAPHONE} Marked as Offtopic!")
        embed.color = discord.Color.red()
        embed.description = (
            f"Please continue your conversation in {thread_or_channel.mention}, "
            "this channel **is not** the right place to discuss this."
        )
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar)
        await ctx.send(embed=embed, reference=msg)

        embed = discord.Embed(
            title="\N{LINK SYMBOL} Original Message",
            url=msg.jump_url,
            description=msg.content,
        )
        embed.set_author(icon_url=msg.author.avatar.with_size(256), name="@" + str(msg.author)) # type: ignore
        await thread_or_channel.send(
            content=f"{msg.author.mention}, please continue here",
            allowed_mentions=discord.AllowedMentions(users=[msg.author]),
            embed=embed,
        )

    # Somewhat of a placeholder for tags that we may or 
    # may not have in the future
    @commands.command(aliases=["r"])
    @commands.guild_only()
    async def resources(self, ctx: commands.Context):
        links = [
            ("NixOS Manual", "https://nixos.org/manual/nixos/stable/"),
            ("Nixpkgs Manual", "https://nixos.org/manual/nixpkgs/stable/"),
            ("Nix.dev", "https://nix.dev/"),
            ("Nix Best Practices", "https://nix.dev/guides/best-practices"),
            ("Nix Flakes, An introduction and tutorial", "https://www.tweag.io/blog/2020-05-25-flakes/"),
            ("Ayats.org", "https://ayats.org/tags/nix/"),
            ("On Nix's Language: Introduction", "https://tales.mbivert.com/on-nix-language/"),
            ("Some notes on nix flakes - Julia Evans", "https://jvns.ca/blog/2023/11/11/notes-on-nix-flakes/"),
            ("Tour of Nix", "https://nixcloud.io/tour/?id=introduction%2Fnix"),
        ]

        formatted = "\n".join(f"- [{name}](<{url}>)" for name, url in links)
        embed = discord.Embed(
            title="Useful Resources",
            color=discord.Color.blue(),
            description=formatted,
        )
        embed.set_footer(text="see #resources for more")
        embed.set_thumbnail(url=ctx.guild.icon.with_size(256)) # type: ignore
        await ctx.send(embed=embed)


async def setup(bot: Bot):
    await bot.add_cog(Meta())
