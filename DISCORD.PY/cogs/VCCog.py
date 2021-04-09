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
from discord.voice_client import VoiceClient
import ffmpeg
import youtube_dl

class VCCog(commands.Cog):
  def __init__(self, client):
    self.client = client
  

  @commands.command(name='join')
  async def join(self, ctx):
    channel = ctx.author.voice.channel
    await channel.connect()


  @commands.command(name='unjoin')
  async def leave(self, ctx):
    await ctx.voice_client.disconnect()
  
  
 

 
          











def setup(client):
  client.add_cog(VCCog(client))
