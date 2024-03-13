from bot_firebase import 정산요청내역_삭제
from bot_button import 뿅정산, 퀸정산,머부정산
from bot_embed import 정산_embed 
import asyncio


        

async def 뵹뵹업데이트(client, message):

    TARGET_CHANNEL_ID = 1215170600675577887

    if message.channel.id != TARGET_CHANNEL_ID:
        return


    if  message.content.startswith('뵹뵹이님의 요청 내역을 정산하시겠습니까?'):
        return 
    
    async for old_message in message.channel.history():
                
        if message.content.startswith ('요청된 정산 내역이 없습니다.'):
                return
        
        if message.content.startswith('요청된 내역은 다음과 같습니다.'):
                return
        
        if old_message.author == client.user and old_message.content.startswith('뵹뵹이님의 요청 내역을 정산하시겠습니까?'):
            멤버_id = 370364396058181635
            멤버 = await client.fetch_user(멤버_id)
            요청자 = "뵹뵹이님의 정산 요청 내역"
            프사 = 멤버.avatar.url
            view = 뿅정산()
            embed = 정산_embed(요청자, 프사)
            await asyncio.gather(
                old_message.delete(),
                message.channel.send("뵹뵹이님의 요청 내역을 정산하시겠습니까?", embed=embed, view=view)
            )
            return

  

async def 지노업데이트(client, message):

    TARGET_CHANNEL_ID = 1215305636653568081

    if message.channel.id != TARGET_CHANNEL_ID:
        return
    
    if message.content.startswith('퀸지노님의 요청 내역을 정산하시겠습니까?'):
        return
    
    async for old_message in message.channel.history():
                
        if message.content.startswith ('요청된 정산 내역이 없습니다.'):
                return
        if message.content.startswith('요청된 내역은 다음과 같습니다.'):
                return
                                        
        if old_message.author == client.user and old_message.content.startswith('퀸지노님의 요청 내역을 정산하시겠습니까?'):
            view = 퀸정산()
            멤버_id = 392328984014225418
            멤버 = await client.fetch_user(멤버_id)
            프사 = 멤버.avatar.url
            요청자 = "지노퀸님의 정산 요청 내역"
            embed = 정산_embed(요청자,프사)
            await asyncio.gather(
                old_message.delete(),
                message.channel.send("퀸지노님의 요청 내역을 정산하시겠습니까?", embed=embed, view=view)
            )
            return

async def 머부업데이트(client, message):

    TARGET_CHANNEL_ID = 1215881784042983475

    if message.channel.id != TARGET_CHANNEL_ID:
        return
    
    if message.content.startswith('김머부님의 요청 내역을 정산하시겠습니까?'):
        return
    
    async for old_message in message.channel.history():
                
        if message.content.startswith ('요청된 정산 내역이 없습니다.'):
            return
        
        if message.content.startswith('요청된 내역은 다음과 같습니다.'):
            return
        
        if old_message.author == client.user and old_message.content.startswith('김머부님의 요청 내역을 정산하시겠습니까?'):

            view = 머부정산()
            멤버_id = 484314457313509376
            멤버 = await client.fetch_user(멤버_id)
            프사 = "https://i.ibb.co/L9V6Zyq/image.webp"
            요청자 = "김머부님의 정산 요청 내역"
            embed = 정산_embed(요청자,프사)
            await asyncio.gather(
                old_message.delete(),
                message.channel.send("김머부님의 요청 내역을 정산하시겠습니까?", embed=embed, view=view)
            )
            return