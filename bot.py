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

@tree.command(name="cmimc_schedule", description="cmimc event schedule", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):
        await interaction.response.send_message('''
**Friday**
```
4:00 pm | CMU Math Info @ Session Wean Hall 7500

6:00 pm	| First mini-event @ Doherty Hall and Wean Hall

7:20 pm	| Second mini-event	@ Doherty Hall and Wean Hall

8:30 pm | Early check-in @ Doherty Hall A302```

**Saturday**
```
8:30 am  | Check-in @ Doherty Hall 1212, 1209

9:30 am  | Opening ceremony @ Doherty Hall, University Center, and Wean Hall

10:00 am | Team rounds @ Doherty Hall, University Center, and Wean Hall

10:00 am | Coach talk with Po-Shen Loh @ Baker Hall A51

12:00 pm | Lunch @ Baker Hall A53

1:00 pm  | Individual rounds @ Doherty Hall, University Center, and Wean Hall

5:00 pm	 | Award ceremony @ Doherty Hall, University Center, and Wean Hall```''')

@tree.command(name="cmimc_rules", description="competition rules", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message('''
**General Rules**
```A student may leave to use the restroom during the exam, but they must turn in their phone to a proctor to do so.
No computational aids other than a writing utensil are allowed.
If a student is caught cheating on an individual round, they will get a -X for that round.
Where X is the score of the highest scoring individual on that round
If a student is caught cheating on a team-based round, their team will get a -X for that round.
Where X is the score of the highest scoring team on that round
If a proctor has reasonable suspicion to believe that a student is cheating, the proctor reserves the right to declare cheating.
Grading decisions (including TCS) can not be protested, but answer protests are welcome in the #protests-disputes channel on discord.```
''')

@tree.command(name="cmimc_format", description="competition format", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message('''
**TCS (Theoretical Computer Science) Round**
This is a 60 minute test with 2-3 problems to be completed as a team. Each question is worth the same number of points. Communication within the team is permitted. Solutions should be written in english.

**Team Round**
This is a 40 minute test with 10 problems to be completed as a team. Each question is worth the same number of points. Communication within the team is permitted. Answers must be reasonably simplified.

**Guts Round**
Teams will work together to solve sets of problems. After completing one set, the next problem set will be given. Teams cannot return to edit answers from a previous set. Communication within the team is permitted. Answers must be reasonably simplified.
''')

@tree.command(name="website", description="link to website", guild=discord.Object(id=GUILD_ID))
async def slash_command(interaction: discord.Interaction):    
    await interaction.response.send_message("https://cmimc.math.cmu.edu/about")

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