from abc import ABC,abstractmethod
class Provider(ABC):
 name='provider'
 @abstractmethod
 def available(self)->bool:...
 @abstractmethod
 def generate(self,prompt:str)->str:...
