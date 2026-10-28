
import os

DEEPSHI_API_KEY = os.environ.get("sk-bf-05bd4acc-6816-4b0b-98bf-f27f27c7c8f7", "").strip()
LOCAL_BRIDGE_KEY = os.environ.get("deepshi-local-bridge-key-8765", "")
DEFAULT_MODEL = os.environ.get("DEFAULT_MODEL", "deepshi-3.0")

HOST = "0.0.0.0"
PORT = int(os.environ.get("PORT", "8765"))

UPSTREAM_URL = "https://api.deepshi.ai/v1/chat/completions"
