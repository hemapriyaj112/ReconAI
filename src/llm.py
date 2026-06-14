# ============================================================
# src/llm.py — LLM Setup (Gemini via LangChain)
#
# Swapped from Claude → Google Gemini (free tier).
# Everything else in the app stays the same — LangChain
# abstracts away the provider difference.
# ============================================================

from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import GOOGLE_API_KEY, LLM_MODEL, LLM_MAX_TOKENS


def get_llm() -> ChatGoogleGenerativeAI:
    """
    Creates and returns a Gemini LLM instance for use in chains and agents.

    ChatGoogleGenerativeAI is LangChain's wrapper around the Google Gemini API.
    It works as a drop-in replacement for ChatAnthropic or ChatOpenAI —
    same .invoke(), same chaining with |, same everything.

    Returns:
        ChatGoogleGenerativeAI: A LangChain-compatible LLM instance.
    """
    llm = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        google_api_key=GOOGLE_API_KEY,
        max_output_tokens=LLM_MAX_TOKENS,

        # Temperature controls creativity vs. consistency:
        #   0.0 = very focused, deterministic (good for factual reports)
        #   1.0 = more creative, varied
        temperature=0.3,
    )
    return llm


def test_llm() -> None:
    """
    Quick sanity check — sends a simple message to Gemini.
    Run with: python -m src.llm
    """
    print("\n🤖 Testing Gemini API connection...\n")
    llm = get_llm()
    response = llm.invoke("Say hello and confirm you are Gemini. Keep it to one sentence.")
    print(f"Gemini says: {response.content}\n")
    print("✅ LLM connection working!\n")


if __name__ == "__main__":
    test_llm()