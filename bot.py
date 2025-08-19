import discord
import requests
import json

def get_meme():
    response=requests.get("https://meme-api.com/gimme")
    json_data=json.loads(response.text)
    return json_data["url"]


class MyClient(discord.Client):
    async def on_ready(shelf):
        print("Logged on as {0}!".format(shelf.user))

intents=discord.Intents.default()
intents.message_content=True
client=MyClient(intents=intents)
client.run("YOUR_BOT_TOKEN")

async def on_message(message):
    if message.author==client.user:
        return
    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")







