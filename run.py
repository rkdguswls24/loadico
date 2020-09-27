import discord,asyncio
from discord.ext import commands
import os
from lost2 import *

# 토큰 파일.txt 를 따로 사용할 경우
token_path = os.path.dirname(os.path.abspath(__file__))+"/TOKEN_BOT.txt"
t = open(token_path,"r",encoding="utf-8")

token = t.read().split()[0]
print("Token_key:",token)
game = discord.Game("!마리")
m = mari()
bot = commands.Bot(command_prefix='!',status=discord.Status.online,activity=game,help_command=None)


@bot.event
async def on_ready():
    print("start bot")

@bot.command()
async def 마리(ctx,arg):
    m.set_data(arg)
    list1 = m.print_data()
    await ctx.send(list1)

# 봇 실행 
# 토큰파일을 사용하지 않을경우 token변수 에 바로 token 코드 삽입
bot.run(token)