from .base import BaseAgent,AgentResult
class Security01(BaseAgent):
 name='Security01'
 def can_handle(self,m):return any(x in m.lower() for x in ('senha','segurança','security','token','credencial'))
 def run(self,m,c):return AgentResult('Modo seguro: não acesso, exponho ou executo credenciais e não faço ações externas automaticamente.',self.name,{'external_call':False})
