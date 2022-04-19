import malclient
import discord 
from discord.ext import commands, tasks
import urllib.request , json
import asyncio
import math
class info (commands.Cog):
    def __init__(self, client):
        self.client = client

    """
    @commands.command(name = "add2")
    async def _add2(self, ctx, member : discord.Member, puntuation):
        if(puntuation[0]=="~"):
            puntuation = int(puntuation[1:])
            with open("./data.json", "r") as f:
                users = json.load(f)
            if str(member) in users:
                users[str(member)]["Points"] += int(puntuation)
            else:
                users[str(member)] = {}
                users[str(member)]["Points"] = int(puntuation)
            with open("data.json", "w") as f:
                json.dump(users,f, indent=4)      
        
        else:
            pass
    """
    @commands.command(name = "add")
    async def _add(self, ctx,*, all):
        role = discord.utils.get(ctx.guild.roles, id = 755569864013250621)
        if role in ctx.author.roles:
            all = all.replace(" ","").split("~")
            print(all)
            member = all[0]
            puntuation = int(all[1])
            member = await self.client.fetch_user(member[3:-1])
            
            with open("./data.json", "r") as f:
                users = json.load(f)
            if str(member) in users:
                users[str(member)]["Points"] += int(puntuation)
            else:

                users[str(member)] = {}
                users[str(member)]["Points"] = int(puntuation)
            with open("data.json", "w") as f:
                json.dump(users,f, indent=4)      
                await ctx.send(f"Puntos añadidos a el usuario {member.name}")
        else:
            await ctx.send("You dont have enough Permissions")


    @commands.command(name = "remove")
    async def _remove(self, ctx,*, all):
        role = discord.utils.get(ctx.guild.roles, id = 755569864013250621)
        if role in ctx.author.roles:
            all = all.replace(" ","").split("~")
            print(all)
            member = all[0]
            puntuation = int(all[1])
            member = await self.client.fetch_user(member[3:-1])
            
            with open("./data.json", "r") as f:
                users = json.load(f)
            if str(member) in users:
                users[str(member)]["Points"] -= int(puntuation)
            else:
                pass
            with open("data.json", "w") as f:
                json.dump(users,f)        
                await ctx.send(f"Puntos retirados a el usuario {member.name}")
        else:
            await ctx.send("You dont have enough Permissions")
def setup (client):
    client.add_cog(info(client))
    print("infoBot cog is loaded!")
