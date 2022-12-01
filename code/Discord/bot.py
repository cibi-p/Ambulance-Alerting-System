import discord
import os

def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content=True
    client = discord.Client(intents=intents)

    @client.event
    async def on_read():
        print(f'{client.user} is Now online')
    
    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        u_message=str(message.content)
        channel=str(message.channel)
        print(f'{username}: {u_message} in {channel}')
        await message.channel.send(u_message)

    client.run(os.getenv('TOKEN'))  

if __name__ == '__main__':
    run_discord_bot()