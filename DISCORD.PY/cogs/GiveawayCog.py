import discord
from discord.ext import commands
import random
from discord.ext import commands
from dotenv import load_dotenv
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps
import json

import asyncio
import datetime




class GiveawayCog(commands.Cog):
  def __init__(self, client):
    self.client = client

  

  @commands.command()
  @commands.has_role("Head Coder")
  async def gstart(self, ctx, mins : int, *, prize: str):
    em = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)


    end = datetime.datetime.utcnow() + datetime.timedelta(seconds = mins*60)

    em.add_field(name="Ends At:", value = f"{end} UTC")
    em.set_footer(text = f"Ends {mins} minutes from now!")

    my_msg = await ctx.send(embed = em)
    await my_msg.add_reaction("🎉")

    await asyncio.sleep(mins)

    new_msg = await ctx.channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(self.client.user))
    winner = random.choice(users)
    await ctx.send(f"Congratualtions! {winner.mention} won {prize}!")



  def convert(self, time):
    pos = ["s", "m", "h", "d"]

    time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d" : 3600*24}
    unit = time[-1]
    if unit not in pos:
      return -1

    try:
      val = int(time[:-1])

    except:
      return -2


    return val * time_dict[unit]


  @commands.command(name='giveaway')
  @commands.has_role('Head Coder')
  async def giveaway(self, ctx):
    em = discord.Embed(title='Giveaway setup', color=ctx.author.color)
    em.add_field(name="Let's start this giveaway!", value="Answer these questions within 15 seconds!")
    await ctx.send(embed=em)


    questions = ["Which channel should it be hosted in?",
    "What should be the duration of the giveaway? (s|m|h|d",
    "What is the prize of the giveaway?"]

    answers = []

    def check(m):
      return m.author == ctx.author and m.channel == ctx.channel


    for i in questions:
      em2 = discord.Embed(title="Question:", color=ctx.author.color)
      em2.add_field(name="Please answer this within 15 seconds", value=(i))
      await ctx.send(embed=em2)


      try:
        msg = await self.client.wait_for('message', timeout=15.0, check=check)


      except asyncio.TimeoutError:
        em3 = discord.Embed(title='Error', color=ctx.author.color)
        em3.add_field(name='Giveaway creation failed', value=f"{ctx.author.mention} you're too slow, please be quicker next time")
        await ctx.send(embed=em3)
        return


      else:
        answers.append(msg.content)


    try:
      c_id = int(answers[0][2:-1])

    except:
      em4 = discord.Embed(title='Error', color=ctx.author.color)
      em4.add_field(name='Giveaway creation failed', value=f"{ctx.author.mention} you didn't mention a channel properly. Do it like this {ctx.channel.mention} next time")
      await ctx.send(embed=em4)
      return

    channel = self.client.get_channel(c_id)

    time = self.convert(answers[1])
    if time == -1:
      em5 = discord.Embed(title='Error', color=ctx.author.color)
      em5.add_field(name='Giveaway creation failed', value=f"{ctx.author.mention} you didnt' answer the time with a proper unit. Do it like this: 4d or 1hr or 10s or 12m")
      await ctx.send(embed=em5)
      return

    elif time == -2:
      em6 = discord.Embed(title='Error', color=ctx.author.color)
      em6.add_field(name='Giveaway creation failed', value=f"{ctx.author.mention} The time must be an integer such as 4 not four.")
      await ctx.send(embed=em6)
      return

    prize = answers[2]

    em7 = discord.Embed(title='Success!', color=ctx.author.color)
    em7.add_field(name='Giveaway channel:', value=f"It will be in {channel.mention}", inline=False)
    em7.add_field(name='Giveaway length:', value=f"It will last {time}", inline=False)
    em7.add_field(name='Giveaway prize:', value=f"The prize will be {prize}", inline=False)
    await ctx.send(embed=em7)



    em = discord.Embed(title = "Giveaway!", description = f"Prize: {prize}", color = ctx.author.color)
    em.add_field(name="Hosted by:", value= ctx.author.mention)



   
    em.set_footer(text = f"Ends {answers[1]} from now!")

    my_msg = await channel.send(embed = em)
    await my_msg.add_reaction("🎉")

    await asyncio.sleep(time)

    new_msg = await channel.fetch_message(my_msg.id)

    users = await new_msg.reactions[0].users().flatten()
    users.pop(users.index(self.client.user))
    winner = random.choice(users)
    await channel.send(f"Congratulations! {winner.mention} won {prize}!")  









    

      
    











def setup(client):
  client.add_cog(GiveawayCog(client))