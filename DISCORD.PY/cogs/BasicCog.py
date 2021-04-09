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




class BasicCog(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  
  
  @commands.command(name="rng")
  async def rng_specify(self, ctx):
    await ctx.channel.send("Please do ';rng_10' for a random number between 1 and 10 and ';rng_100' for a random number between 1 and 100.")
    

  @commands.command(name="rng_10")
  async def rng_10(self, ctx):
    await ctx.channel.send(random.randint(1, 10))


  @commands.command(name="rng_100")
  async def rng_100(self, ctx):
    await ctx.channel.send(random.randint(1, 100))


  @commands.command(name="help")
  async def help(self, ctx):
      await ctx.channel.send(
          "Commands:\n ;ip - prints the smp ip\n ;rng - picks a random number\n ;sub - plugs max's twitch\n ;sub2 - plugs sam's twitch\n ;info - info about the bot\n ;gweather- prints the weather in Guildford\n ;lweather - prints the weather in london "
      )


  @commands.command(name="sub")
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def mtwitch(self, ctx):
      await ctx.channel.send(
          "go sub to twitch.tv/flaming_c rn or you have no balls")


  @commands.command(name="sub2")
  async def stwitch(self, ctx):
      await ctx.channel.send(
          "go sub to twitch.tv/goatedsupersam or you have no balls")


  @commands.command(name="info")
  async def info(self, ctx):
      await ctx.channel.send(
          "This bot was created by Paddyxl using the discord.py commands database in python 3.7.3\n It was coded on a raspberry pi 3 using visual studio code\n It is hosted on said raspberry pi or on repl.it servers"
      )


  @commands.command(name="whyispaddyshort")
  async def short(self, ctx):
      await ctx.channel.send("U can't be tall and smart but u can be short and dum :)")


  @commands.command(name="gweather")
  async def weather_guildford(self, ctx):
      owm = OWM('1083910e974188490d7352fe22d37e30')
      mgr = owm.weather_manager()

      # Search for current weather in London (Great Britain) and get details
      observation = mgr.weather_at_place('Guildford,GB')
      w = observation.weather

      status = w.detailed_status  # 'clouds'
      w.wind()  # {'speed': 4.6, 'deg': 330}
      w.humidity  # 87
      temp = w.temperature(
          'celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
      w.rain  # {}
      w.heat_index  # None
      w.clouds  # 75
      message = "It is currently " + str(int(
          temp['temp'])) + " degrees and " + status
      await ctx.channel.send(message)


  @commands.command(name="lweather")
  async def weather_london(self, ctx):
      owm = OWM('1083910e974188490d7352fe22d37e30')
      mgr = owm.weather_manager()

      # Search for current weather in London (Great Britain) and get details
      observation = mgr.weather_at_place('London ,GB')
      w = observation.weather

      status = w.detailed_status  # 'clouds'
      w.wind()  # {'speed': 4.6, 'deg': 330}
      w.humidity  # 87
      temp = w.temperature(
          'celsius')  # {'temp_max': 10.5, 'temp': 9.7, 'temp_min': 9.0}
      w.rain  # {}
      w.heat_index  # None
      w.clouds  # 75
      message1 = "It is currently " + str(int(
          temp['temp'])) + " degrees and " + status
      await ctx.channel.send(message1)
        
  @commands.command(name="doespaddyhaveasmallpp")
  async def penis(self, ctx):
      await ctx.channel.send("Short answser, Yes.")        

def setup(client):
  client.add_cog(BasicCog(client))

