import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents)

TOKEN = "MTM5MTU2ODEwNTY0OTczNzc3OA.G_5SPV._vRQOqAVWR9U5Aulv8KFCuvhKk6Ao27o74t9RQ"

@bot.event
async def on_ready():
    print(f'Todo listo, el bot arranco:')

@bot.command()
async def hola(ctx):
    await ctx.send(f'¡Hola, {ctx.author.mention}!, ¿Cómo estás?')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')

bot.run(TOKEN)
