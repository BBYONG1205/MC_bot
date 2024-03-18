import discord
from bot_firebase import 멤버정보_불러오기, 정산요청서_불러오기, 정산요청상세_불러오기
from bot_marketprice import 자원시세_계산

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def 멤버정보_임베드(유저):
    
    기존등록멤버=멤버정보_불러오기(유저.id)
    닉네임 = 기존등록멤버.get("닉네임")
    직업 = 기존등록멤버.get("직업")
    마크아이디 = 기존등록멤버.get("마크 아이디")   

    if 기존등록멤버:
        embed = discord.Embed(title=f"{닉네임}님의 정보 :identification_card:", color=0xffffff)

        if 직업 == "광부":
            embed.add_field(name=f"**직업**  `{직업}` :pick:",value="", inline=False)

        elif 직업 == "농부":
            embed.add_field(name=f"**직업**  `{직업}` :farmer:",value="", inline=False)
        
        elif 직업 == "어부":
            embed.add_field(name=f"**직업** `{직업}` :fishing_pole_and_fish:",value="", inline=False)

        elif 직업 == "요리사":
            embed.add_field(name=f"**직업**  `{직업}` :cook:",value="", inline=False)


        embed.add_field(name=f"**마크 아이디**  `{마크아이디}`", value="", inline=False)
        if 유저.avatar:      
            embed.set_thumbnail(url=유저.avatar.url)
        else:  
            embed.set_thumbnail(url="https://i.ibb.co/Vm2Gx5w/image.jpg")
     
    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def 광물시세_임베드(품목명, 개당_가격, 한세트_가격,한블럭_가격,블럭세트_가격):

    embed = discord.Embed(title=f"{품목명} 시세 💰", color=0xffffff)
    embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
    embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)
    embed.add_field(name=f"**1 블럭** `{한블럭_가격}원`",value="", inline=False)
    embed.add_field(name=f"**블럭 1 세트** `{블럭세트_가격}원`",value="", inline=False)
    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#광물 제외 품목들의 시세 임베드 (광물의 경우 블럭단위가 있어서 제외함)

def 일반시세_임베드(품목명, 개당_가격, 한세트_가격):

    embed = discord.Embed(title=f"{품목명} 시세 💰", color=0xffffff)
    embed.add_field(name=f"**개당** `{개당_가격}원`", value = "", inline=False)
    embed.add_field(name=f"**1 세트** `{한세트_가격}원`",value="", inline=False)
    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#정산 요청 입력시 출력되는 임시 임베드


def 정산요청서(정산요청자_닉네임, 품목명_리스트, 세트_리스트, 셜커_리스트, 금액_리스트, 금액_합):
    
    이모지 = {
        "고추": ':hot_pepper:',
        "가지": ':eggplant:',
        "마늘": ':garlic:',
        "파인애플" : ':pineapple:',
        "포도" : ':grapes:',
        "토마토":':tomato:',
        "홉" : ':olive:',
        "배추" : ':leafy_green:',
        "양배추" : ':green_circle:',
        "옥수수" : ':corn:',
        "생고기" : ':pig:',
        "조미료" : ':salt:'
    }        
        
    표기_리스트 = []

    for 숫자, 셜커 in zip(세트_리스트, 셜커_리스트):

        합계 = 숫자 - (셜커*27)

        if 합계 > 0 and 셜커 == 0 :
            표기_리스트.append(f'{숫자}셋')

        elif 합계  ==  0 and 셜커 > 0:
            표기_리스트.append(f'{셜커}셜')

        elif 합계 > 0 and 셜커 > 0 :
            표기_리스트.append(f'{셜커}셜 {합계}셋')

    품목명_필드 = "\n".join([f"{이모지.get(품목명)}{품목명}" for 품목명 in 품목명_리스트])
    금액_필드 = "\n".join([f"{format(금액,",")}원" for 금액 in 금액_리스트])
    표기_필드 = "\n".join([f"{표기}" for 표기 in 표기_리스트])

    총금액 = "{:,}".format(금액_합)
    embed = discord.Embed(title=f"**{정산요청자_닉네임}님의 정산 요청 내역** :clipboard:", description="===========================", color=0xffffff)

    embed.add_field(name="**품목명**",value=f"{품목명_필드}", inline=True)
    embed.add_field(name="**수량**",value=f"{표기_필드}", inline=True)
    embed.add_field(name="**금액**",value=f"{금액_필드}", inline=True)
    embed.add_field(name="",value="===========================", inline=False)
    embed.add_field(name=f"**총 금액** `{총금액}원`",value="", inline=True)

    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#정산 확인 버튼 클릭 시 출력되는 최종 임베드


def 정산요청내역(요청자):

    이모지 = {
        "고추": ':hot_pepper:',
        "가지": ':eggplant:',
        "마늘": ':garlic:',
        "파인애플" : ':pineapple:',
        "포도" : ':grapes:',
        "토마토":':tomato:',
        "홉" : ':olive:',
        "배추" : ':leafy_green:',
        "양배추" : ':green_circle:',
        "옥수수" : ':corn:',
        "생고기" : ':pig:',
        "조미료" : ':salt:'
    }        
    
    총금액 = 정산요청서_불러오기(요청자).get("총 금액")
    품목명_리스트, 금액_리스트 , 세트_리스트, 셜커_리스트 = 정산요청상세_불러오기(요청자)

    
    표기_리스트 = []

    for 숫자, 셜커 in zip(세트_리스트, 셜커_리스트):

        합계 = 숫자 - (셜커*27)

        if 합계 > 0 and 셜커 == 0 :
            표기_리스트.append(f'{숫자}셋')

        elif 합계  ==  0 and 셜커 > 0:
            표기_리스트.append(f'{셜커}셜')

        elif 합계 > 0 and 셜커 > 0 :
            표기_리스트.append(f'{셜커}셜 {합계}셋')

        
        
    품목명_필드 = "\n".join([f"{이모지.get(품목명)}{품목명}" for 품목명 in 품목명_리스트])
    금액_필드 = "\n".join([f"{format(금액,",")}원" for 금액 in 금액_리스트])
    표기_필드 = "\n".join([f"{표기}" for 표기 in 표기_리스트])

    총금액 = "{:,}".format(총금액)
    embed = discord.Embed(title=f"**{요청자}** :clipboard:", description="===========================", color=0xffffff)

    embed.add_field(name="**품목명**",value=f"{품목명_필드}", inline=True)
    embed.add_field(name="**수량**",value=f"{표기_필드}", inline=True)
    embed.add_field(name="**금액**",value=f"{금액_필드}", inline=True)
    embed.add_field(name="",value="===========================", inline=False)
    embed.add_field(name=f"**총 금액** `{총금액}원`",value="", inline=True)

    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def 티켓설명():
    embed = discord.Embed(title="**정산봇 사용 가이드**", description="", color=0xffffff)
    embed.add_field(name="**정산요청**",value="- 모든 자원은 자원의 첫 번째 글자, 초성, 영타 등으로 입력 가능합니다.\n\n예시)토1홉1포1\n\n- 셜커 혹은 블럭 단위로 입력을 원하는 경우 셜커는 '셜', 블럭은 '블' 이라고 자원명 뒤에 붙여주세요.\n\n예시)토셜1금블1", inline=False)
    embed.add_field(name="**주의사항**", value="- 자원명과 숫자는 반드시 분리되어야 합니다.\n\n예시)토마토11홉\n→ 토마토 1세트 홉1세트가 아닌 토마토11세트로 입력됨",inline=False)
    #embed.set_footer(text="정산이 끝난 경우 하단의 정산 완료 버튼을 통해 티켓을 닫을 수 있습니다.")
    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ
#농부 전용 시세표

def 시세표():
    def 가격_가져오기(자원, 품목들):
        개당가격_리스트 = []
        한세트가격_리스트 = []
        이모지 = {
        "고추": ':hot_pepper:',
        "가지": ':eggplant:',
        "마늘": ':garlic:',
        "파인애플" : ':pineapple:',
        "포도" : ':grapes:',
        "토마토":':tomato:',
        "홉" : ':olive:',
        "배추" : ':leafy_green:',
        "양배추" : ':green_circle:',
        "옥수수" : ':corn:',
        "생고기" : ':pig:',
        "조미료" : ':salt:',
        "닭고기" : ':chicken:'
        }        

        for 품목명 in 품목들:
            개당_가격, 한세트_가격, _, _ = 자원시세_계산(자원, 품목명)
            개당가격_리스트.append(개당_가격)
            한세트가격_리스트.append(한세트_가격)

        품목명_필드 = "\n".join(f"{이모지.get(품목명)} {품목명}" for 품목명 in 품목들)
        개당가격_필드 = "\n".join([f"{가격}원" for 가격 in 개당가격_리스트])
        세트가격_필드 = "\n".join([f"{format(가격, ',')}원" for 가격 in 한세트가격_리스트])

        return 품목명_필드, 개당가격_필드, 세트가격_필드

    농작물 = ["토마토","가지","포도", "마늘", "홉", "고추", "옥수수", "배추", "파인애플", "양배추"]
    기타 = [ "닭고기","조미료", "생고기"]

    농작물_품목, 농작물_개당가격, 농작물_세트가격 = 가격_가져오기("농작물", 농작물)
    기타_품목, 기타_개당가격, 기타_세트가격 = 가격_가져오기("기타", 기타)

    embed = discord.Embed(title="", description="", color=0xffffff)

    embed.add_field(name="**품목명**", value=f"{농작물_품목}\n{기타_품목}", inline=True)
    embed.add_field(name="**1셋**", value=f"{농작물_세트가격}\n{기타_세트가격}", inline=True)
    embed.add_field(name="**1개**", value=f"{농작물_개당가격}\n{기타_개당가격}", inline=True)

    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def 정산_embed (요청자,프사):
    요청서_확인 = 정산요청서_불러오기(요청자)

    if 요청서_확인 is None :
        요청금액_확인 = int(0)
    
    else:
        요청금액_확인 = 정산요청서_불러오기(요청자).get("총 금액")
    
    요청금액_총합 = "{:,}".format(요청금액_확인)

    embed = discord.Embed(title=f"**{요청자}** :clipboard:", color=0xffffff)
 
    embed.set_thumbnail(url=프사)

    embed.add_field(name=f"**총 정산 금액**",value=f"{요청금액_총합}원", inline=False)

    return embed

#ㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡㅡ

def 계산요청서(계산요청자, 품목명_리스트, 세트_리스트, 금액_리스트,금액_합):

        
    요청자 = f"{계산요청자}님의 계산 요청 내역"
    
    품목명_필드 = "\n".join([f"{품목명}" for 품목명 in 품목명_리스트])
    금액_필드 = "\n".join([f"{금액}원" for 금액 in 금액_리스트])
    세트_필드 = "\n".join([f"{세트}세트" for 세트 in 세트_리스트])

    총금액 = "{:,}".format(금액_합)
    embed = discord.Embed(title=f"**{요청자}** :clipboard:", description="===========================", color=0xffffff)

    embed.add_field(name="**품목명**",value=f"{품목명_필드}", inline=True)
    embed.add_field(name="**수량**",value=f"{세트_필드}", inline=True)
    embed.add_field(name="**금액**",value=f"{금액_필드}", inline=True)
    embed.add_field(name="",value="===========================", inline=False)
    embed.add_field(name=f"**총 금액** `{총금액}원`",value="", inline=True)

    return embed
