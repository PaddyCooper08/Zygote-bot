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





class RpgCog(commands.Cog):
  def __init__(self, client):
    self.client = client
  @commands.command(name="start")
  async def start_rpg(self, ctx):
    await ctx.channel.send(
        "Hello, my name is Zygote and I'm here to guid you through your journey in Nevermarsh. Nevermarsh is in grave danger and we need your help. The gelatinous cube has escaped his prison and is rampaging though the seven kingdoms. Please do ';tutorial' to find out the commands"
    )

  async def get_bank_data(self):
    with open('mainbank.json', 'r') as f:
      users = json.load(f)

      return users
  @commands.command(name="tutorial")
  async def rpg_tutorial(self, ctx):
      await ctx.channel.send(
          "You can do ';hp' to find out how many health points you have. If you lose all 20 you lose a random item"
      )


  @commands.command(name="hp")
  async def current_hp(self, ctx):
    await self.open_account(ctx)
    user = ctx.author

    users = await self.get_bank_data()

    curr_hp = users[str(user.id)]["hp"]
    
    await ctx.channel.send(curr_hp)


  '''
  async def edit_json():
    user = ctx.author
    users = await self.get_bank_data()
    earnings = int("5")
    users[str(user.id)]["hp"] += earnings


    with open("mainbank.json",'w') as f:
      json.dump(users,f)
    wallet_amt = users[str(user.id)]["hp"]
  '''
  mainshop = [{
      "name": "Stone Sword - 01",
      "price": 100,
      "description": "A good second sword"
  }, {
      "name": "Leather armour - 02",
      "price": 1000,
      "description": "Your first armour, plus 5hp"
  }, {"name": "Health Potion - 03", "price": 100, "description": "Heals you to your max hp"}, 
  {"name": "Hermes boots - 04", "price": 5000, "description": "Fly like the god hermes, lowers agility by 3"},
  {"name": "Fishing rod - 05", "price": 1000, "description": "You need this to fish"}]


  @commands.command(name="xyz1")
  async def give_100_bank(self, ctx):
      user = ctx.author
      users = await self.get_bank_data()
      earnings = int("100")
      users[str(user.id)]["bank"] += earnings

      with open("mainbank.json", 'w') as f:
          json.dump(users, f)
      bank_amt = users[str(user.id)]["bank"]
      await ctx.channel.send(bank_amt)


  @commands.command(name="shop")
  async def shop1(self, ctx):
      em = discord.Embed(title="Shop")

      for item in self.mainshop:
          name = item["name"]
          price = item["price"]
          desc = item["description"]

          em.add_field(name=name, value=f"£{price} | {desc}")
      await ctx.channel.send(embed=em)


  async def open_account(self, ctx):
    user = ctx.author
    users = await self.get_bank_data()

    if str(user.id) in users:
      return False
    else:
      users[str(user.id)] = {}
      users[str(user.id)]["hp"] = 20
      users[str(user.id)]["bank"] = 100
      users[str(user.id)]["leather_armour"] = 0
      users[str(user.id)]['stone_sword'] = 0
      users[str(user.id)]['health_potion'] = 5
      users[str(user.id)]['maxhp'] = 20
      users[str(user.id)]['kingdom'] = 1
      users[str(user.id)]['max_damage'] = 5
      users[str(user.id)]['min_damage'] = 1
      users[str(user.id)]['xp'] = 0
      users[str(user.id)]['agility'] = 20
      users[str(user.id)]['hermes_boots'] = 0
      users[str(user.id)]['leather_armour_equipped'] = 0
      users[str(user.id)]['stone_sword_equipped'] = 0
      users[str(user.id)]['no_sword'] = 1
      users[str(user.id)]['no_armour'] = 1
      users[str(user.id)]['fishing_rod'] = 0
      users[str(user.id)]['fishing_luck'] = 500
      users[str(user.id)]['fishing_rod_equipped'] = 0
      users[str(user.id)]['no_rod'] = 1
      users[str(user.id)]['no_boots'] = 1
      users[str(user.id)]['hermes_boots_equipped'] = 0
      with open('mainbank.json', 'w') as f:
          json.dump(users, f)

          return True

      
      
    





  @commands.command(name="buy_01")
  async def buy_stone_sword(self, ctx):
      users = await self.get_bank_data()
      get_bank_data
      user = ctx.author
      bank_amt = users[str(user.id)]["bank"]

      if bank_amt < 100:
          await ctx.channel.send("You don't have enough money to buy this :(")

      else:

          with open("mainbank.json", "w") as write_file:
              price_01 = 100
              users[str(user.id)]['bank'] -= price_01
              users[str(user.id)]['stone_sword'] += 1
              bank_amt = users[str(user.id)]["bank"] - price_01
              await ctx.channel.send('Success')

              json.dump(users, write_file)


  @commands.command(name='bal')
  async def print_bal(self, ctx):
      user = ctx.author
      await self.open_account(ctx)
      users = await self.get_bank_data()
      
      bank_amt = users[str(user.id)]['bank']

      await ctx.channel.send(bank_amt)


  @commands.command(name="inv")
  async def inventory(self, ctx):
      user = ctx.author
      users = await self.get_bank_data()
      em = discord.Embed(title="Inventory", color=discord.Color.purple())
      em2 = discord.Embed(title="Equipped Items", color=discord.Color.purple())

      

          

      if users[str(user.id)]['stone_sword'] > 0 :
        stone_sword_amount = users[str(user.id)]['stone_sword']
        em.add_field(name='Stone Sword', value=str(stone_sword_amount), inline=False) 

      
    

          
          

      if users[str(user.id)]['leather_armour'] > 0 :
          leather_armour_amount = users[str(user.id)]['leather_armour'] 
          em.add_field(name='Leather Armour', value=str(leather_armour_amount), inline=False)
      
          

      if users[str(user.id)]['health_potion'] > 0 :
          users = await self.get_bank_data()
          health_potion_amount = users[str(user.id)]['health_potion']
          em.add_field(name='Health Potion', value=str(health_potion_amount), inline=False)
      

      if users[str(user.id)]['hermes_boots'] > 0 :
          users = await self.get_bank_data()
          hermes_boots_amount = users[str(user.id)]['hermes_boots']
          em.add_field(name='Hermes Boots', value=str(hermes_boots_amount), inline=False)

      if users[str(user.id)]['leather_armour_equipped'] == 1:
        users = await self.get_bank_data()
        em2.add_field(name='Armour', value='Leather Armour', inline=False)

      if users[str(user.id)]['no_armour'] == 1:
        users = await self.get_bank_data()
        em2.add_field(name='Armour', value='None', inline=False)
      

      if users[str(user.id)]['stone_sword_equipped'] > 0:
        users = await self.get_bank_data()
        em2.add_field(name='Sword', value='Stone sword', inline=False)

      if users[str(user.id)]['no_sword'] > 0:
        users = await self.get_bank_data()
        em2.add_field(name='Sword', value='Wooden', inline=False)
        
      if users[str(user.id)]['fishing_rod'] > 0:
        rod_amt = users[str(user.id)]['fishing_rod']
        users = await self.get_bank_data()
        em.add_field(name='Fishing rod', value=str(rod_amt), inline=False)
        
      if users[str(user.id)]['no_rod'] > 0:
        rod_amt = users[str(user.id)]['fishing_rod']
        users = await self.get_bank_data()
        em2.add_field(name='Rod', value='None', inline=False)

      if users[str(user.id)]['fishing_rod_equipped'] > 0:
        users = await self.get_bank_data()
        em2.add_field(name='Rod', value='Fishing rod', inline=False)

      if users[str(user.id)]['no_boots'] == 1:
        users = await self.get_bank_data()
        em2.add_field(name='Boots', value='None', inline=False)


      if users[str(user.id)]['hermes_boots_equipped'] == 1:
        users = await self.get_bank_data()
        em2.add_field(name='Boots', value='Hermes boots', inline=False)

        


      


      
          
          

      await ctx.channel.send(embed=em)
      await ctx.channel.send(embed=em2)


  @commands.command(name="buy_02")
  async def buy_leather_armour(self, ctx):
      users = await self.get_bank_data()
      get_bank_data
      user = ctx.author
      bank_amt = users[str(user.id)]["bank"]

      if bank_amt < 1000:
          await ctx.channel.send("You don't have enough money to buy this :(")

      else:

          with open("mainbank.json", "w") as write_file:
              price_02 = 1000
              users[str(user.id)]['bank'] -= price_02
              users[str(user.id)]['leather_armour'] += 1
              users[str(user.id)]['leather_armour_equipped'] = 0
              await ctx.channel.send('Success')

              json.dump(users, write_file)


  @commands.command(name="equip_leather_armour")
  async def equip_leather_armour1(self, ctx):
      users = await self.get_bank_data()
      user = ctx.author
      if users[str(user.id)]['leather_armour'] == int('1'):
          with open('mainbank.json', 'w') as write_file:
              users[str(user.id)]['leather_armour_equipped'] == int('1')
              users[str(user.id)]['no_armour'] == 0
              users[str(user.id)]['leather_armour'] -= 1
              await ctx.channel.send('Success')
              users[str(user.id)]['maxhp'] += 5

              json.dump(users, write_file)

      else:
          await ctx.channel.send("You don't own leather armour, get it first")





  @commands.command(name='adv')
  async def adventure(self, ctx):
    await self.open_account(ctx)
    user = ctx.author

    users = await self.get_bank_data()

    wallet_amt = users[str(user.id)]["hp"]
    if wallet_amt <= int("0"):
      await ctx.channel.send(
        "You can't go adventuring without any hp, consider healing up with a health potion"
          )


  @commands.command(name="heal")
  async def use_health_pot(self, ctx):
      user = ctx.author
      users = await self.get_bank_data()
      health_potion_amount = users[str(user.id)]['health_potion']
      if health_potion_amount > int('0'):
          with open('mainbank.json', 'r') as f:
              users = json.load(f)
          wallet_amt = users[str(user.id)]["hp"]
          max_hp = users[str(user.id)]['maxhp']
          users[str(user.id)]['hp'] = max_hp

          users[str(user.id)]['health_potion'] -= int('1')
          health_potion_amount = users[str(user.id)]['health_potion']
          message3 = 'You now have ' + str(
              health_potion_amount) + ' health potions left'
          with open("mainbank.json", 'w') as f:
              json.dump(users, f)

          await ctx.channel.send(message3)

      else:
          await ctx.channel.send('You need a health potion to heal dummy')


  fightmap = [{
      "name": "Goblin - 01",
      "difficulty": " easy",
      "description": "5hp, 1 attack - the easiest monster"
  }, {"name": "Sand Shark - 02", "difficulty": " easy", "description": "10hp, 3 attack - a fairly easy monster"}]


  @commands.command(name='fight')
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def go_fight(self, ctx):
      em = discord.Embed(title="Fight")
      for item in self.fightmap:
          name = item["name"]
          price = item["difficulty"]
          desc = item["description"]

          em.add_field(name=name, value=f"Difficulty:{price} | {desc}")
      await ctx.channel.send(embed=em)
      await ctx.channel.send(
          'Do ";fight_" then the number next to the monsters name on the Fight list'
      )

  async def goblin_fight_sequence(self, ctx):
    
          
    await asyncio.sleep(1.5) #use await asyncio.sleep(1.5) here rather
    rng3 = random.randint(1, 10)
    if rng3 == int('3') or int('4') or int('7'):
              
      user = ctx.author
      users = await self.get_bank_data()
      agility = users[str(user.id)]['agility']
      if random.randint(1, agility) == 2:
        await ctx.channel.send("You dodged the goblin's attack") 
        
      else:
        
        await ctx.channel.send('The goblin hit you so you lost 1 hp')   
        users[str(user.id)]['hp'] -= int('1') 

                  
    
      dmg = users[str(user.id)]['max_damage'] #You forgot an ] here so I replaced it
      rng4 = random.randint(0, dmg)
      rng5 = str(rng4)
      users[str(user.id)]['rng'] = rng4
      await asyncio.sleep(1.5) #use await asyncio.sleep(1.5) here rather
      content1 = 'You did ' + rng5 + ' damage'
      users[str(user.id)]['goblin_hp_json'] -= int(rng4)
      with open("mainbank.json", 'w') as f:
        json.dump(users, f)
      users = await self.get_bank_data()
      await ctx.channel.send(content1)




  async def sandshark_fight_sequence(self, ctx):
    
          
    await asyncio.sleep(1.5) #use await asyncio.sleep(1.5) here rather
    rng3 = random.randint(1, 10)
    if rng3 == int('3') or int('4') or int('7'):
              
      user = ctx.author
      users = await self.get_bank_data()
      agility = users[str(user.id)]['agility']
      if random.randint(1, agility) == 2 :
        await ctx.channel.send("You dodged the sand shark's attack")
          
      else:
        
        await ctx.channel.send('The sand shark hit you so you lost 3 hp')   
        users[str(user.id)]['hp'] -= int('3')

                  
    
      dmg = users[str(user.id)]['max_damage'] #You forgot an ] here so I replaced it
      min_dmg = users[str(user.id)]['min_damage']
      rng4 = random.randint(min_dmg, dmg)
      rng5 = str(rng4)
      users[str(user.id)]['rng'] = rng4
      await asyncio.sleep(1.5) #use await asyncio.sleep(1.5) here rather
      content1 = 'You did ' + rng5 + ' damage'
      users[str(user.id)]['sandshark_hp_json'] -= int(rng4)
      with open("mainbank.json", 'w') as f:
        json.dump(users, f)
      users = await self.get_bank_data()
      await ctx.channel.send(content1)











              
                    
      
          
  

  @commands.command(name="buy_03")
  async def buy_health_pot(self, ctx):
      users = await self.get_bank_data()
      
      user = ctx.author
      bank_amt = users[str(user.id)]["bank"]

      if bank_amt < 100:
          await ctx.channel.send("You don't have enough money to buy this :(")

      else:

          with open("mainbank.json", "w") as write_file:
              price_03 = 100
              users[str(user.id)]['bank'] -= price_03            
              users[str(user.id)]['health_potion'] += 1            
              bank_amt = users[str(user.id)]["bank"] - price_03
              await ctx.channel.send('Success')
            
              json.dump(users, write_file)


  

          

  @commands.command(name="stats")
  async def stats_embed(self, ctx):
    users = await self.get_bank_data()
    user = ctx.author
    min_dmg = users[str(user.id)]['min_damage']
    max_dmg = users[str(user.id)]['max_damage']
    agility = users[str(user.id)]['agility']
    max_hp = users[str(user.id)]['maxhp']
    fish_luck = users[str(user.id)]['fishing_luck']
    em = discord.Embed(title="Stats", color=discord.Color.purple())
    em.add_field(name='Minimum damage', value=str(min_dmg), inline=False)
    em.add_field(name='Maximum damage', value=str(max_dmg), inline=False)
    em.add_field(name='Agility', value=str(agility) + ' (The lower the better)', inline=False)
    em.add_field(name='Max HP', value=str(max_hp), inline=False)
    em.add_field(name='Fishing luck', value=str(fish_luck), inline= False)
    await ctx.channel.send(embed=em)


  @commands.command(name="buy_04")
  async def buy_hermes_boots(self, ctx):
      users = await self.get_bank_data()
      
      user = ctx.author
      bank_amt = users[str(user.id)]["bank"]

      if bank_amt < 5000:
          await ctx.channel.send("You don't have enough money to buy this :(")

      else:

          with open("mainbank.json", "w") as write_file:
              price_01 = 5000
              users[str(user.id)]['bank'] -= price_01
              users[str(user.id)]['hermes_boots'] += 1
            
              await ctx.channel.send('Success')

              json.dump(users, write_file)


  @commands.command(name="equip_stone_sword")
  async def equip_stone_sword1(self, ctx):
      users = await self.get_bank_data()
      user = ctx.author
      if users[str(user.id)]['stone_sword'] > 0:
          with open('mainbank.json', 'w') as write_file:
              users[str(user.id)]['stone_sword_equipped'] = 1
              users[str(user.id)]['stone_sword'] -= 1
              users[str(user.id)]['no_sword'] -= 1
              await ctx.channel.send('Success')
              users[str(user.id)]['max_damage'] = 15

              json.dump(users, write_file)

      else:
          await ctx.channel.send("You don't own a stone sword, get it first")
      
  @commands.command(name="buy_05")
  async def buy_fishing_rod(self, ctx):
      users = await self.get_bank_data()
      
      user = ctx.author
      bank_amt = users[str(user.id)]["bank"]

      if bank_amt < 1000:
          await ctx.channel.send("You don't have enough money to buy this :(")

      else:

          with open("mainbank.json", "w") as write_file:
              price_05 = 1000
              users[str(user.id)]['bank'] -= price_05
              users[str(user.id)]['fishing_rod'] += 1
        
              await ctx.channel.send('Success')

              json.dump(users, write_file)

  @commands.command(name="equip_fishing_rod")
  async def equip_rod(self, ctx):
      users = await self.get_bank_data()
      user = ctx.author
      if users[str(user.id)]['fishing_rod'] > 0:
          with open('mainbank.json', 'w') as write_file:
              users[str(user.id)]['fishing_rod_equipped'] = 1
              users[str(user.id)]['no_rod'] = 0
              users[str(user.id)]['fishing_rod'] -= 1
              await ctx.channel.send('Success')
              users[str(user.id)]['fishing_luck'] -= 10
              

              json.dump(users, write_file)

      else:
          await ctx.channel.send("You don't own a fishing rod, get it first")

  @commands.command(name='fish')
  async def go_fish(self, ctx):
    users = await self.get_bank_data()
    user = ctx.author
    if users[str(user.id)]['no_rod'] == 1:
      await ctx.channel.send('Lol, imagine not having a rod')
     
    else:
      luck = users[str(user.id)]['fishing_luck']
      rng = random.randint(1, luck)
      if rng in (1, 5, 6, 9, 3, 4, 10):
        await ctx.channel.send('You caught a small fish, well done')
        users[str(user.id)]['small_fish'] += 1
        with open('mainbank.json', 'w') as f:
          json.dump(users, f)

      else:
        await ctx.channel.send("Lol, u didn't catch anything")
      
    


  @commands.command(name='fight_01')
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def fight_goblin(self, ctx):
      users = await self.get_bank_data()
      user = ctx.author
      rng1 = random.randint(1, 3)
      hp = users[str(user.id)]['hp']
      users[str(user.id)]['goblin_hp_json'] = 5
      with open("mainbank.json", 'w') as f:
        json.dump(users, f)
      rng2 = random.randint(1, 3)
      if rng1 == int('2'):
          await ctx.channel.send("You searched all around and couldn't find a goblin, try again next time :(")

      elif hp <= 0:
        await ctx.channel.send("You can't go adventuring with no hp you idiot")
          
              
    


      #Define this as async then remove the set hp to 5.
      #THen call it using the loop that the stackoverflow guy gave
      else:
        await ctx.channel.send('You encountered a wild goblin!')

        while True: #an infinite loop
          user = ctx.author
          users = await self.get_bank_data()
          goblin_hp = users[str(user.id)]['goblin_hp_json']
          if users[str(user.id)]['hp'] <= 0:
            await asyncio.sleep(1.5)
            await ctx.channel.send('You died, better luck next time')
                      #If your command stop here you can use return, else use break to get out of the loop, here I will use break
            break
          if goblin_hp <= 0:
            rng5 = users[str(user.id)]['rng']
            content3 = 'You killed the goblin, well done'
            await ctx.channel.send(content3)
            rng6 = random.randint(20, 100)
            users[str(user.id)]['bank'] += rng6
            rng7 = random.randint(1, 20)
            await asyncio.sleep(0.8) #use await asyncio.sleep(0.8) here rather
            content4 = 'You gained ' + str(rng6) + ' coins for defeating the goblin'
      
            users[str(user.id)]['xp'] += rng7          
            await ctx.channel.send(content4)
            await asyncio.sleep(0.8)
          
            with open("mainbank.json", 'w') as f:
              json.dump(users, f)
                      #Same here, I will use break
            
            return
          else:
            await self.goblin_fight_sequence(ctx)
                    #(This is where I want it to return to the first else: statement)
                    #Here you can use continue to repeat your loop, or just delete this part (an you will return to the first if). To match with your current code, I will use continue
                    #continue

  @commands.command(name='fight_02')
  @commands.cooldown(1, 30, commands.BucketType.user)
  async def fight_sand_shark(self, ctx):
      users = await self.get_bank_data()
      user = ctx.author
      rng1 = random.randint(1, 3)
      hp = users[str(user.id)]['hp']
      users[str(user.id)]['sandshark_hp_json'] = 10
      with open("mainbank.json", 'w') as f:
        json.dump(users, f)
      rng2 = random.randint(1, 3)
      if rng1 == int('2'):
          await ctx.channel.send("You searched all around and couldn't find a sand shark, try again next time :(")

      elif hp <= 0:
        await ctx.channel.send("You can't go adventuring with no hp you idiot")
          
              
    


      #Define this as async then remove the set hp to 5.
      #THen call it using the loop that the stackoverflow guy gave
      else:
        await ctx.channel.send('You encountered a wild sand shark!')

        while True: #an infinite loop
          user = ctx.author
          users = await self.get_bank_data()
          sandshark_hp = users[str(user.id)]['sandshark_hp_json']
          if users[str(user.id)]['hp'] <= 0:
            await asyncio.sleep(1.5)
            await ctx.channel.send('You died, better luck next time')
                      #If your command stop here you can use return, else use break to get out of the loop, here I will use break
            break
              
                    
      
          elif sandshark_hp <= 0:
            rng5 = users[str(user.id)]['rng']
            content3 = 'You killed the sand shark, well done'
            await ctx.channel.send(content3)
            rng6 = random.randint(20, 120)
            users[str(user.id)]['bank'] += rng6
            rng7 = random.randint(1, 25)
            await asyncio.sleep(0.8) #use await asyncio.sleep(0.8) here rather
            content4 = 'You gained ' + str(rng6) + ' coins for defeating the sand shark'
      
            users[str(user.id)]['xp'] += rng7          
            await ctx.channel.send(content4)
            await asyncio.sleep(0.8)
            
            with open("mainbank.json", 'w') as f:
              json.dump(users, f)
                      #Same here, I will use break
            
            return
          else:
            await self.sandshark_fight_sequence(ctx)


  @commands.command(name='equip_hermes_boots')
  async def equip_hermes(self, ctx):
    users = await self.get_bank_data()
    user = ctx.author
     
    if users[str(user.id)]['hermes_boots']  <= 0:
      await ctx.channel.send("You can't equip something you don't own dumbass")

    elif users[str(user.id)]['hermes_boots_equipped'] == 1:
      await ctx.channel.send("You can't equip something twice you plonker")

    else:
      users[str(user.id)]['hermes_boots_equipped'] = 1
      users[str(user.id)]['agility'] -= 3
      users[str(user.id)]['no_boots'] = 0
      with open("mainbank.json", 'w') as f:
        json.dump(users, f)
      await ctx.channel.send('Success')

  






def setup(client):
  client.add_cog(RpgCog(client))