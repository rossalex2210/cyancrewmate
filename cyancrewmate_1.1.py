import discord
from discord.ext import commands
from config import settings
class MyClient(discord.Client):
    #Отправка кодов
    async def on_message(self, message):
        if message.author.id == self.user.id:
            return
        if message.channel.id == settings['codechannelid']:
            await message.channel.send('**{0.author.voice.channel.name} \n   {0.author.name}**'.format(message))
            await message.channel.send('**   {0.content}\n\n\n**'.format(message))
            await message.delete()         
client = MyClient()
client.run(settings['token'])

