import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Hai fatto l\'accesso come {bot.user}')

@bot.command()
async def ciao(ctx):
    await ctx.send(f'Ciao! Sono un bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5, fruit="banana"):
    await ctx.send("he" * count_heh)
    await ctx.send(f"Your favorite fruit is {fruit}")

@bot.command()
async def info(ctx):
    await ctx.send(f"Ciao {ctx.author.name}! Hai scritto in #{ctx.channel.name}.")


bot.run("INSERIRE IL TOKEN QUA!")
