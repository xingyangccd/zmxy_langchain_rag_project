from backend.app.config import get_settings

s=get_settings()
print(s.app_name)
print(s.api_prefix)
print(s.deepseek_model)