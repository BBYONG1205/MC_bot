import discord
from bot_firebase import 멤버정보_불러오기

async def 멤버정보_임베드(interaction: discord.Interaction, 유저: discord.Member):
    기존등록멤버=멤버정보_불러오기(유저.id)
    
    if 기존등록멤버:
        embed = discord.Embed(title=f"{유저.display_name}님의 정보", color=0xffffff)
        embed.add_field(name="닉네임", value=기존등록멤버.get("닉네임"), inline=False)
        if 유저.avatar:      
            embed.set_thumbnail(url=유저.avatar.url)
        else:  
            embed.set_thumbnail(url="https://i.ibb.co/Vm2Gx5w/image.jpg")
        embed.add_field(name='직업',value=기존등록멤버.get("직업"))