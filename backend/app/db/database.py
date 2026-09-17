from sqlalchemy import create_engine,text
from ..core.config import settings
engine=create_engine(settings.database_url)
def check_database():
 try:
  with engine.connect() as c:c.execute(text('SELECT 1'))
  return True
 except Exception:return False
