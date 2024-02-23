import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate('./calculatebot-667f4-firebase-adminsdk-30usx-0850ba7a7f.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

# 멤버 정보를 Firebase에 저장
def 멤버정보_저장(member_id, 멤버정보):
    doc_ref = db.collection('멤버 정보').document(str(member_id))
    doc_ref.set(멤버정보)
    

def 멤버정보_불러오기(member_id):
    doc_ref = db.collection('멤버 정보').document(str(member_id))
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    
def 시세_불러오기(자원):
    doc_ref = db.collection('시세표').document(str(자원))
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None
    

def 시세_업데이트(자원, 품목명, 변동가격):

    user_ref = db.collection('시세표').document(str(자원))
    update_marketprice = {품목명 : 변동가격}

    user_ref.update(update_marketprice)

def 정산요청서_생성(요청자, 총금액):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc_ref.set(총금액)


def 정산요청서_불러오기(요청자):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None


def 정산요청내역_업데이트(요청자, 품목명, 요청내역, 요청금액_합계):
    user_ref = db.collection('정산 요청서').document(str(요청자))
    update_Settlement = {
        품목명: 요청내역,
        "총 합": 요청금액_합계
    }

    user_ref.update(update_Settlement)

def 정산요청내역_삭제(요청자):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc_ref.delete()