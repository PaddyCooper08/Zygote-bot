import os
import discord
import random
import random
from discord.ext import commands
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json
import time
import asyncio
import youtube_dl
import urllib.request
import parse
import re
from collections import deque
import pafy
import urllib


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix=';', help_command=None)
class Queue:
	def __init__(self):
		self.buffer = deque()
		
	def enqueue(self, val):
		self.buffer.appendleft(val)
		
	def dequeue(self):
		return self.buffer.pop()
	
	def is_empty(self):
		return len(self.buffer)==0		
	def size(self):
		return len(self.buffer)

pq = Queue()
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,
                                 activity=discord.Game(";help"))
    print("Bot is connected")


@client.command(name='ping')
async def ping_command(ctx):
  await ctx.channel.send('pong')







@client.event
async def on_command_error( ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
  # If the command is currently on cooldown trip this
                
    m, s = divmod(error.retry_after, 60)
    h, m = divmod(m, 60)
    if int(h) == 0 and int(m) == 0:
      await ctx.channel.send(f' You must wait {int(s)} seconds to use this command!')
    elif int(h) == 0 and int(m) != 0:
      await ctx.channel.send(f' You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
    else:
      await ctx.channelsend(f' You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
  raise error
  def is_connected(ctx):
    voice_client = get(ctx.bot.voice_clients, guild=ctx.guild)
    return voice_client and voice_client.is_connected()


async def play_music_no_curr_channel(ctx):
  def check(m):
    return m.author == ctx.author and m.channel == ctx.channel
    

    
    
    
  song_there = os.path.isfile("song.mp3")
  try:
    if song_there:
      os.remove("song.mp3")
  except PermissionError:
    await ctx.send("Wait for the current playing music to end or use the 'stop' command")
    return
  voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
  print(voice)
  
  em = discord.Embed(title="Mixer", color=ctx.author.color)
  em.add_field(name='Please answer the following question within the next 15 seconds:', value=f"{ctx.author.mention} please type the name of the song you would like to play.")
  await ctx.send(embed=em)
  try:
    msg = await client.wait_for('message', timeout=15.0, check=check)

  except asyncio.TimeoutError:
    em2 = discord.Embed(title='Error', color=ctx.author.color)
    em2.add_field(name='Mixer creation failed', value=f"{ctx.author.mention} you're too slow, please be quicker next time")      
    await ctx.send(embed=em2) 
    return
  search_keyword = msg.content.replace(" ", "_")
  print(search_keyword)
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  finished_url = ("https://www.youtube.com/watch?v=" + video_ids[0])
  video = pafy.new(finished_url)
  value = video.length
  em3=discord.Embed(title='Mixer', color=ctx.author.color)
  em3.add_field(name='Mixer success please wait for the following song to be donwloaded and played', value=f"Playing {finished_url}, requested by {ctx.author.mention}")
  await ctx.send(embed=em3)
     
  if value > 420:
    await ctx.send('Sorry, 7 minute maximum length on videos')
  else:
    pq.enqueue(finished_url)
    print(pq.buffer)
      


@client.command(aliases=['mixer', 'p', 'start_mixer', 'music', 'm'])
async def play(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    while True:
        if voice == None:
          voiceChannel = ctx.author.voice.channel
          await voiceChannel.connect()
          voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
          await play_music_no_curr_channel(ctx)
        if voice.is_playing() == False:
 
            finished_url = pq.dequeue()
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            ydl_opts = {
                'format': 'bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192',
                }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([finished_url])
            for file in os.listdir("./"):
                if file.endswith(".mp3"):
                    os.rename(file, "song.mp3")
            voice.play(discord.FFmpegPCMAudio("song.mp3"))
            print(voice)
        else:
            await play_music_no_curr_channel(ctx)
            await ctx.send('Song added to queue')
                    
        
        
        
    else:
        await play_music_no_curr_channel(ctx)
        if voice.is_playing() == False:
            finished_url = pq.dequeue()
            voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
            ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
            }],
            }
            with youtube_dl.YoutubeDL(ydl_opts) as ydl:
                ydl.download([finished_url])
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                        voice.play(discord.FFmpegPCMAudio("song.mp3"))
                        print(voice)

        else:
            await play_music_no_curr_channel(ctx)
            await ctx.send('Song added to queue')
                    
        
                
            
            
        

    






















              

      
   


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")



@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")

@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()


@client.command(aliases=['youtube', 'y', 'ys', 'search_youtube'])
async def yt_search(ctx, url : str):
  search_keyword = url
  html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + search_keyword)
  video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
  await ctx.channel.send("https://www.youtube.com/watch?v=" + video_ids[0])

@client.command()
async def url_play(ctx, url : str):
    
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    print(voice)
    if voice == None:
     
      
      
      voiceChannel = ctx.author.voice.channel
      await voiceChannel.connect()
      voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
      ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
          }],
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
      for file in os.listdir("./"):
          if file.endswith(".mp3"):
              os.rename(file, "song.mp3")
      voice.play(discord.FFmpegPCMAudio("song.mp3"))
      print(voice)
      

    else:
     
      ydl_opts = {
          'format': 'bestaudio/best',
          'postprocessors': [{
              'key': 'FFmpegExtractAudio',
              'preferredcodec': 'mp3',
              'preferredquality': '192',
          }],
      }
      with youtube_dl.YoutubeDL(ydl_opts) as ydl:
          ydl.download([url])
      for file in os.listdir("./"):
          if file.endswith(".mp3"):
              os.rename(file, "song.mp3")
      voice.play(discord.FFmpegPCMAudio("song.mp3"))
      print(voice)














for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
client.run(TOKEN)
