from .base import BaseAgent,AgentResult
class Reviewer01(BaseAgent):
 name='Reviewer01'
 def can_handle(self,m):return any(x in m.lower() for x in ('revis','valid','qualidade','verif'))
 def run(self,m,c):return AgentResult('Revisão inicial concluída localmente: faltam dados/fontes para validar afirmações externas.',self.name,{'verified':False})
