from urllib.parse import quote_plus
from decouple import config

class Settings:
    username = ""
    password = quote_plus("userinfo@2025")  
    host = ""
    database = ""

    
    DATABASE_URL = f"postgresql://{username}:{password}@{host}/{database}"

settings = Settings()
