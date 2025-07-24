from discord.ext import commands
import discord
import os
import random
from keep_alive import keep_alive  # ✅ ye hona chahiye

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix=None, intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online! 🧠 Chatbot ready!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if bot.user.mentioned_in(message):
        responses = [
            "Kya haal hai bhai? 😎",
            "Main ek chatbot hoon, aap mujhe summon kar chuke ho! 🤖",
            "Haanji, kya sawaal hai aapka? 💭",
            "Kya chahiye tumhe mortal?! 💀",
            "Mujhe mention karke bulaya gaya... kya kaam hai? 😂"
        ]
        response = random.choice(responses)
        await message.channel.send(f"<@{message.author.id}> {response}")

    await bot.process_commands(message)

bot.run(os.environ['TOKEN'])  # Render me TOKEN environment me daala hoga
