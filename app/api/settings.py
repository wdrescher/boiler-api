from pydantic import BaseSettings, Field

class Settings(BaseSettings):
    jwt_expire_in: int = 600
    app_environment: str = 'dev'
    jwt_sign_algorithm: str = 'HS256'
    api_secret: str = Field('the_score', alias='secret')
    tablename_prefix: str = 'local'
    user_id_cache_expiry: int = 300
    group_id_cache_expiry: int = 1200
    db_username: str = None
    db_password: str = None
    db_db: str = None
    db_instance: str = None
    db_url: str = '3.238.242.230'
    sendgrid_api_key: str = None
    client_hostname: str = 'localhost:4200'
    no_reply_email: str = 'crewteamatvcu@gmail.com'
    app_name: str = "Backstay"
    sendgrid_password_reset_key = "d-e8585c4ff13c46f9b699de1d890c001f"

settings = Settings()
