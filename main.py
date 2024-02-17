import disnake

from disnake.ext import commands

bot = commands.Bot(command_prefix="*", intents=disnake.Intents.all())


@bot.slash_command()
async def test(interaction: disnake.AppCmdInter):
    await interaction.send("test")

bot.run("MTIwODQ3NjAzNDc2OTYyNTE2OQ.G-IecI.TD1_ulchIfRVNb9yEOXnGrjXMHDAXhZBjhlff8")
