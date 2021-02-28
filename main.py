import discord
import os
from keep_alive import keep_alive

client = discord.Client()
violations = {}

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    await client.change_presence(activity=discord.Game(name="Automod for JR Discord"))

@client.event
async def on_message(message):
    msg = message.content.lower()
    if message.author == client.user:
        return

    if "fuck" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]))
    
    if "bitch" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]))
    
    if "queer" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language if you are cishet.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]) + '. Note that this word is special and it is okay for LGBT+ people to use.')
    
    if "cunt" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]))
    
    if "pussy" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]))
    
    if "retard" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language if you are abled.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]) + '. Note that this word is special and it is okay for disabled people to use.')
    
    if "fag" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language if you are heterosexual.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]) + '. Note that this word is special and it is okay for homosexual people to use.')
    
    if "tranny" in msg:
      await message.delete()
      await message.channel.send(str(message.author) + ", please avoid using that language if you are cisgender.")
      if message.author not in violations:
        violations[message.author] = 1
      else:
        violations[message.author] += 1
      channel = client.get_channel(783529978532593685) ## replace this with your staff channel id
      await channel.send('Snitch message: ' + str(message.author) + ' said "' + str(msg) + '" in channel #' + str(message.channel) + '. This is their violation #' + str(violations[message.author]) + '. Note that this word is special and it is okay for transgender people to use.')
    
  
    

keep_alive()
client.run(os.getenv('TOKEN'))
