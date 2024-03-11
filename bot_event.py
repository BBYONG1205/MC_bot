from bot_firebase import 정산요청내역_삭제
from bot_button import 뿅정산

async def 간편정산(client, message):
    if message.author == client.user:
        return  
    
    if message.content.startswith('.'):

        if "뵹" in message.content or "뿅" in message.content:
            요청자 = "뵹뵹이님의 정산 요청 내역"
            정산요청내역_삭제(요청자)
            await message.channel.send("뵹뵹이님의 정산이 완료되었습니다.")
            return

        if "머" in message.content:
            요청자 = "김머부님의 정산 요청 내역"
            정산요청내역_삭제(요청자)
            await message.channel.send("김머부님의 정산이 완료되었습니다.")
            return
        
        if "퀸" in message.content:
            요청자 = "지노퀸님의 정산 요청 내역" 
            정산요청내역_삭제(요청자)
            await message.channel.send("퀸지노님의 정산이 완료되었습니다.")
            return
        

async def 신규업데이트(client, message):
    if not message.content.startswith('뵹뵹이님의 요청 내역을 정산하시겠습니까?'):
        async for old_message in message.channel.history():
                if old_message.author == client.user and old_message.content.startswith('뵹뵹이님의 요청 내역을 정산하시겠습니까?'):
                    await old_message.delete()
                    view = 뿅정산()
                    await message.channel.send("뵹뵹이님의 요청 내역을 정산하시겠습니까?",view=view)
                    return

