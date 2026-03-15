from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "Spiritual Wisdom API"
    app_env: str = "development"
    app_debug: bool = True
    database_url: str
    cors_origins: str = "http://localhost:3000"
    openai_api_key: str = ""
    embedding_model: str = "text-embedding-3-small"
    chat_model: str = "gpt-5-mini"
    top_k_retrieval: int = 6

    model_config = SettingsConfigDict(env_file=".env", extra="ignore")


settings = Settings()
