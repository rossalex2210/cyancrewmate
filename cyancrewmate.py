import discord
from discord.ext import commands
from config import settings
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.channel.id == settings['codechannelid']:
            await message.channel.send('Код: {0.content} Комната: {0.author.voice.channel.name}'.format(message))
            await message.delete()
client = MyClient()
client.run(settings['token'])
