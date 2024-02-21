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