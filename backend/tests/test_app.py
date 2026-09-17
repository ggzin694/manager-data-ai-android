from fastapi.testclient import TestClient
from app.main import app
from app.manager import ManagerDataManager

def test_health():
 r=TestClient(app).get('/health'); assert r.status_code==200 and r.json()['status']=='ok'
def test_local_chat():
 m=ManagerDataManager();r=m.chat('revisar estes dados');assert r['agent']=='Reviewer01' and not r['external_call']
def test_auth_and_chat():
 c=TestClient(app);t=c.post('/api/v1/auth/token').json()['access_token'];r=c.post('/api/v1/chat',headers={'Authorization':'Bearer '+t},json={'message':'olá'});assert r.status_code==200
