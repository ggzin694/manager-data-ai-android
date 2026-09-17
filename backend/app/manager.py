from .agents.collectors import Collector01,Collector02
from .agents.reviewer import Reviewer01
from .agents.security import Security01
from .providers.router import ProviderRouter
from .memory.manager import MemoryManager
class ManagerDataManager:
 def __init__(self):
  self.agents=[Security01(),Reviewer01(),Collector01(),Collector02()]; self.router=ProviderRouter(); self.memory=MemoryManager()
 def chat(self,message,user_id='local-user'):
  self.memory.add(user_id,message)
  for agent in self.agents:
   if agent.can_handle(message):
    r=agent.run(message,{'memory':self.memory.recent(user_id)}); return {'answer':r.answer,'agent':r.agent,'metadata':r.metadata,'safe_mode':True,'external_call':False}
  answer,provider=self.router.generate(message)
  return {'answer':answer,'agent':'ManagerDataManager','metadata':{'provider':provider},'safe_mode':True,'external_call':False}
