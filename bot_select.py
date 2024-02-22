import discord

class 광부(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="레드스톤", emoji= ":heart:", value="레드스톤"),
            discord.SelectOption(label="청금석",emoji= ":blue_heart:", value="청금석"),
            discord.SelectOption(label="구리",emoji= ":brown_heart:", value="구리"),
            discord.SelectOption(label="철", emoji= ":white_heart:", value="철"),
            discord.SelectOption(label="금", emoji= ":yellow_heart:", value="금"),
            discord.SelectOption(label="금 원석", emoji= ":yellow_heart:", value="금 원석"),
            discord.SelectOption(label="다이아",emoji= ":gem:", value="다이아")
        ]
        super().__init__(options=options, placeholder="정산을 요청할 자원을 선택하세요.", max_values=7)

    async def callback(self, interaction: discord.Interaction):
        await self.view.respond_to_answer1(interaction, self.values)

class 농부(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="가지", emoji= ":heart:", value="가지"),
            discord.SelectOption(label="파인애플",emoji= ":blue_heart:", value="파인애플"),
            discord.SelectOption(label="양배추",emoji= ":brown_heart:", value="양배추"),
            discord.SelectOption(label="배추", emoji= ":white_heart:", value="배추"),
            discord.SelectOption(label="마늘", emoji= ":yellow_heart:", value="마늘"),
            discord.SelectOption(label="포도",emoji= ":gem:", value="포도"),
            discord.SelectOption(label="고추",emoji= ":gem:", value="고추"),
            discord.SelectOption(label="옥수수",emoji= ":gem:", value="옥수수"),
            discord.SelectOption(label="",emoji= ":gem:", value="옥수수"),            

        ]
        super().__init__(options=options, placeholder="정산 요청할 자원을 선택하세요.", max_values=2)

    async def callback(self, interaction: discord.Interaction):
        await self.view.respond_to_answer2(interaction, self.values)