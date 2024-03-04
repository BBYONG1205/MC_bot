import discord
from typing import Literal
from bot_firebase import 멤버정보_저장, 멤버정보_불러오기, 시세_불러오기, 시세_업데이트, 정산요청서_생성,정산총금액_업데이트, 정산요청서_업데이트, 정산요청서_불러오기, 정산요청내역_삭제
from bot_embed import 멤버정보_임베드, 광물시세_임베드, 일반시세_임베드, 정산요청서
from bot_marketprice import 자원시세_계산
from bot_button import 정산버튼
from bot_item import 품목_목록, 축약어
import re
import pyperclip


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

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


#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

async def 정보(interaction: discord.Interaction, 유저:discord.Member):

    기존등록멤버 = 멤버정보_불러오기(유저.id)

    if 기존등록멤버 is None:
        await interaction.response.send_message("등록되지 않은 멤버입니다.", ephemeral=True)
        return


    embed = 멤버정보_임베드 (유저)

    await interaction.response.send_message(embed=embed)
    return

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

async def 복사(interaction: discord.Interaction, 유저:discord.Member):
    기존등록멤버 = 멤버정보_불러오기(유저.id)

    if 기존등록멤버 is None:
        await interaction.response.send_message("등록되지 않은 멤버입니다.", ephemeral=True)
        return
    
    마크아이디 = 기존등록멤버.get("마크 아이디")

    pyperclip.copy(마크아이디)

    await interaction.response.send_message(f"{유저.display_name} 의 마크 아이디가 복사되었습니다.\n```{마크아이디}```", ephemeral=True)
    return

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

async def 정산요청(interaction: discord.Interaction, 요청내역 : str):

    정산요청자 = interaction.user.id
    기존등록멤버 = 멤버정보_불러오기(정산요청자)
    정산요청자_닉네임 = 기존등록멤버.get("닉네임")
    요청자 = f"{정산요청자_닉네임}님의 정산 요청 내역"
    요청서_불러오기=정산요청서_불러오기(요청자)
    
    if 요청서_불러오기 is None:
        요청서생성 = {"요청내역":[], "총 금액" : 0}
        정산요청서_생성(요청자, 요청서생성)


    if 기존등록멤버 is None:
        await interaction.response.send_message("멤버 등록이 되어있지 않아 정산 요청 작업에 실패하였습니다.", ephemeral=True)
        return      

    요청내역 = 요청내역.replace(" ", "").strip()
    품목_세트_리스트 = re.findall(r'([가-힣]+)(\d+)', 요청내역)

    결과_리스트 = []
    금액_합 = 0

    for match in 품목_세트_리스트:
        품목, 세트 = match
        축약어_모음 = 축약어()

        광물, 농작물, 물고기, 기타 = 품목_목록()

        # 입력된 품목명을 축약어로 변환
        품목명 = 축약어_모음.get(품목, 품목)

        # 각 항목에 대한 축약어 적용
        광물 = [축약어_모음.get(item, item) for item in 광물]
        농작물 = [축약어_모음.get(item, item) for item in 농작물]
        물고기 = [축약어_모음.get(item, item) for item in 물고기]
        기타 = [축약어_모음.get(item, item) for item in 기타]

        if 품목명 not in 광물 and 품목명 not in 농작물 and 품목명 not in 물고기 and 품목명 not in 기타:
            await interaction.response.send_message(f"올바르지 않은 품목명입니다.\n입력 값 : __**{품목명}**__",ephemeral=True)
            return
    
        if 품목명 in 광물 :
            자원 = "광물"
        if 품목명 in 농작물 : 
            자원 = "농작물"
        if 품목명 in 물고기 :
            자원 = "물고기"

        _, 한세트_가격,_, _= 자원시세_계산(자원, 품목명)
        금액 = 한세트_가격 *  int(세트)
        결과_리스트.append((품목, int(세트), 금액))
        금액_합 += 금액
        
        요청내역 = 세트, f"{금액}원"
        print(품목, 세트, 금액)
        요청서업데이트 ={"품목명":품목명, "세트":세트, "금액":금액}
        정산요청서_업데이트(요청자, 요청서업데이트)
        
    
    요청금액_합계 = 정산요청서_불러오기(요청자).get("총 금액") + 금액_합
    정산총금액_업데이트(요청자,요청금액_합계)
    print(결과_리스트)
    embed = 정산요청서(정산요청자_닉네임)
        
    await interaction.response.send_message(f"정산 요청이 완료되었습니다.", embed = embed)
    return

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

async def 시세_확인(interaction: discord.Interaction, 품목명: str):

    축약어_모음 = 축약어()
    광물, 농작물, 물고기, 기타 = 품목_목록()

    # 입력된 품목명을 축약어로 변환
    품목명 = 축약어_모음.get(품목명, 품목명)

    # 각 항목에 대한 축약어 적용
    광물 = [축약어_모음.get(item, item) for item in 광물]
    농작물 = [축약어_모음.get(item, item) for item in 농작물]
    물고기 = [축약어_모음.get(item, item) for item in 물고기]
    기타 = [축약어_모음.get(item, item) for item in 기타]

    if 품목명 not in 광물 and 품목명 not in 농작물 and 품목명 not in 물고기 and 품목명 not in 기타:
        await interaction.response.send_message(f"올바르지 않은 품목명입니다.\n입력 값 : __**{품목명}**__", ephemeral=True)
        return
    
    if 품목명 in 광물:
        if 품목명 == "금 원석":
            자원 = "광물"
            개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격 = 자원시세_계산(자원, 품목명)
            embed = 일반시세_임베드(품목명, 개당_가격, 한세트_가격)
        else:
            자원 = "광물"
            개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격 = 자원시세_계산(자원, 품목명)
            embed = 광물시세_임베드(품목명, 개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격)

    if 품목명 in 농작물:
        자원 = "농작물"

    if 품목명 in 물고기:
        자원 = "물고기"

    if 품목명 in 기타:
        자원 = "기타"

    개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격 = 자원시세_계산(자원, 품목명)
    embed = 일반시세_임베드(품목명, 개당_가격, 한세트_가격)
    await interaction.response.send_message(embed=embed)

    
#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

async def 시세_변동(interaction:discord.Interaction, 품목명 : str, 세트가격 : int):
    

    축약어_모음 = 축약어()

    광물, 농작물, 물고기, 기타 = 품목_목록()

    # 입력된 품목명을 축약어로 변환
    품목명 = 축약어_모음.get(품목명, 품목명)

    # 각 항목에 대한 축약어 적용
    광물 = [축약어_모음.get(item, item) for item in 광물]
    농작물 = [축약어_모음.get(item, item) for item in 농작물]
    물고기 = [축약어_모음.get(item, item) for item in 물고기]
    기타 = [축약어_모음.get(item, item) for item in 기타]

    if "블럭" in 품목명:
        광물명 = 품목명.replace("블럭", "").strip()
        세트가격 = 세트가격/9
        품목명 = 광물명
    
    if 품목명 not in 광물 and 품목명 not in 농작물 and 품목명 not in 물고기 and 품목명 not in 기타:
        await interaction.response.send_message(f"올바르지 않은 품목명입니다.\n입력 값 : __**{품목명}**__",ephemeral=True)
        return 
    
    if 품목명 in 광물 : 

        자원 = "광물"

    if 품목명 in 농작물:

        자원 = "농작물"

    if 품목명 in 물고기 :

        자원 = "물고기"
    
    if 품목명 in 기타 : 
        
        자원 = "기타"

    변동가격 = round(세트가격 / 64,3)

    이전시세값 = 시세_불러오기(자원)

    이전시세 = 이전시세값.get(품목명)

    시세_업데이트(자원,품목명, 변동가격)

    시세 = 시세_불러오기(자원)

    변경시세 = 시세.get(품목명)

    await interaction.response.send_message(f"다음과 같이 시세가 변동되었습니다. \n**{이전시세} → {변경시세}**")
    return

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

async def 정산(interaction: discord.Interaction, 멤버 : discord.Member):

    멤버정보 = 멤버정보_불러오기(멤버.id)

    if 멤버정보 is None:
        await interaction.response.send_message("멤버 등록이 되어있지 않은 유저입니다.", ephemeral=True)
        return    
    
    요청자_닉네임 = 멤버정보.get("닉네임")
    요청자 = f"{요청자_닉네임}님의 정산 요청 내역"
    요청내역_확인 =  정산요청서_불러오기(요청자)

    if 요청내역_확인 is None:

        await interaction.response.send_message(f"{요청자_닉네임}님의 미정산 내역이 없습니다.", ephemeral=True)
        return
    
    요청금액_확인 = 정산요청서_불러오기(요청자).get("총 금액")
    오청금액_총합 = "{:,}".format(요청금액_확인)

    embed = discord.Embed(title=f"**{요청자_닉네임}님의 정산 요청 금액** :clipboard:", color=0xffffff)
    embed.add_field(name=f"**총 정산 금액**",value=f"{오청금액_총합}원", inline=False)

    view = 정산버튼(요청자,멤버)

    await interaction.response.send_message(f"{요청자_닉네임}님의 정산 요청 금액을 정산하시겠습니까?", embed = embed, view =view )





