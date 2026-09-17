import base64,hmac,hashlib,json,time
from fastapi import Header,HTTPException
from .config import settings

def _b64(data:bytes)->str:return base64.urlsafe_b64encode(data).decode().rstrip('=')
def create_token(subject='local-user'):
 payload=_b64(json.dumps({'sub':subject,'exp':int(time.time())+43200},separators=(',',':')).encode())
 sig=_b64(hmac.new(settings.secret_key.encode(),payload.encode(),hashlib.sha256).digest())
 return payload+'.'+sig
def require_auth(authorization: str|None=Header(default=None)):
 if settings.auth_disabled:return 'local-user'
 if not authorization or not authorization.lower().startswith('bearer '): raise HTTPException(401,'Bearer token required')
 try:
  payload,sig=authorization.split(' ',1)[1].split('.',1)
  expected=_b64(hmac.new(settings.secret_key.encode(),payload.encode(),hashlib.sha256).digest())
  data=json.loads(base64.urlsafe_b64decode(payload+'='*((4-len(payload)%4)%4)))
  if not hmac.compare_digest(sig,expected) or data['exp']<time.time():raise ValueError
  return data['sub']
 except Exception:raise HTTPException(401,'Invalid token')
