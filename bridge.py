import os

DEEPSHI_API_KEY = os.environ.get("DEEPSHI_API_KEY", "").strip()
LOCAL_BRIDGE_KEY = os.environ.get("LOCAL_BRIDGE_KEY", "")
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "deepshi-3.0")

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8765"))

UPSTREAM_URL = "https://api.deepshi.ai/v1/chat/completions"
