import discord
import random
from discord.ext import commands
from bot_logic import gen_emodji

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="/", intents=intents, help_command=commands.DefaultHelpCommand())

TOKEN = "..."

@bot.event
async def on_ready():
    print(f'Todo listo, el bot arranco:')

@bot.command()
async def Hola(ctx):
    await ctx.send(f'¡Hola, {ctx.author.mention}!, ¿Cómo estás?')

@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.command()
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command()
async def help(ctx):
    help_message = """
**Comandos disponibles:**

`/add <num1> <num2>` – Suma dos números.
`/hello` – El bot te saluda.
`/joined` - Bienvenida a un nuevo miembro al servidor.
"""
    await ctx.send(help_message)

bot.run(TOKEN)
