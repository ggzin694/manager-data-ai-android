class MemoryManager:
 def __init__(self):self._items=[]
 def add(self,user_id,content):self._items.append({'user_id':user_id,'content':content})
 def recent(self,user_id,limit=10):return [x for x in self._items if x['user_id']==user_id][-limit:]
