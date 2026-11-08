from typing import Any

from docx.settings import Settings
from langchain.chat_models import init_chat_model
from langchain_core.language_models import BaseChatModel
from langchain_core.messages import AIMessage

from app.config import Settings, get_settings

def create_chat_model(
    temperature: float = 0,
    settings: Settings | None = None,
) -> BaseChatModel:
    settings = settings or get_settings()

    if not settings.deepseek_api_key:
        raise RuntimeError("DEEPSEEK_API_KEY 未配置")

    return init_chat_model(
        model=settings.deepseek_model,
        model_provider="openai",
        api_key=settings.deepseek_api_key,
        base_url=settings.deepseek_base_url,
        temperature=temperature,
    )


async def invoke_text(model: BaseChatModel, prompt: str) -> tuple[str, dict[str, Any]]:
    response = await model.ainvoke(prompt)
    if not isinstance(response, AIMessage):
        raise TypeError(f"聊天模型返回了不支持的消息类型：{type(response).__name__}")
    return response.text, dict(response.usage_metadata or {})