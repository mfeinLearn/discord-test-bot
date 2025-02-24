import nextcord
from nextcord.ext import commands 

# Enable intents
intents = nextcord.Intents.default()
intents.message_content = True  # Enable Message Content Intent

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("PASTE YOUR TOKEN HERE")