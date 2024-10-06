# bot.py
import os
import discord
from dotenv import load_dotenv
from discord import app_commands
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
MY_ID = int(os.getenv('DISCORD_MY_ID'))
GUILD_ID = 1287446707759743119

intents = discord.Intents.all()  # Adjust intents as necessary
client = commands.Bot(command_prefix='!', intents=intents)  # Use commands.Bot for easier command handling
tree = client.tree  # Use the command tree from commands.Bot

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    synced_commands = await tree.sync(guild=discord.Object(id=GUILD_ID))
    print(f'Synced {len(synced_commands)} commands: {synced_commands}')

@tree.command(name="cmwmc_schedule", description="cmwmc event schedule", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message('''```
9:00       Breakfast/Check-in\n
9:30       Opening ceremony\n
10:00      Individual round/Speaker Talk\n
11:15      Guts round\n
12:30      Lunch\n
1:30       Relay round\n
2:30       Sponsor Mini-events\n
4:30       Award ceremony```''')

@tree.command(name="cmwmc_format", description="competition format", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message('''
**Individual Round**
The individual round contains problems on Algebra, Number Theory, Geometry, Combinatorics, and Computer Science. 

**Relay Round**
Teams will work to solve sets of problems where each team member works on one problem of the set and passes their answer to the next team member, who will use that answer to solve their own problem, like a relay! No other communication is allowed. You don't have to wait for the person before you to finish before you start working on your problem. Only the last team member's submission will be graded.

**Guts Round**
Teams will work together to solve sets of problems. After completing one set, the next problem set will be given. Teams cannot return to edit answers from a previous set.        
''')

@tree.command(name="staff", description="staff contacts", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("For personal questions contact cmimc.info@gmail.com")

@tree.command(name="map", description="parking_info", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message('''[Google Maps](<https://www.google.com/maps/dir/Morewood+Gardens+Parking+Lot,+4902+Forbes+Ave,+Pittsburgh,+PA+15213/Doherty+Hall,+Pittsburgh,+PA/@40.4410439,-79.9478529,1720m/data=!3m1!1e3!4m14!4m13!1m5!1m1!1s0x8834f223cc46da6d:0x20fe8cbb72b0da5b!2m2!1d-79.9439412!2d40.4453379!1m5!1m1!1s0x8834f2210788dbe1:0xa75c77611d51a6dc!2m2!1d-79.9443068!2d40.4423925!3e2?entry=ttu&g_ep=EgoyMDI0MTAwMi4xIKXMDSoASAFQAw%3D%3D>) 
    https://media.discordapp.net/attachments/1287446708401475676/1292529645102694410/Screenshot_2024-10-06_at_12.51.18_PM.png?ex=67041189&is=6702c009&hm=ae7d727403290043caddfd39aa3f5ac5689727336625b437545779b33aef5e8c&=&format=webp&quality=lossless&width=1208&height=1138''')

@tree.command(name="sponsors", description="sponsorships", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("here ")

client.run(TOKEN)