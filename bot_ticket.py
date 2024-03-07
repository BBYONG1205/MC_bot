import discord
from bot_embed import 시세표,티켓설명

class ticket_launcher(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="정산요청📃", style=discord.ButtonStyle.primary, custom_id="정산_요청")
    async def ticket(self, interaction: discord.Interaction, button: discord.ui.Button):
        # 채널 찾기
        ticket_name = f"{interaction.user.display_name}님의-정산-요청"
        ticket_channel = discord.utils.get(interaction.guild.channels, name=ticket_name)
        category_name = "⛏ MINECRAFT 정산"
        category_channel = discord.utils.get(interaction.guild.categories, name=category_name)
        if category_channel is None:
            category_overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=True),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
            }
            category_channel = await interaction.guild.create_category(name= category_name, overwrites=category_overwrites)

        if ticket_channel is not None:
            await interaction.response.send_message(f"이미 존재하는 정산 요청 채널이 있습니다. {ticket_channel.mention}", ephemeral=True)

        else:

            overwrites = {
                interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
                interaction.user: discord.PermissionOverwrite(view_channel=True, send_messages=True, attach_files=True, embed_links=True, read_message_history=True),
                interaction.guild.me: discord.PermissionOverwrite(view_channel=True, send_messages=True, read_message_history=True)
            }
            channel = await category_channel.create_text_channel(
                name=ticket_name,
                overwrites=overwrites,
                reason=f"{interaction.user.display_name}님의 정산 요청📃"
            )
            await interaction.response.send_message(f"정산 요청 채널이 생성되었습니다! {channel.mention}", ephemeral=True)
            embed = 시세표()
            embed2 = 티켓설명()
            await channel.send ("## 정산 요청 채널에 오신 것을 환영합니다!" ,embed= embed2)
            await channel.send ("### 아래의 시세표을 참고하여 정산을 요청해보세요!",embed = embed)





class close_button(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="정산완료✅", style=discord.ButtonStyle.secondary, custom_id="정산_완료")
    async def done(self, interaction: discord.Interaction, button: discord.ui.Button):
        commit_button=yes_or_no()
        await interaction.response.send_message("정산을 완료하시겠습니까? 확인 버튼을 클릭 시 채널이 닫힙니다.",view=commit_button)

class yes_or_no(discord.ui.View):
    def __init__(self) -> None:
        super().__init__(timeout=None)

    @discord.ui.button(label="확인", style=discord.ButtonStyle.success, custom_id="정산_확인")
    async def commit(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.delete()
        await interaction.response.send_message("정산이 완료되었습니다.")

    @discord.ui.button(label="취소", style=discord.ButtonStyle.danger, custom_id="정산_취소")
    async def cancel(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.response.send_message("취소되었습니다", ephemeral=True)

