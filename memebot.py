import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def mem(ctx):
    a = random.randint(1,3)
    if a == 1:
        with open('images/mem1.jpg', 'rb') as f:
            # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
            picture = discord.File(f)
    elif a == 2:
        with open('images/mem2.jpg', 'rb') as f:
            # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
            picture = discord.File(f)
    else:
        with open('images/mem3.jpg', 'rb') as f:
            # Zapiszmy przekonwertowany plik biblioteki Discord w tej zmiennej!
            picture = discord.File(f)
# Możemy następnie wysłać ten plik jako parametr!
    await ctx.send(file=picture)
    
bot.run()
