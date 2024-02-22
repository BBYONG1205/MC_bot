import discord
from typing import Literal
from bot_firebase import 멤버정보_저장, 멤버정보_불러오기, 시세_불러오기, 시세_업데이트
from bot_embed import 멤버정보_임베드, 광물시세_임베드
from bot_marketprice import 자원시세_계산
import pyperclip



async def 멤버등록(interaction: discord.Interaction, 유저:discord.Member, 닉네임:str, 직업: Literal["광부", "농부", "어부", "요리사"], 마크아이디: str):
    
    print(f"멤버 등록 요청 : {interaction.user.display_name} \n 입력 닉네임 : {닉네임}")

    기존등록멤버 = 멤버정보_불러오기(유저.id)

    if 기존등록멤버:
        await interaction.response.send_message("이미 등록되어있는 멤버입니다.")
        return
    
    멤버정보 = {"유저":유저.global_name, "닉네임": 닉네임, "직업" : 직업, "마크 아이디": 마크아이디}
    멤버정보_저장(유저.id, 멤버정보)
    
    embed = 멤버정보_임베드(유저)

    await interaction.response.send_message("멤버 등록이 완료되었습니다.", embed=embed, ephemeral=True)
    return


async def 정보(interaction: discord.Interaction, 유저:discord.Member):

    기존등록멤버 = 멤버정보_불러오기(유저.id)

    if 기존등록멤버 is None:
        await interaction.response.send_message("등록되지 않은 멤버입니다.", ephemeral=True)
        return


    embed = 멤버정보_임베드 (유저)

    await interaction.response.send_message(embed=embed)
    return


async def 복사(interaction: discord.Interaction, 유저:discord.Member):
    기존등록멤버 = 멤버정보_불러오기(유저.id)

    if 기존등록멤버 is None:
        await interaction.response.send_message("등록되지 않은 멤버입니다.", ephemeral=True)
        return
    
    마크아이디 = 기존등록멤버.get("마크 아이디")

    pyperclip.copy(마크아이디)

    await interaction.response.send_message(f"{유저.display_name} 의 마크 아이디가 복사되었습니다.\n```{마크아이디}```", ephemeral=True)
    return


async def 정산요청(interaction: discord.Interaction):

    정산요청자 = interaction.user.id
    기존등록멤버 = 멤버정보_불러오기(정산요청자)
    정산요청자_직업 = 정산요청자.get("직업")

    if 기존등록멤버 is None:
        await interaction.response.send_message("멤버 등록이 되어있지 않아 정산 요청 작업에 실패하였습니다.", ephemeral=True)
        return
    
    if 정산요청자_직업 == "광부":
        자원 = "광물"
        시세 = 시세_불러오기(자원)
    

    if 정산요청자_직업 == "농부":
        자원 = "농산물"
        시세 = 시세_불러오기(자원)


    if 정산요청자_직업 == "어부":
        자원 = "물고기"
        시세 = 시세_불러오기(자원)


async def 시세_확인(interaction: discord.Interaction, 품목명 : str):

    광물 = ["청금석","레드스톤","금","철","구리","다이아","금 원석"]

    농작물 = ["가지","파인애플","홉","토마토","고추","마늘","양배추","배추","포도"]

    물고기 = ["강꼬치고기","개복치","금붕어","농어","다랑어","메기","문어","숭어","연어","잉어","잡어","적색통돔","정어리"]
    
    if 품목명 not in 광물 and 품목명 not in 농작물 and 품목명 not in 물고기:
        await interaction.response.send_message(f"올바르지 않은 품목명입니다.\n입력 값 : __**{품목명}**__",ephemeral=True)
        return
    
    if 품목명 in 광물:

        if 품목명 == "금 원석":
            자원 = "광물"
            개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격 = 자원시세_계산(자원, 품목명)

            embed = discord.Embed(title=f"{품목명} 시세💰", color=0xffffff)
            embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
            embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)

            await interaction.response.send_message(embed=embed)
            return
        
        else:    

            자원 = "광물"
            개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격 = 자원시세_계산(자원, 품목명)

            embed = 광물시세_임베드(품목명, 개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격)


            await interaction.response.send_message(embed=embed)
            return

    if 품목명 in 농작물:

        자원 = "농작물"

        개당_가격, 한세트_가격= 자원시세_계산(자원, 품목명)

        embed = discord.Embed(title=f"{품목명} 시세💰", color=0xffffff)
        embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
        embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)

        await interaction.response.send_message(embed=embed)

        return
    
    if 품목명 in 물고기:

        자원 = "물고기"

        개당_가격, 한세트_가격= 자원시세_계산(자원, 품목명)

        embed = discord.Embed(title=f"{품목명} 시세💰", color=0xffffff)
        embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
        embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)

        await interaction.response.send_message(embed=embed)

        return
    
    
async def 시세_변동(interaction:discord.Interaction, 품목명 : str, 세트가격 : int):
    
    광물 = ["청금석","레드스톤","금","철","구리","다이아","금 원석"]

    농작물 = ["가지","파인애플","홉","토마토","고추","마늘","양배추","배추","포도"]

    물고기 = ["강꼬치고기","개복치","금붕어","농어","다랑어","메기","문어","숭어","연어","잉어","잡어","적색통돔","정어리"]
    
    if "블럭" in 품목명:
        광물명 = 품목명.replace("블럭", "").strip()
        세트가격 = 세트가격/9
        품목명 = 광물명
    
    if 품목명 not in 광물 and 품목명 not in 농작물 and 품목명 not in 물고기:
        await interaction.response.send_message(f"올바르지 않은 품목명입니다.\n입력 값 : __**{품목명}**__",ephemeral=True)
        return 
    
    if 품목명 in 광물 : 

        자원 = "광물"
        

        변동가격 = round(세트가격 / 64,3)


        시세_업데이트(자원,품목명, 변동가격)

        시세 = 시세_불러오기(자원)

        await interaction.response.send_message(f"다음과 같이 시세가 변동되었습니다. {시세.get(품목명)}")
        return
    
    if 품목명 in 농작물 : 

        자원 = "농작물"
        

        변동가격 = round(세트가격 / 64,3)


        시세_업데이트(자원,품목명, 변동가격)

        시세 = 시세_불러오기(자원)

        await interaction.response.send_message(f"다음과 같이 시세가 변동되었습니다. {시세.get(품목명)}")
        return
    
    if 품목명 in 물고기 : 

        자원 = "물고기"
        

        변동가격 = round(세트가격 / 64,3)


        시세_업데이트(자원, 품목명, 변동가격)

        시세 = 시세_불러오기(자원)

        await interaction.response.send_message(f"다음과 같이 시세가 변동되었습니다. {시세.get(품목명)}")
        return