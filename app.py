import nextcord
from nextcord.ext import commands 
import logging

# Enable intents
intents = nextcord.Intents.default()
intents.message_content = True  # Enable Message Content Intent

logger = logging.getLogger('discord')
logging.basicConfig(level= logging.NOTSET)

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


@bot.event
async def on_ready():
    logging.info(f"Logged in as: {bot.user.name}")
    logging.info(f"{bot.user}, is ready!")
    logging.info(f"{bot.guilds} bot's guilds!")


@bot.event
async def on_voice_state_update(member, before, after):
    if member.bot:
        return
    if not before.channel:
        logging.info(f'{member.name} joined {after.channel.name}')
    if before.channel and not after.channel:
        logging.info("User left channel")


if __name__ == '__main__':
    bot.run("PASTE YOUR TOKEN HERE")