import discord
from discord.ext import commands
import random
from discord.ext import commands
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json
import nasapy
import asyncio
from datetime import datetime
from dotenv import load_dotenv
import os
import urllib.request
load_dotenv()
k = os.getenv('NASA_TOKEN')
nasa = nasapy.Nasa(key = k)


class AstroCog(commands.Cog):
	def __init__(self, client):
		self.client = client
 
	
    
   
 
	@commands.command(name='nasapicoftheday', aliases=['potd', 'npotd', 'nasa_pic', 'pic'])
	async def nasa_pic_of_the_day(self, ctx):
		d = datetime.today().strftime('%Y-%m-%d')
		apod = nasa.picture_of_the_day(date=d, hd=True)


		
			
		if("hdurl" in apod.keys()):
				title = d + '_' + apod['title'].replace(' ', '_').replace(':', '_') + ('.jpeg')
					
				image_dir = './Astro_Images'
				
				dir_res = os.path.exists(image_dir)
				
				if (dir_res==False):
					os.makedirs(image_dir)
					
				else:
					print('Directory already exists!\n')
					
				urllib.request.urlretrieve(url = apod['hdurl'], filename = os.path.join(image_dir,title))
				em=discord.Embed(title='Nasa picture of the day', color=ctx.author.color)
					
				if "date" in apod.keys():
					em.add_field(name='Date image released:', value=apod["date"])
				
				if "copyright" in apod.keys():
					em.add_field(name='This image is owned by:', value=apod['copyright'])
					
				if "title" in apod.keys():
					em.add_field(name='Title of the image:', value=apod['title'])
					 
					 
				if "explanation" in apod.keys():
					em.add_field(name='Description of the image:', value='Please do ;desc to get the description')
				 
				if "hdurl" in apod.keys():
					em.add_field(name='URL for this image', value=apod['hdurl'])
				image = os.path.join(image_dir,title)
				await ctx.send(file=discord.File(image))
				await ctx.send(embed=em)
				
				
	@commands.command(name='description', aliases=['desc', 'd'])
	async def nasa_pic_of_the_day_desc(self, ctx):
		d = datetime.today().strftime('%Y-%m-%d')
		apod = nasa.picture_of_the_day(date=d, hd=True)
		await ctx.send(apod['explanation'])
				
				
			 
		

		
		
		
			
			
			
			
    
    
    
    
    
 
def setup(client):
  client.add_cog(AstroCog(client))
