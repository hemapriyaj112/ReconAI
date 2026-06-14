# ============================================================
# tests/test_setup.py — ReconAI Setup Verification
#
# Run this FIRST to verify all connections are working.
# Usage: python tests/test_setup.py
# ============================================================

import sys
import os

# Add project root to Python's path so we can import src/
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def test_env_variables():
    """Check that .env file exists and has the required keys."""
    print("\n📋 Test 1: Checking API keys in .env...")

    from dotenv import load_dotenv
    load_dotenv()

    google_key = os.getenv("GOOGLE_API_KEY")
    tavily_key = os.getenv("TAVILY_API_KEY")

    if not google_key or google_key == "your_gemini_api_key_here":
        print("   ❌ GOOGLE_API_KEY missing or not set in .env")
        print("      → Get your free key at: https://aistudio.google.com/app/apikey")
        return False

    if not tavily_key or tavily_key == "your_tavily_api_key_here":
        print("   ❌ TAVILY_API_KEY missing or not set in .env")
        print("      → Get your free key at: https://app.tavily.com/")
        return False

    print(f"   ✅ GOOGLE_API_KEY found  (ends in ...{google_key[-4:]})")
    print(f"   ✅ TAVILY_API_KEY found  (ends in ...{tavily_key[-4:]})")
    return True


def test_llm_connection():
    """Send a simple message to Gemini and check for a response."""
    print("\n🤖 Test 2: Testing Gemini API connection...")
    try:
        from src.llm import get_llm
        llm = get_llm()
        response = llm.invoke("Reply with exactly: 'ReconAI LLM test passed'")
        print(f"   ✅ Gemini responded: {response.content}")
        return True
    except Exception as e:
        print(f"   ❌ Gemini API failed: {e}")
        return False


def test_search_connection():
    """Run a simple Tavily search and check results come back."""
    print("\n🔍 Test 3: Testing Tavily search...")
    try:
        from src.search_tool import get_search_tool
        tool    = get_search_tool()
        results = tool.invoke("Python programming language")

        if results and len(results) > 0:
            print(f"   ✅ Tavily returned {len(results)} results")
            print(f"   ✅ First result: {results[0].get('title', 'N/A')}")
            return True
        else:
            print("   ❌ Tavily returned no results")
            return False
    except Exception as e:
        print(f"   ❌ Tavily search failed: {e}")
        return False


def test_full_pipeline():
    """Run the complete ReconAI pipeline on a simple topic."""
    print("\n🚀 Test 4: Full pipeline test (search + summarize)...")
    try:
        from src.agent import run_research
        result = run_research("what is Python programming language")

        if result and result.get("report") and len(result["report"]) > 100:
            print(f"   ✅ Report generated ({len(result['report'])} characters)")
            print(f"   ✅ Sources found: {len(result['sources'])}")
            return True
        else:
            print("   ❌ Report was empty or too short")
            return False
    except Exception as e:
        print(f"   ❌ Pipeline failed: {e}")
        return False


if __name__ == "__main__":
    print("=" * 55)
    print("  ReconAI — Setup Verification Tests")
    print("=" * 55)

    results = [
        test_env_variables(),
        test_llm_connection(),
        test_search_connection(),
        test_full_pipeline(),
    ]

    passed = sum(results)
    total  = len(results)

    print("\n" + "=" * 55)
    print(f"  Results: {passed}/{total} tests passed")
    print("=" * 55)

    if passed == total:
        print("\n🎉 All tests passed! Run the app with:")
        print("   streamlit run app.py\n")
    else:
        print("\n⚠️  Some tests failed. Fix the errors above before running the app.\n")