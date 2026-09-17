import asyncio
from abc import ABC,abstractmethod
class ResearchEngine(ABC):
 @abstractmethod
 async def search(self,query:str):...
class SafeResearchEngine(ResearchEngine):
 def __init__(self,timeout=8):self.timeout=timeout;self.cache={}
 async def search(self,query):
  if query in self.cache:return self.cache[query]
  result={'query':query,'sources':[],'status':'not_configured','external_call':False}
  self.cache[query]=result; return result
