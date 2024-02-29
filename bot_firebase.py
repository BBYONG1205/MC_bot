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

def 정산요청서_생성(요청자, 요청서생성):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc_ref.set(요청서생성)


def 정산요청서_불러오기(요청자):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

def 정산요청내역_업데이트(요청자, 요청서업데이트,요청금액_합계):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc_ref.update({
            "요청내역": firestore.ArrayUnion([요청서업데이트]),
            "총 금액" : 요청금액_합계
        })
    

def 정산요청상세_불러오기(요청자):
    db = firestore.client()
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc = doc_ref.get()

    if doc.exists:
        
        품목_목록 = doc.to_dict().get('요청내역', [])
        
        # 모든 참여자의 이름 목록 가져오기
        품목명_리스트 = [품목.get('품목명', '내역없음') for 품목 in 품목_목록]
        금액_리스트 = [금액.get('금액', '내역없음') for 금액 in 품목_목록]
        세트_리스트 = [세트.get('세트', '내역없음') for 세트 in 품목_목록]

        return 품목명_리스트, 금액_리스트 , 세트_리스트
    else:
        print('해당 문서가 존재하지 않습니다.')


def 정산요청내역_삭제(요청자):
    doc_ref = db.collection('정산 요청서').document(str(요청자))
    doc_ref.delete()

