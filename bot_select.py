import discord

class 광부(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="레드스톤", emoji= ":heart:", value="레드스톤"),
            discord.SelectOption(label="청금석",emoji= ":blue_heart:", value="청금석"),
            discord.SelectOption(label="구리",emoji= ":brown_heart:", value="구리"),
            discord.SelectOption(label="철", emoji= ":white_heart:", value="철"),
            discord.SelectOption(label="금", emoji= ":yellow_heart:", value="금"),
            discord.SelectOption(label="다이아",emoji= ":gem:", value="다이아")
        ]
        super().__init__(options=options, placeholder="정산을 요청할 자원을 선택하세요.", max_values=6)

    async def callback(self, interaction: discord.Interaction):
        await self.view.respond_to_answer1(interaction, self.values)

class 농부(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="가지", emoji="<:LOL_TOP:1197071245389336628>", description="Top"),
            discord.SelectOption(label="", emoji="<:LOL_MID:1197071240846921809>", description="Mid"),
            discord.SelectOption(label="정글", emoji="<:LOL_JUNGLE:1197071238296784906>", description="Jungle"),
            discord.SelectOption(label="원딜", emoji="<:LOL_ADC:1197071235255898162>", description="ADC"),
            discord.SelectOption(label="서폿", emoji="<:LOL_SUPPORT:1197071243573215333>", description="Support"),
            discord.SelectOption(label="상관없음", emoji="<:LOL_FILL:1199916524018868265>", description="Fill"),
        ]
        super().__init__(options=options, placeholder="정산 요청할 자원을 선택하세요.", max_values=2)

    async def callback(self, interaction: discord.Interaction):
        await self.view.respond_to_answer2(interaction, self.values)