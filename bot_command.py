import discord
from typing import Literal
from bot_firebase import 멤버정보_저장, 멤버정보_불러오기
from bot_embed import 멤버정보_임베드
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