from .base import BaseAgent,AgentResult
class Collector01(BaseAgent):
 name='Collector01'
 def can_handle(self,m):return any(x in m.lower() for x in ('colet','buscar dados','dados de'))
 def run(self,m,c):return AgentResult('Coleta local preparada. Nenhuma fonte externa foi consultada sem credenciais.',self.name,{'external_call':False})
class Collector02(BaseAgent):
 name='Collector02'
 def can_handle(self,m):return 'import' in m.lower() or 'arquivo' in m.lower()
 def run(self,m,c):return AgentResult('Importação local preparada; forneça um arquivo ou fonte autorizada para continuar.',self.name)
