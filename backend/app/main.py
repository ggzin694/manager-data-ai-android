from fastapi import FastAPI
from .core.config import settings
from .api.v1.routes import router
from .db.database import check_database
app=FastAPI(title=settings.app_name,version='0.1.0');app.include_router(router,prefix='/api/v1')
@app.get('/health')
def health():return {'status':'ok','service':settings.app_name,'database':check_database(),'external_providers':'not_configured'}
