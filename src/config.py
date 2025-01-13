from pydantic_settings import BaseSettings
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    dbPort: str
    dbPassword: str
    dbUsername: str
    dbName: str
    dbHostname: str