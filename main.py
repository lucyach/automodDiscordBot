import discord
import os
from keep_alive import keep_alive

client = discord.Client()
violations = {}

## for github viewers, I have removed the lists of words because it's crude:/
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

    for i in range(0, len(blacklist)):
      if blacklist[i] in msg:
        await message.delete()
        await message.channel.send(str(message.author) + ", please avoid using that language.")
        if message.author not in violations:
          violations[message.author] = 1
        else:
          violations[message.author] += 1
        if message.channel != 817623556463919114 or message.channel != 817623583713918996:
          channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
          await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]))
    
    for i in range(0, len(specialBlacklist)):
      if specialBlacklist[i] in msg:
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

    ## for github viewers, this is a joke for my friend. ignore.
    if str(message.author) == "Beni#6609":
      if 'bark' in msg:
        await message.channel.send('Beni people might respect you more if the words that came out of your mouth where intelligent and when poeple asked you a question you auctually responded instead of saying "BARK BARK". Face it beni your not a dog. Dogs are cute and your not')

keep_alive()
client.run(os.getenv('TOKEN'))
