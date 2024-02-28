import discord
from discord import app_commands 
from typing import Literal
from bot_command import 멤버등록, 정보, 복사, 시세_확인,시세_변동, 정산요청, 정산


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

@tree.command(name='시세', description='자원의 시세를 검색합니다.')
async def market_price(interaction: discord.Interaction, 품목명 : str):
    await 시세_확인(interaction, 품목명)

@tree.command(name='시세변동', description='변동된 시세를 반영합니다.')
async def mp_update(interaction:discord.Interaction, 품목명 : str, 세트가격 : int):
    await 시세_변동(interaction, 품목명, 세트가격)

@tree.command(name='정산요청', description='수집한 자원에 대해 정산 요청을 전송합니다.')
async def update_settlement(interaction:discord.Interaction, 요청내역 : str):
    await 정산요청(interaction, 요청내역)

@tree.command(name='정산하기', description='선택한 멤버의 정산 요청 금액을 정산합니다.')
async def complete_settlement(interaction:discord.Interaction, 멤버 : discord.Member):
    await 정산(interaction, 멤버)

@tree.command(name='사용가이드', description='뿅뿅 정산봇 사용 가이드입니다.')
async def guide(interaction:discord.Interaction):

    embed = discord.Embed(title="**정산봇 사용 가이드**", color=0xffffff)
    embed.add_field(name="🔔 __**등록(최초 1회)**__",value = "\n등록 명령어를 통해 멤버 등록을 진행합니다. \n\n /등록 `유저`@뿅망치살인마 `닉네임` 뿅살 `직업` 농부 `마크아이디` BBYONG_",inline=False)
    embed.add_field(name="🔔 __**정산요청**__", value = "\n정산 요청서를 생성하여 정산이 필요한 내역들을 취합합니다.\n\n/정산요청 `품목명`레드스톤 or 레드스톤 블럭 `세트` 3 `나머지` 22 \n\n> 레드스톤 3세트 22개 정산 요청 완료!",inline=False)
    embed.add_field(name="🔔 __**정산하기**__",value = "\n사용자가 입력해둔 정산 요청에 대해 정산을 진행합니다.\n\n/정산하기 `유저`@뿅망치살인마\n\n뿅망치살인마님이 입력해둔 정산 요청 금액을 확인합니다.\n\n확인 버튼을 누를 시 저장되어있던 정산 요청 내역이 삭제됩니다.")
    embed.add_field(name="🤍 **시세**", value = "\n입력한 품목의 시세를 조회합니다. \n\n/시세 `품목명` 금 \n\n> 금의 개당 가격, 세트 가격, 블럭 가격, 블럭 세트 가격 등 조회 가능",inline=False)
    embed.add_field(name="🤍 **시세변동**",value = "\n원하는 품목의 시세를 조정합니다. \n\n/시세변동 `품목명` 레드스톤 `세트가격` 890",inline=False)
    embed.add_field(name="🤍 **복사**",value = "\n선택한 유저의 마크아이디를 복사합니다. \n\n/복사 `유저` @뿅망치살인마",inline=False)

    await interaction.response.send_message(embed=embed)



client.run(token)