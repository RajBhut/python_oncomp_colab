import os

class Settings:
    PROJECT_NAME: str = "FastAPI WebSocket Server"
    VERSION: str = "1.0.0"
    HOST: str = os.getenv("HOST", "127.0.0.1")
    PORT: int = int(os.getenv("PORT", 8000))
    DEBUG: bool = os.getenv("DEBUG", "false").lower() in ("true", "1", "t")

settings = Settings()