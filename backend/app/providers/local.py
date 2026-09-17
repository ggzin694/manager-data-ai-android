from .base import Provider
class LocalProvider(Provider):
 name='local-fallback'
 def available(self):return True
 def generate(self,prompt):return 'Fallback local ativo. Não há provedor externo configurado; posso organizar, revisar e planejar dados localmente.'
