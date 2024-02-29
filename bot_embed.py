import discord
from bot_firebase import 멤버정보_불러오기, 정산요청서_불러오기, 정산요청상세_불러오기

def 멤버정보_임베드(유저):
    
    기존등록멤버=멤버정보_불러오기(유저.id)
    닉네임 = 기존등록멤버.get("닉네임")
    직업 = 기존등록멤버.get("직업")
    마크아이디 = 기존등록멤버.get("마크 아이디")

    

    if 기존등록멤버:
        embed = discord.Embed(title=f"{닉네임}님의 정보 :identification_card:", color=0xffffff)

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

    embed = discord.Embed(title=f"{품목명} 시세 💰", color=0xffffff)
    embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
    embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)
    embed.add_field(name=f"**1 블럭** `{한블럭_가격}원`",value="", inline=False)
    embed.add_field(name=f"**블럭 1 세트** `{블럭세트_가격}원`",value="", inline=False)
    return embed

def 일반시세_임베드(품목명, 개당_가격, 한세트_가격):

    embed = discord.Embed(title=f"{품목명} 시세 💰", color=0xffffff)
    embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
    embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)
    return embed


def 정산요청서(정산요청자_닉네임):

        
    요청자 = f"{정산요청자_닉네임}님의 정산 요청 내역"
    총금액 = 정산요청서_불러오기(요청자).get("총 금액")
    품목명_리스트, 금액_리스트 , 세트_리스트= 정산요청상세_불러오기(요청자)
    
    품목명_필드 = "\n".join([f"{품목명}" for 품목명 in 품목명_리스트])
    금액_필드 = "\n".join([f"{금액}원" for 금액 in 금액_리스트])
    세트_필드 = "\n".join([f"{세트}세트" for 세트 in 세트_리스트])

    총금액 = "{:,}".format(총금액)
    embed = discord.Embed(title=f"**{정산요청자_닉네임}님의 정산 요청 내역** :clipboard:", description="===========================", color=0xffffff)

    embed.add_field(name="**품목명**",value=f"{품목명_필드}", inline=True)
    embed.add_field(name="**수량**",value=f"{세트_필드}", inline=True)
    embed.add_field(name="**금액**",value=f"{금액_필드}", inline=True)
    embed.add_field(name="",value="===========================", inline=False)
    embed.add_field(name=f"**총 금액** `{총금액}원`",value="", inline=True)

    return embed