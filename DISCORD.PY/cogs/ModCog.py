import discord
from discord.ext import commands
import random
from discord.ext import commands
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json
import time
import asyncio
from better_profanity import profanity
from discord.utils import get




class ModCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  profanity.load_censor_words_from_file('./profanity.txt')



  @commands.Cog.listener()
  async def on_message(self, message):
    profanity.load_censor_words_from_file('./profanity.txt')

    
    your_role = message.author.roles
  
    if profanity.contains_profanity(message.content):
      if not message.author.bot:
        if message.guild:
          if '823264759105323028' in str(your_role) :
            print (your_role)
            return
          
          
            
          else:
            await message.delete()
            await message.channel.send("You can't say that here")


  @commands.command(name="addprofanity", aliases=['addswears', 'add_profanity', 'ap'])
  @commands.has_role('Head Coder')
 
  async def add_swears(self, ctx, words):
  
  
    f = open("profanity.txt", "a")
    f.write(words)
    f.close()
    w = open("profanity.txt", "a")
    w.write('\n')
    w.close
    profanity.load_censor_words_from_file('./profanity.txt')
    await ctx.send('Success')


    
    
  
    
    
  @commands.command(aliases=['get_profanity', 'gp', 'get_swears', 'get_curses', 'gs', 'gc'])
  async def print_profanity(self, ctx):
    try:
      f = open('profanity.txt', 'r')
      profanity = f.read()
      await ctx.send(profanity)
      f.close()
      
    except:
      await ctx.send("There are no swear words currently")
     
            
          
          
  @commands.command(name='remove_profanity', aliases=['removeprofanity', 'delcurses', 'removecurses', 'rp'])
  async def del_profanity(self, ctx, words):
     with open("profanity.txt", "r") as f:
       lines = f.readlines()
     with open("profanity.txt", "w") as f:
       for line in lines:
         if line.strip("\n") != words:
           f.write(line)
           await ctx.send("Success")
       
    
      

       
    
    
  @commands.command(name='clean', aliases=['c', 'claen'])
  @commands.has_role('Head Coder')
  async def cleanmsgs(self, ctx, amount=2):
      await ctx.channel.purge(limit=amount)
      
      
      
  @commands.command(name='clear')
  @commands.has_role('Head Coder')
  async def clearmsgs(slef, ctx, amount=387469832491832749832749):
    await ctx.channel.purge(limit=amount)
    
    
  @commands.command(name='mute')
  @commands.has_permissions(kick_members=True)
  async def mute_member(self, ctx, member : discord.Member):
    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
    MESSAGE = await ctx.send(f"@{ctx.author} please state a reason")
    try:
        msg = await self.client.wait_for('message', timeout=15.0, check=check)


    except asyncio.TimeoutError:
      await ctx.send(f"@{ctx.author} you're too slow")
      return
    await MESSAGE.delete()
    await msg.delete()

    
    
    
    role = discord.utils.get(member.guild.roles, name='Muted')
    await member.add_roles(role)
    em = discord.Embed(Title='Moderation Control', color=ctx.author.color)
    em.add_field(name=f"@{member} has been muted by @{ctx.author}", value=f"Reason: {msg.content}")
    await ctx.send(embed=em)
    
    
    
  @commands.command(name='unmute')
  @commands.has_permissions(kick_members=True)
  async def unmute_member(self, ctx, member : discord.Member):
    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel
    role = discord.utils.get(member.guild.roles, name='Muted')
    await member.remove_roles(role)
    MESSAGE = await ctx.send(f"@{ctx.author} please state a reason")
    try:
        msg = await self.client.wait_for('message', timeout=15.0, check=check)


    except asyncio.TimeoutError:
      await ctx.send(f"@{ctx.author} you're too slow")
      return
    await MESSAGE.delete()
    await msg.delete()

  
       
       
    
    
   
    
    
    em = discord.Embed(Title='Moderation Control', color=ctx.author.color)
    em.add_field(name=f"@{member} has been unmuted by @{ctx.author}", value=f"Reason: {msg.content}")
    await ctx.send(embed=em)
    
    
 
        
    
     
   

       
        












def setup(client):
  client.add_cog(ModCog(client))
