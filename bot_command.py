import discord
from typing import Literal
from bot_firebase import 멤버정보_저장, 멤버정보_불러오기

async def 멤버등록(interaction: discord.Interaction, 유저:discord.Member, 닉네임:str, 직업: Literal["광부", "농부", "어부", "요리사"], 마크아이디: str):
    기존등록멤버 = 멤버정보_불러오기(유저.id)

    if 기존등록멤버:
        await interaction.response.send_message("이미 등록되어있는 멤버입니다.")

    멤버정보 = {"유저":유저.global_name, "닉네임": 닉네임, "직업" : 직업, "마크 아이디": 마크아이디}
    멤버정보_저장(유저.id, 멤버정보)
    
    await interaction.response.send_message("멤버 등록이 완료되었습니다.", ephemeral=True)
