from nextcord.ext import commands # type: ignore

bot = commands.Bot(command_prefix="!")

# !hi
# Hello!

# name of our command
# async function because we want function to execute asynchronously 

@bot.command(name="hi")
async def SendMessage(ctx):
    await ctx.send('Hello!')


@bot.event
async def on_ready():
    print(f"Logged in as: {bot.user.name}")


if __name__ == '__main__':
    bot.run("PASTE YOUR TOKEN HERE")