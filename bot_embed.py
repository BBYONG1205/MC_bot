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
            embed.add_field(name=f"**직업**  `{직업}` :pick:",value="", inline=False)

        elif 직업 == "농부":
            embed.add_field(name=f"**직업**  `{직업}` :farmer:",value="", inline=False)
        
        elif 직업 == "어부":
            embed.add_field(name=f"**직업** `{직업}` :fishing_pole_and_fish:",value="", inline=False)

        elif 직업 == "요리사":
            embed.add_field(name=f"**직업**  `{직업}` :cook:",value="", inline=False)


        embed.add_field(name=f"**마크 아이디**  `{마크아이디}`", value="", inline=False)
        if 유저.avatar:      
            embed.set_thumbnail(url=유저.avatar.url)
        else:  
            embed.set_thumbnail(url="https://i.ibb.co/Vm2Gx5w/image.jpg")
     
    return embed


def 광물시세_임베드(품목명, 개당_가격, 한세트_가격,한블럭_가격,블럭세트_가격):

    embed = discord.Embed(title=f"{품목명} 시세💰", color=0xffffff)
    embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
    embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)
    embed.add_field(name=f"**1 블럭** `{한블럭_가격}원`",value="", inline=False)
    embed.add_field(name=f"**블럭 1 세트** `{블럭세트_가격}원`",value="", inline=False)
    return embed

def 정산요청서_광부(유저):



    embed = discord.Embed(title=f":clipboard: **정산 요청서**", color=0xffffff)
    embed.add_field(name=f"**광물**",value=":heart:레드스톤\n:blue_heart:청금석\n:brown_heart:구리\n:white_heart:철\n:yellow_heart:금\n:gem:다이아", inline=True)
    embed.add_field(name=f"**수량**",value=f"{레드스톤_수량}\n{청금석_수량}\n{구리_수량}\n{철_수량}\n{금_수량}\n{다이아_수량}", inline=True)

    