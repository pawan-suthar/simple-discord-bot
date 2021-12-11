from logging import error
import discord
from discord.enums import ContentFilter
from discord.ext import commands
from discord.ext.commands import context

client = commands.Bot(command_prefix = '!')

bot_token = "OTE4NTI3NTAyMjQxMTAzODcz.YbIjZQ.W6Zrmc5keYHsn4HJU-hgzYZTCo4"
  
#bot ready
@client.event
async def on_ready():
    print(" hey... i am ready")
 
# clear messages
@client.command()   
@commands.has_permissions(manage_messages=True) #set permission
async def clear(ctx,amount:int): #give msg amount to delete
    await ctx.channel.purge(limit = amount+1)
    
@clear.error
async def clear_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('please tell no. of messages you wanto delete')
    
#ping command
@client.command()
async def ping(ctx):
    await ctx.send(f"latency: {round(client.latency * 1000)} Ms")
    
    
#to send msg 
@client.command()
async def hello(ctx):
    if str(ctx.author) == "_king_icon_#1796":
        await ctx.send(f" hello {ctx.author}")
        
#to send pics        
@client.command()
async def pic(ctx):
    await ctx.send(file=discord.File("bbb.jpg"))

#to send links 
@client.command()
async def link(url):
    await url.send("https://koders.in/#/")
    
#show list of all commands
@client.command()
async def plzhelp(ctx):
    embed = discord.Embed(title="Commands",description="some use commands in this bot")
    embed.add_field(name="!hello", value="bot send hello",inline=True)
    embed.add_field(name="!pic", value="bot sends you a pic",inline=True)
    embed.add_field(name="!link", value="it will sendyou a link",inline=True)
    embed.add_field(name="!clear", value="it will delete msg ",inline=True)
    embed.add_field(name="!ping", value="show you ping",inline=True)
    await ctx.send(embed=embed)    
       
#if some one say bad words then delete it   
bad_words = ["abe","saale","bc","mc","kutte"]
@client.event
async def on_message(message):
    message.content = message.content.lower() #if msg in uppercase conver in lowercase
    for word in bad_words:
        if message.content.count(word) >0:
            await message.channel.purge(limit=1)          
    await client.process_commands(message)
    

client.run(bot_token)

