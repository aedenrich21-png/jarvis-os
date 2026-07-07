import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    APP_NAME = "JARVIS OS"
    VERSION = "0.1.0"

    USER_NAME = "Aeden"

    MEMORY_FILE = "data/memory.json"

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")


settings = Settings()
