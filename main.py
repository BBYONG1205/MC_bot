import discord
from discord import app_commands 
from typing import Literal
from bot_command import 멤버등록, 정보, 복사


f = open('token.txt', 'r')
token = f.readline().strip()

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.default())
        self.synced = False

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True
        print(f'{self.user}이 시작되었습니다')
        game = discord.Game('정산') 
        await self.change_presence(status=discord.Status.online, activity=game)


client = aclient()
tree = app_commands.CommandTree(client)


@tree.command(name ='등록', description='기린 서버를 함께하는 멤버 등록을 진행합니다.') 
async def register_member(interaction: discord.Interaction, 유저:discord.Member, 닉네임:str, 직업: Literal["광부", "농부", "어부", "요리사"], 마크아이디: str):
    await 멤버등록(interaction, 유저, 닉네임, 직업, 마크아이디)

@tree.command(name ='정보', description='등록된 멤버의 정보를 확인합니다.')
async def member_info(interaction: discord.Interaction, 유저:discord.Member):
    await 정보(interaction, 유저)

@tree.command(name ='복사', description='등록된 멤버의 마크 아이디를 복사합니다.')
async def member_info(interaction: discord.Interaction, 유저:discord.Member):
    await 복사(interaction, 유저)



client.run(token)