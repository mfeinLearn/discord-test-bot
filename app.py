import nextcord
from nextcord.ext import commands 
import logging

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

    role_name = "studying"
    role = nextcord.utils.get(member.guild.roles, name=role_name)

    if not role:
        logging.error(f"Role '{role_name}' not found in the server.")
        return  # Exit the function if the role doesn't exist
    
    if not before.channel and after.channel:
        logging.info(f'{member.name} joined {after.channel.name}')
        # Assign the "studying" role
        await member.add_roles(role, atomic=True) 
        logging.info(f"Assigned '{role_name}' role to {member.name}")
    
    if before.channel and not after.channel:
        logging.info(f'{member.name} left the channel')
        # Remove the "studying" role
        await member.remove_roles(role, atomic=True) 
        logging.info(f"Removed '{role_name}' role from {member.name}")


if __name__ == '__main__':
    bot.run("PASTE YOUR TOKEN HERE")