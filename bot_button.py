import discord
from bot_firebase import 정산요청내역_삭제, 정산요청서_업데이트, 정산총금액_업데이트, 정산요청서_불러오기
from bot_embed import 정산요청내역
    
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



class 정산요청확정(discord.ui.View):
    def __init__(self, 요청자,품목명_리스트, 세트_리스트, 금액_리스트, 금액_합):
        super().__init__(timeout=None)
        self.요청자 = 요청자
        self.품목명_리스트 = 품목명_리스트
        self.세트_리스트 = 세트_리스트
        self.금액_리스트 = 금액_리스트
        self.금액_합 = 금액_합

    @discord.ui.button(label='요청', style=discord.ButtonStyle.primary, custom_id='정산요청')
    async def 정산요청(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.children[1].disabled = True
        for i in range(len(self.품목명_리스트)):
            data = {
                "품목명": self.품목명_리스트[i],
                "세트": self.세트_리스트[i],
                "금액": self.금액_리스트[i]
                        }
            요청서업데이트 = data
            정산요청서_업데이트(self.요청자, 요청서업데이트)


        요청금액합계 = 정산요청서_불러오기(self.요청자).get("총 금액") + self.금액_합
        정산총금액_업데이트(self.요청자,요청금액합계)
        embed = 정산요청내역(self.요청자)
        await interaction.response.edit_message(content="요청이 완료되었습니다.", embed = embed ,view =self)


    @discord.ui.button(label='취소', style=discord.ButtonStyle.danger, custom_id='정산요청취소')
    async def 취소(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.children[0].disabled = True
        await interaction.response.edit_message(content="요청이 취소되었습니다.", view =self)  # 새로운 메시지 발송


#
        
class 뿅정산(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='정산하기', style=discord.ButtonStyle.primary, custom_id='뿅정산')
    async def 뵹뵹이정산(self, interaction: discord.Interaction, button: discord.ui.Button):
        요청자 = "뵹뵹이님의 정산 요청 내역"
        요청서_불러오기=정산요청서_불러오기(요청자)
        if 요청서_불러오기 is None :
            await interaction.response.send_message("요청된 정산 내역이 없습니다.",ephemeral=True)
            return
        정산요청내역_삭제(요청자)

        await interaction.response.send_message(content="뵹뵹이님의 정산이 완료되었습니다.")