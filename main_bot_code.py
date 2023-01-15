import discord          
from discord.ext import commands
import random
import os 
from itertools import cycle
import webscrape


intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=">",intents = intents)
Status = cycle(['Status 1','Status 2','Status 3'])

token = "Your Bot Token"

Course = webscrape.FreeCourse()

# no result message 
no_result_message = '''Sorry, we can\'t find what you are searching for. We may not have written anything about it yet, 
but you can subscribe to our news letter for updates of our newest content'''



@bot.event
async def on_ready():
    print("BOT IS ONLINE!!")

@bot.event
async def on_message(message): 
  # make sure bot doesn't respond to it's own messages to avoid infinite loop
  if message.author == bot.user:
      return  
  # lower case message
  message_content = message.content.lower()  
  
  if message.content.startswith(f'hello'):
    await message.channel.send('Hello there! I\'m the fidgeting bot from RunPee')

  if  f'search' in message_content:

    key_words, search_words = Course.key_words_search_words(message_content)
    result_links = Course.search(key_words)
    links = Course.send_link(result_links, search_words)
    
    if len(links) > 0:
      for link in links:
       await message.channel.send(link)
    else:
      await message.channel.send(no_result_message)

# @tasks.loop(seconds = 5)
# async def change_status():
#     await bot.change_presence(activity=discord.Game(next(Status)))

# @bot.event 
# async def on_command_error(ctx,error):
#     if isinstance(error,commands.CommandNotFound):
#         await ctx.send("Invalid command used")

# @bot.event
# async def on_member_join(member):
#     print(f'{member} has joined a server')

# @bot.event
# async def  on_member_remove(member):
#     print(f'{member} has been removed form server')


# #Greeting to bot
# @bot.command(aliases=['hi','hello','Yo','Aye'])
# async def greet(ctx):
#     responses = ["Long time no see",
#                 "hello mate!!!",
#                 "welcome",
#                 "Its good to see you again!!"]
#     await ctx.send(random.choice(responses))

# #clear messages
# @bot.command()
# async def clr(ctx,amount : int):
#     await ctx.channel.purge(limit=amount)

# @clr.error
# async def clr_error(ctx,error):
#     if isinstance(error,commands.MissingRequiredArgument):
#        await ctx.send("Please specify an amount of messages to delete")




# #kicking/banning members
# @bot.command()
# async def kick(ctx, member : discord.Member, *, reason=None):
#     await member.kick(reason=reason)

# @bot.command()
# async def ban(ctx, member : discord.Member, *, reason=None):
#     await member.ban(reason=reason)    
#     await ctx.send(f'Banned {member.mention}')

# #unbanning member
# @bot.command()
# async def unban(ctx,*,member):
#     banned_users = await ctx.guild.bans()
#     member_name, member_tag = member.split('#')

#     for ban_entry in banned_users:
#         user = ban_entry.user

#         if (user.name, user.tag) == (member_name,member_tag):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}')
#             return




      

bot.run(token)