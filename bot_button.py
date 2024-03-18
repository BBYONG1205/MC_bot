import discord
from bot_firebase import 정산요청내역_삭제, 정산요청서_업데이트, 정산요청서_생성, 정산총금액_업데이트, 정산요청서_불러오기, 정산요청상세_불러오기
from bot_embed import 정산요청내역, 정산_embed
    
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
    def __init__(self, 요청자, 품목명_리스트, 세트_리스트, 셜커_리스트, 금액_리스트, 금액_합):
        super().__init__(timeout=None)
        self.요청자 = 요청자
        self.신규_품목명_리스트 = 품목명_리스트
        self.신규_세트_리스트 = 세트_리스트
        self.신규_셜커_리스트 = 셜커_리스트
        self.신규_금액_리스트 = 금액_리스트
        self.금액_합 = 금액_합

    @discord.ui.button(label='요청', style=discord.ButtonStyle.primary, custom_id='정산요청')
    async def 정산요청(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.children[1].disabled = True

        품목명_리스트, 금액_리스트, 세트_리스트, 셜커_리스트 = 정산요청상세_불러오기(self.요청자)
        기존요청금액 = 정산요청서_불러오기(self.요청자).get("총 금액")

        # 기존 요청내역 삭제
        정산요청내역_삭제(self.요청자)
        
        # 새로운 요청서 생성
        요청서생성 = {"요청내역": [], "총 금액": 0}
        정산요청서_생성(self.요청자, 요청서생성)

        # 기존에 입력된 품목과 비교하여 업데이트
        for index, 품목 in enumerate(품목명_리스트):
            if 품목 in self.신규_품목명_리스트:
                # 같은 품목이 있다면 해당 품목의 인덱스를 가져옴
                idx = self.신규_품목명_리스트.index(품목)
                # 세트값과 금액을 업데이트
                세트_리스트[index] += self.신규_세트_리스트[idx]
                셜커_리스트[index] += self.신규_셜커_리스트[idx]
                금액_리스트[index] += self.신규_금액_리스트[idx]

        # 새로운 품목 추가
        for i in range(len(self.신규_품목명_리스트)):
            if self.신규_품목명_리스트[i] not in 품목명_리스트:
                품목명_리스트.append(self.신규_품목명_리스트[i])
                세트_리스트.append(self.신규_세트_리스트[i])
                셜커_리스트.append(self.신규_셜커_리스트[i])
                금액_리스트.append(self.신규_금액_리스트[i])

        # 업데이트된 값을 사용하여 요청서를 업데이트
        for i in range(len(품목명_리스트)):
            data = {
                "품목명": 품목명_리스트[i],
                "세트": 세트_리스트[i],
                "셜커": 셜커_리스트[i],
                "금액": 금액_리스트[i]
            }
            요청서업데이트 = data
            정산요청서_업데이트(self.요청자, 요청서업데이트)

        # 요청금액 합계 업데이트
        요청금액합계 = 기존요청금액 + self.금액_합
        정산총금액_업데이트(self.요청자, 요청금액합계)

        # 업데이트된 내용을 보여주기 위해 새로운 요청내역 생성
        embed = 정산요청내역(self.요청자)
        await interaction.response.edit_message(embed=embed, view=self)
        await interaction.channel.send(content="요청이 완료되었습니다.")



    @discord.ui.button(label='취소', style=discord.ButtonStyle.danger, custom_id='정산요청취소')
    async def 취소(self, interaction: discord.Interaction, button: discord.ui.Button):
        button.disabled = True
        self.children[0].disabled = True
        await interaction.response.edit_message(view =self)
        await interaction.channel.send(content="요청이 취소되었습니다.", )  # 새로운 메시지 발송


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

        await interaction.channel.send(content="뵹뵹이님의 정산이 완료되었습니다.")

class 퀸정산(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='정산하기', style=discord.ButtonStyle.primary, custom_id='퀸정산')
    async def 퀸지노정산(self, interaction: discord.Interaction, button: discord.ui.Button):
        요청자 = "지노퀸님의 정산 요청 내역"
        요청서_불러오기=정산요청서_불러오기(요청자)
        if 요청서_불러오기 is None :
            await interaction.response.send_message("요청된 정산 내역이 없습니다.",ephemeral=True)
            return
        정산요청내역_삭제(요청자)

        await interaction.channel.send(content="퀸지노님의 정산이 완료되었습니다.")

class 머부정산(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(label='정산하기', style=discord.ButtonStyle.primary, custom_id='머부정산')
    async def 김머부정산(self, interaction: discord.Interaction, button: discord.ui.Button):
        요청자 = "김머부님의 정산 요청 내역"
        요청서_불러오기=정산요청서_불러오기(요청자)
        if 요청서_불러오기 is None :
            await interaction.response.send_message("요청된 정산 내역이 없습니다.",ephemeral=True)
            return
        정산요청내역_삭제(요청자)

        await interaction.channel.send(content="김머부님의 정산이 완료되었습니다.")