from fastapi import FastAPI

from app.config import get_settings

settings = get_settings()


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        description="FastAPI + LangChain 政策知识库问答系统",
        version="1.0.0",
    )

    @app.get("/")
    async def root():
        return {
            "name": "政务政策 RAG 系统",
            "docs": "/docs",
            "message": "服务已启动",
        }

    return app