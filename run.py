import discord,asyncio
from discord.ext import commands
import os
import random
from lost2 import *
from lost3 import *

# 토큰 파일.txt 를 따로 사용할 경우
token_path = os.path.dirname(os.path.abspath(__file__))+"/TOKEN_BOT.txt"
t = open(token_path,"r",encoding="utf-8")

token = t.read().split()[0]
print("Token_key:",token)
game = discord.Game("%마리")
m = mari()
spec = spec()
bot = commands.Bot(command_prefix='%',status=discord.Status.online,activity=game,help_command=None)

@bot.event
async def on_ready():
    print("start bot")


@bot.command()
async def 명령어(ctx):
    content = "%마리 (골드)\n%스펙 (아이디)\n"
    await ctx.send(content)

    
@bot.command()
async def 마리(ctx,arg):
    try:
        m.set_data(arg)
        list1 = m.get_data()
    except Exception:
        list1 = ("골드를 입력하세요\n사용예) %마리 1000\n")
    await ctx.send(list1)

@마리.error
async def 마리_error(ctx,error):
    await ctx.send("골드를 입력하세요\n사용예) %마리 1000\n")

@bot.command()
async def 스펙(ctx,arg):
    try:
        spec.set_name(arg)
        str1 = spec.get_data()
    except Exception:
        str1 = "사용자를 찾을수 없습니다\n"
    await ctx.send(str1)

@스펙.error
async def 스펙_error(ctx,error):
    await ctx.send("사용자를 찾을수 없습니다\n")

# @bot.command()
# async def 주사위(ctx,*arg):
#     shuffle = arg
    



# 봇 실행 
# 토큰파일을 사용하지 않을경우 token변수 에 바로 token 코드 삽입
bot.run(token)