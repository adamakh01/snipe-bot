import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

# Load token from .env file
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Configure Intents (Permissions your bot needs to read data)
intents = discord.Intents.default()
intents.message_content = True  # Required to read message contents

# Initialize the bot with a command prefix (e.g., !hello)
bot = commands.Bot(command_prefix='!', intents=intents)

# Event: Runs when the bot successfully logs in
@bot.event
async def on_ready():
    print(f'Logged in successfully as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command: Responds to "!hello"
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hello {ctx.author.mention}! 👋')

# Run the bot
if __name__ == '__main__':
    bot.run(TOKEN)