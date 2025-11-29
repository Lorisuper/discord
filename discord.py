import discord
from discord.ext import commands
import random, os
import requests
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
async def cat(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una volta chiamato il comando duck, il programma richiama la funzione get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.group()
async def comepulire(ctx):
    
    if ctx.invoked_subcommand is None:
        await ctx.send(f'i comandi sono altri come casa , box, dovebuttolaspazzatura')


@comepulire.command(name='casa')
async def _casa(ctx):
    await ctx.send("intanto passi l'aspirapolvere, poi passi lo straccio inzuppato con sapone e poi alla fine o all'inizio passi una sorta di swiffer per la polvere in punti in cui non passa l'aspiraolvere")

@comepulire.command(name='box')
async def _box(ctx):
    await ctx.send("per il box in realtà non c'è molto da fare però se vuoi per pulirlo un po' potresti levare gli oggetti all'interno e levare la polvere con lo swiffer che diventerà praticamente nero e poi con dell'acqua insaponata")

@comepulire.command(name='dovebuttolaspazzatura')
async def _dovebuttolaspazzatura(ctx):
    await ctx.send("la carta e cartone vanno nel secchione blu, la plastica nel giallo,il vetro in una sorta di campana verde, per l'indifferenziata anche io che non la faccio ci metto la busta di spazzatura piena di cose diverse, nell'organico ci metti il cibo che non si mangia e nel secchione del azzurro, mai visto, ci metti il metallo")


bot.run("INSERIRE IL TOKEN QUA!")
