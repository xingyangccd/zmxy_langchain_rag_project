import asyncio

from app.config import get_settings
from app.model_factory import create_chat_model, invoke_text


async def main():
    model = create_chat_model(temperature=0.5, settings=get_settings())
    result=await invoke_text(model, "什么是LangChain?")
    print(result[0])
    print(result[1])

if __name__ == '__main__':
    asyncio.run(main())