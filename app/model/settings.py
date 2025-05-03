from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    upload_dir: str = None
    kafka_brokers: str = None




