from pydantic_settings import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    app_name:str='Manager Data AI'; app_env:str='development'; secret_key:str='change-me-locally'
    database_url:str='sqlite:///./manager_data.db'; redis_url:str='redis://localhost:6379/0'
    auth_disabled:bool=False; research_timeout_seconds:float=8.0
    model_config=SettingsConfigDict(env_file='.env', extra='ignore')
settings=Settings()
