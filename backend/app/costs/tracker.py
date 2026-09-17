class CostTracker:
 def __init__(self):self.events=[]
 def record(self,provider,tokens=0):self.events.append({'provider':provider,'tokens':tokens})
 def summary(self):return {'events':len(self.events),'tokens':sum(x['tokens'] for x in self.events)}
