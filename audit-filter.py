import discord
import requests
import asyncio
import os
from dotenv import loaddotenv

Load environment variables from a .env file (if applicable)
loaddotenv()

Discord bot token and webhook URL from environment variables
DISCORDTOKEN = os.getenv('DISCORDTOKEN')
DESTINATION_WEBHOOK_URL = os.getenv('DESTINATION_WEBHOOK_URL')

Channel IDs to monitor
CHANNEL_IDS = [
    1261781408968347625, 
    1262412438733590558
]

def filter_message(content):
    # Print the message content for debugging
    # print(f"Checking message content: {content}")
    # Return True for messages that do not contain 'broadcast', 'whitespace', or 'Camera'
    return 'broadcast' not in content and 'whitespace' not in content and 'Camera' not in content

Create a client instance
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    # Start the periodic task
    client.loop.create_task(periodic_check())

@client.event
async def on_message(message):
    # Skip messages from the bot itself
    if message.author == client.user:
        return

    # Check if the message is from one of the specified channels
    if message.channel.id in CHANNEL_IDS:
        # Filter the message
        if filter_message(message.content):
            # Forward the message to the destination webhook
            payload = {
                'content': message.content,
            }
            response = requests.post(DESTINATION_WEBHOOK_URL, json=payload)

async def periodic_check():
    while True:
        await asyncio.sleep(30)  # Wait for 30 seconds
        # Add periodic tasks here if needed

Run the bot
if __name == "__main":
    if not DISCORD_TOKEN or not DESTINATION_WEBHOOK_URL:
        print("Environment variables for DISCORD_TOKEN or DESTINATION_WEBHOOK_URL are missing.")
    else:
        client.run(DISCORD_TOKEN)
