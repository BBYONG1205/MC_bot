from bot_firebase import 시세_불러오기

def 자원시세_계산(자원, 품목명):

    시세표 = 시세_불러오기(자원) # 광물, 농산물, 물고기 각 정보값 불러오기

    품목_가격 = 시세표.get(품목명)

    if 자원 == "광물":

        개당_가격 = int(round(float(품목_가격)))

        한세트_가격 = int(round(float(품목_가격) * 64))

        한블럭_가격 = int(round(float(품목_가격) * 9))

        블럭세트_가격 = int(round(float(품목_가격) * 9 * 64))

        return 개당_가격, 한세트_가격, 한블럭_가격, 블럭세트_가격

    if 자원 == "농작물" or "물고기":

        개당_가격 = int(round(float(품목_가격)))

        한세트_가격 = int(round(float(개당_가격) * 64))

        return 개당_가격, 한세트_가격