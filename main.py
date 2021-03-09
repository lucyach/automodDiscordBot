import discord
import os
from keep_alive import keep_alive

client = discord.Client()
violations = {}
bad_words = ["fuck", "bitch", "cunt", "pussy"]
specialBadWords = ["queer", "retard", "fag", "tranny"]
specialResponses = [", please avoid using that language if you are cishet.", ", please avoid using that language if you are abled.", ", please avoid using that language if you are heterosexual.", ", please avoid using that language if you are cisgender."]
specialSnitch = [". Note that this word is special and it is okay for LGBT+ people to use.", ". This is their violation #' + str(violations[message.author]) + '. Note that this word is special and it is okay for disabled people to use.", ". Note that this word is special and it is okay for homosexual people to use.", ". Note that this word is special and it is okay for transgender people to use."]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Automod for JR Discord"))

@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return

    for i in range(0, len(bad_words)):
      if bad_words[i] in msg:
        await message.delete()
        await message.channel.send(str(message.author) + ", please avoid using that language.")
        if message.author not in violations:
          violations[message.author] = 1
        else:
          violations[message.author] += 1
        if message.channel != 817623556463919114 or message.channel != 817623583713918996:
          channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
          await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]))
    
    for i in range(0, len(specialBadWords)):
      if specialBadWords[i] in msg:
        await message.delete()
        if i == 0:
          await message.channel.send(str(message.author) + specialResponses[i])
        if message.author not in violations:
          violations[message.author] = 1
        else:
          violations[message.author] += 1
        if message.channel != 817623556463919114 or message.channel != 817623583713918996:
          channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
          await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]) + specialSnitch[i])

keep_alive()
client.run(os.getenv('TOKEN'))
