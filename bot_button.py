import discord
from bot_firebase import 정산요청내역_삭제

    
class 정산버튼(discord.ui.View):
    def __init__(self, 요청자,멤버):
        super().__init__(timeout=None)
        self.요청자 = 요청자
        self.멤버 = 멤버

    @discord.ui.button(label='확인', style=discord.ButtonStyle.primary, custom_id='확인')
    async def 정산완료(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.children[1].disabled = True 
        await interaction.response.edit_message(view=self)

        정산요청내역_삭제(self.요청자)

        await interaction.channel.send(content=f"{self.멤버.mention}님의 정산이 완료되었습니다.")

    @discord.ui.button(label='취소', style=discord.ButtonStyle.danger, custom_id='취소')
    async def 정산취소(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.children[0].disabled = True 
        await interaction.response.edit_message(view=self)

        await interaction.channel.send(content="해당 멤버의 정산이 취소되었습니다.", ephemeral=True)
        