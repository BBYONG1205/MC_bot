import discord
from discord import app_commands 
from typing import Literal
from bot_command import 멤버등록, 정보, 복사, 시세_확인,시세_변동, 정산요청, 정산, 정산요청내역확인, 멤버요청내역확인
from bot_guide import guide
from bot_embed import 시세표
from bot_event import 간편정산, 신규업데이트
from bot_button import 뿅정산
from bot_ticket import ticket_launcher

f = open('token.txt', 'r')
token = f.readline().strip()

class aclient(discord.Client):
    def __init__(self):
        super().__init__(intents = discord.Intents.all())
        self.synced = False
        self.added = False
        self.bbyong = False


    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: 
            await tree.sync() 
            self.synced = True

        if not self.added :
            self.add_view(ticket_launcher())
            self.added = True

        if not self.bbyong :
            self.add_view(뿅정산())
            self.bbyong = True
    



        print(f'{self.user}이 시작되었습니다')
        game = discord.Game('정산') 
        await self.change_presence(status=discord.Status.online, activity=game)


client = aclient()
client.intents.messages = True
client.intents.message_content = True
client.intents.members = True
tree = app_commands.CommandTree(client)

@client.event
async def on_message(message):
    await 간편정산(client,message)
    await 신규업데이트(client,message)


@tree.command(name ='등록', description='기린 서버를 함께하는 멤버 등록을 진행합니다.') 
async def register_member(interaction: discord.Interaction, 유저:discord.Member, 닉네임:str, 직업: Literal["광부", "농부", "어부", "요리사"], 마크아이디: str):
    await 멤버등록(interaction, 유저, 닉네임, 직업, 마크아이디)

#@tree.command(name ='정보', description='등록된 멤버의 정보를 확인합니다.')
#async def member_info(interaction: discord.Interaction, 유저:discord.Member):
#    await 정보(interaction, 유저)

#@tree.command(name ='복사', description='등록된 멤버의 마크 아이디를 복사합니다.')
#async def member_info(interaction: discord.Interaction, 유저:discord.Member):
#    await 복사(interaction, 유저)

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
async def guide_command(interaction:discord.Interaction):

    embed = guide()

    await interaction.response.send_message(embed=embed)

@tree.command(name='티켓생성', description='정산 전용 티켓을 생성합니다.')
async def ticketing(interaction:discord.Interaction):
    embed = discord.Embed(title="하단의 버튼을 눌러 정산 기능을 이용해보세요!", color=0xffffff)
    embed.add_field(name="**- 개인의 정산 전용 채널이 생성됩니다.**",value="",inline=False)
    embed.add_field(name="**- 정산이 완료되면 채널을 삭제할 수 있습니다.**",value="",inline=False)
    await interaction.channel.send(embed=embed, view=ticket_launcher())
    await interaction.response.send_message("정산 전용 티켓 생성이 완료되었습니다.", ephemeral=True)


@tree.command(name='시세표', description='기린 서버의 자원들에 대한 시세표입니다.')
async def marketprice(interaction:discord.Interaction):
    embed= 시세표()
    await interaction.response.send_message(embed=embed)

@tree.command(name='내요청내역',description= '현재까지 요청된 내역을 확인합니다.')
async def settlement_list(interaction:discord.Interaction):
    await 정산요청내역확인(interaction)

@tree.command(name='멤버요청내역', description= '등록된 멤버의 요청 내역을 확인합니다.')
async def member_settlement_list (interaction:discord.Interaction, 멤버 : discord.Member):
    await 멤버요청내역확인(interaction,멤버)

@tree.command(name='뿅뿅정산설치', description='뿅망치 살인마님 전용 정산 버튼을 설치합니다..')
async def test(interaction:discord.Interaction):
    view = 뿅정산()
    await interaction.response.send_message("뵹뵹이님의 요청 내역을 정산하시겠습니까?", view = view)

client.run(token)