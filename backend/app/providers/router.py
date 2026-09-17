from .local import LocalProvider
class ProviderRouter:
 def __init__(self):self.local=LocalProvider()
 def generate(self,prompt):return self.local.generate(prompt),self.local.name
