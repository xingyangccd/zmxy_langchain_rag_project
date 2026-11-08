import sys
from functools import lru_cache
from pathlib import Path

from pandas import lreshape
from pydantic_settings import BaseSettings, SettingsConfigDict

BACKEND_ROOT = Path(__file__).resolve().parents[1]
if str(BACKEND_ROOT) not in sys.path:
    sys.path.insert(0, str(BACKEND_ROOT))
class Settings(BaseSettings):
    app_name: str = "政务政策 RAG 系统"
    debug: bool = True
    api_prefix: str = "/api"
    database_url: str = (
        "mysql+pymysql://root:xy666666@127.0.0.1:3306/gov_rag?charset=utf8mb4"
    )

    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com"
    deepseek_model: str = "deepseek-v4-flash"

    model_config = SettingsConfigDict(
        env_file=(f"{BACKEND_ROOT}/.env",),  # 此处可以传递一个元组，元组中可以有多个.env路径
        env_file_encoding="utf-8",
        extra="ignore",
    )

@lru_cache
def get_settings()->Settings:
    return Settings()
