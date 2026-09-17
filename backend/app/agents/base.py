from abc import ABC,abstractmethod
from dataclasses import dataclass,field
@dataclass
class AgentResult: answer:str; agent:str; metadata:dict=field(default_factory=dict)
class BaseAgent(ABC):
 name='base'
 @abstractmethod
 def can_handle(self,message:str)->bool:...
 @abstractmethod
 def run(self,message:str,context:dict)->AgentResult:...
