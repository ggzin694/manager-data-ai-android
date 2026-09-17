from pydantic import BaseModel, Field
from typing import Any
class ChatRequest(BaseModel): message:str=Field(min_length=1,max_length=10000); user_id:str='local-user'
class ChatResponse(BaseModel): answer:str; agent:str; safe_mode:bool=True; external_call:bool=False; metadata:dict[str,Any]={}
class TokenResponse(BaseModel): access_token:str; token_type:str='bearer'
