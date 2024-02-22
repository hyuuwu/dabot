  import discord
from discord.ext import commands
from discord import app_commands
from config import Token



bot = commands.Bot(command_prefix="!", intents = discord.Intents.all())

@bot.event
async def on_ready():
    print('IM READY FOR SEX')
    try:
        synced = await bot.tree.sync()
        print(f"synced {len(synced)} commands daddy")
    except Exception as e:
        print(e)



@bot.tree.command(name="sex", description="linuk user e foda")
async def sex(interaction: discord.Interaction):
    await interaction.response.send_message(f"KRL E A {interaction.user.mention}!")

@bot.tree.command(name="kanye", description="kanyewest")
@app_commands.describe(yapp = "yapp. now.")
async def yapp (interaction: discord.Interaction, yapp: str):
    await interaction.response.send_message(f"{interaction.user.mention} mandou eu falar '{yapp}' ")



bot.run('ur token here lulz >:3')'
