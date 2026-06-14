# ============================================================
# src/config.py — Central Configuration for ReconAI
#
# This file loads all API keys from your .env file and
# provides them as constants to the rest of the app.
# ============================================================

import os
from dotenv import load_dotenv

# Load the .env file — reads your API keys into environment variables
load_dotenv()


def get_api_key(key_name: str) -> str:
    """
    Safely fetch an API key from environment variables.
    Raises a clear error if the key is missing.
    """
    value = os.getenv(key_name)
    if not value:
        raise ValueError(
            f"\n❌ Missing API key: '{key_name}'\n"
            f"   → Copy .env.example to .env and add your key there.\n"
            f"   → Never hardcode keys directly in Python files!\n"
        )
    return value


# ── API Keys ──────────────────────────────────────────────
GOOGLE_API_KEY = get_api_key("GOOGLE_API_KEY")   # Gemini (free tier)
TAVILY_API_KEY = get_api_key("TAVILY_API_KEY")   # Tavily search (free tier)

# ── LLM Settings ──────────────────────────────────────────
# gemini-2.0-flash: fast, free, great for summarization
# Free tier: 1500 requests/day, 1 million tokens/day
LLM_MODEL      = "gemini-2.5-flash"

# Max tokens for the LLM response (1 token ≈ 0.75 words)
LLM_MAX_TOKENS = 2000

# ── Search Settings ───────────────────────────────────────
# How many search results Tavily should return per query
SEARCH_MAX_RESULTS = 5

# ── Report Settings ───────────────────────────────────────
# Where generated reports get saved
REPORTS_DIR = os.path.join(os.path.dirname(__file__), "..", "reports")