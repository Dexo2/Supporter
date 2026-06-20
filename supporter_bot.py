import discord
from discord.ext import commands
from discord.ui import Button, View
import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
KANAL_NAZEV = "💕〢žádost-o-roli-supporter"
ROLE_NAZEV = "💕| Supporter"
OBRAZEK_URL = "https://i.imgur.com/TVUJ_OBRAZEK.png"  # nahraj obrázek na imgur.com a vlož URL

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)


class SupporterView(View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Získat roli",
        style=discord.ButtonStyle.primary,
        custom_id="supporter_role_button",
        emoji="💕"
    )
    async def ziskat_roli(self, interaction: discord.Interaction, button: Button):
        role = discord.utils.get(interaction.guild.roles, name=ROLE_NAZEV)

        if role is None:
            await interaction.response.send_message(
                "❌ Role nebyla nalezena. Kontaktuj admina.", ephemeral=True
            )
            return

        if role in interaction.user.roles:
            await interaction.response.send_message(
                "✅ Roli už máš!", ephemeral=True
            )
            return

        await interaction.user.add_roles(role)
        await interaction.response.send_message(
            f"💕 Gratuluji! Získal(a) jsi roli **{ROLE_NAZEV}**!", ephemeral=True
        )


@bot.event
async def on_ready():
    print(f"✅ Bot přihlášen jako {bot.user}")
    bot.add_view(SupporterView())

    kanal = discord.utils.get(bot.get_all_channels(), name=KANAL_NAZEV)
    if kanal is None:
        print(f"❌ Kanál '{KANAL_NAZEV}' nebyl nalezen!")
        return

    async for zprava in kanal.history(limit=10):
        if zprava.author == bot.user and zprava.embeds:
            print("ℹ️ Embed již existuje, neodesílám znovu.")
            return

    embed = discord.Embed(
        title="❤️ Požadavky pro získání role @Supporter ❤️",
        color=0x5865F2
    )
    embed.add_field(
        name="• Dej si tag našeho serveru.",
        value="‣ Nevíš jak? Podívej se na tohle [video](https://www.youtube.com/watch?v=Kf3ClwK-XWw)",
        inline=False
    )
    embed.add_field(
        name="• Jaké jsou výhody?",
        value=(
            "‣ Supporteři dostávají každý den **kódy na Event / VIP** coiny.\n"
            "‣ Supporteři mají skoro každý den nějakou **giveaway**."
        ),
        inline=False
    )
    embed.set_image(url=OBRAZEK_URL)

    await kanal.send(embed=embed, view=SupporterView())
    print("✅ Embed odeslán!")


bot.run(BOT_TOKEN)
