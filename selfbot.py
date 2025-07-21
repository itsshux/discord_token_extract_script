# dumbed the fk down version of my trollbot, just a template
# request full troll version if interested

import discord
from discord.ext import commands
from openai import OpenAI

bot = commands.Bot(command_prefix='!', self_bot=True)
TOKEN = ""
client = OpenAI(api_key="")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "epic troll prompt"}],
        max_tokens=100,
        temperature=0.8
    )
    ai_response = response.choices[0].message.content.strip()
    await message.channel.send(ai_response)

if __name__ == "__main__":
    bot.run(TOKEN) 
