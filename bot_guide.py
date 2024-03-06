import discord

def guide():

    embed = discord.Embed(title="**정산봇 사용 가이드**", color=0xffffff)
    embed.add_field(name="🔔 __**등록(최초 1회)**__",value = "\n등록 명령어를 통해 멤버 등록을 진행합니다. \n\n /등록 `유저`@뿅망치살인마 `닉네임` 뿅살 `직업` 농부 `마크아이디` BBYONG_\n",inline=False)
    embed.add_field(name="🔔 __**정산요청**__", value = "\n정산 요청서를 생성하여 정산이 필요한 내역들을 취합합니다.\n\n/정산요청 `요청내역` 마2 \n\n> 마늘 2세트 정산 요청 완료! \n 아이템 이름의 앞글자, 초성, 영타 등으로 입력해도 정상 입력됩니다.\n `마늘` `마` `ㅁㄴ` `aksmf` 등\n",inline=False)
    embed.add_field(name="🔔 __**정산하기**__",value = "\n사용자가 입력해둔 정산 요청에 대해 정산을 진행합니다.\n\n/정산하기 `유저`@뿅망치살인마\n\n뿅망치살인마님이 입력해둔 정산 요청 금액을 확인합니다.\n\n확인 버튼을 누를 시 저장되어있던 정산 요청 내역이 삭제됩니다.\n",inline=False)
    embed.add_field(name="🤍 **시세**", value = "\n입력한 품목의 시세를 조회합니다. \n\n/시세 `품목명` 금 \n\n> 금의 개당 가격, 세트 가격, 블럭 가격, 블럭 세트 가격 등 조회 가능\n",inline=False)
    embed.add_field(name="🤍 **시세변동**",value = "\n원하는 품목의 시세를 조정합니다. \n\n/시세변동 `품목명` 레드스톤 `세트가격` 890\n",inline=False)
    embed.add_field(name="🤍 **복사**",value = "\n선택한 유저의 마크아이디를 복사합니다. \n\n/복사 `유저` @뿅망치살인마\n",inline=False)

    return embed