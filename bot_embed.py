import discord
from bot_firebase import 멤버정보_불러오기

def 멤버정보_임베드(유저):
    
    기존등록멤버=멤버정보_불러오기(유저.id)
    닉네임 = 기존등록멤버.get("닉네임")
    직업 = 기존등록멤버.get("직업")
    마크아이디 = 기존등록멤버.get("마크 아이디")



    if 기존등록멤버:
        embed = discord.Embed(title=f"{닉네임}님의 정보", color=0xffffff)

        if 직업 == "광부":
            embed.add_field(name='**직업**',value=f"{직업}:pick:", inline=False)

        elif 직업 == "농부":
            embed.add_field(name='**직업**',value=f"{직업}:farmer:", inline=False)
        
        elif 직업 == "어부":
            embed.add_field(name='**직업**',value=f"{직업}:fishing_pole_and_fish:", inline=False)

        elif 직업 == "요리사":
            embed.add_field(name='**직업**',value=f"{직업}:cook:", inline=False)


        embed.add_field(name="**마크 아이디**", value=f"```{마크아이디}```", inline=False)
        if 유저.avatar:      
            embed.set_thumbnail(url=유저.avatar.url)
        else:  
            embed.set_thumbnail(url="https://i.ibb.co/Vm2Gx5w/image.jpg")
     
    return embed