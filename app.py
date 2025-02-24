import nextcord
from nextcord.ext import commands 
import logging

# Enable intents
intents = nextcord.Intents.default()
intents.message_content = True  # Enable Message Content Intent

logger = logging.getLogger('discord')
logging.basicConfig(level= logging.NOTSET)

bot = commands.Bot(
    command_prefix="_",
    help_command=None,  # This disables the default help command
    member_cache_flags=nextcord.MemberCacheFlags.none(),  # No member data is cached
    intents=intents
)

@bot.command(name="testing")
async def SendMessage(ctx):
    await ctx.send('Working test!')


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