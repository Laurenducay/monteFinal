import discord
import os
from dotenv import load_dotenv
from ec2_metadata import ec2_metadata

# Load the .env file
load_dotenv()

# Initialize the bot
intents = discord.Intents.default()
intents.message_content = True  # Important for reading message content
intents.messages = True

client = discord.Client(intents=intents)
token = str(os.getenv('TOKEN'))

@client.event
async def on_ready():
    print(f"Logged in as a bot {client.user}".format(client))
    print(f'This is my Ec2_metadata.region:', ec2_metadata.region)
    print(f'This is my Ec2_metadata.instance.id:', ec2_metadata.instance_id)

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)

    print(f'Message "{user_message}" by {username} on {channel}')
    
    if message.author == client.user:
        return

    if channel == "random":
        if user_message.lower() in ["hello", "hi"]:
            await message.channel.send(f"Hello {username}!")
            return
        elif user_message.lower() == "show me mimikyu":
            await message.channel.send(f'https://tenor.com/view/jump-cute-happy-love-pokemon-gif-17464877')
        elif user_message.lower() == "do you know who chip is?":
            await message.channel.send(f'YES!!')
        elif user_message.lower() == "prove it":
            await message.channel.send('https://cdn.discordapp.com/attachments/1290443928797184042/1311407472040345640/chip.jpg?ex=6748bee2&is=67476d62&hm=f334491bf7a4a0cc7400f58aeb7d942a580c6f94ee6b44ae00e069448f072185&')


# Run the bot
client.run(token)
