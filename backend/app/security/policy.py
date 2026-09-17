class SecurityPolicy:
 external_calls_allowed=False
 def check(self,action):return {'allowed':False,'reason':'external actions require explicit configuration and approval'}
