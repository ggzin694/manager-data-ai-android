from fastapi import APIRouter,Depends
from ...core.auth import require_auth,create_token
from ...core.schemas import ChatRequest,ChatResponse,TokenResponse
from ...manager import ManagerDataManager
router=APIRouter(); manager=ManagerDataManager()
@router.post('/auth/token',response_model=TokenResponse)
def token():return {'access_token':create_token()}
@router.get('/auth/me')
def me(user=Depends(require_auth)):return {'user_id':user}
@router.post('/chat',response_model=ChatResponse)
def chat(req:ChatRequest,user=Depends(require_auth)):
 r=manager.chat(req.message,req.user_id or user);return r
@router.get('/agents')
def agents(user=Depends(require_auth)):return {'agents':[a.name for a in manager.agents], 'provider':'local-fallback'}
