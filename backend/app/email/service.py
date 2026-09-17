from abc import ABC,abstractmethod
class EmailService(ABC):
 @abstractmethod
 async def send(self,*args,**kwargs):...
class DisabledEmailService(EmailService):
 async def send(self,*args,**kwargs):return {'sent':False,'reason':'email provider not configured'}
