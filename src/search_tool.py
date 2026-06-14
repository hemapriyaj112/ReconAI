# ============================================================
# src/search_tool.py — Web Search via Tavily
#
# This module wraps the Tavily search API as a LangChain Tool.
# The agent will call this tool whenever it needs to search
# the live web for information about the user's topic.
# ============================================================

from langchain_community.tools.tavily_search import TavilySearchResults
from src.config import TAVILY_API_KEY, SEARCH_MAX_RESULTS
import os

# Set the Tavily API key as an environment variable
# (Tavily's LangChain integration reads it from here)
os.environ["TAVILY_API_KEY"] = TAVILY_API_KEY


def get_search_tool() -> TavilySearchResults:
    """
    Creates and returns a Tavily search tool configured for ReconAI.

    The tool returns structured results: each result has:
      - url:     the source URL
      - content: a snippet of the page content
      - title:   the page title

    Returns:
        TavilySearchResults: A LangChain-compatible tool the agent can call.
    """
    search_tool = TavilySearchResults(
        max_results=SEARCH_MAX_RESULTS,   # Number of results per search
        include_answer=True,              # Include Tavily's own AI summary
        include_raw_content=False,        # Raw HTML — not needed, too noisy
        include_images=False,             # Skip images for now
    )

    # Give the tool a clear description so the LLM knows when to use it
    # (LangChain agents read this description to decide which tool to call)
    search_tool.description = (
        "Use this tool to search the web for current, real-time information. "
        "Input should be a clear search query string. "
        "Returns a list of search results with titles, URLs, and content snippets. "
        "Use this when you need facts, news, or any live data about a topic."
    )

    return search_tool


def test_search(query: str = "latest developments in AI 2025") -> None:
    """
    Quick test function to verify your Tavily setup is working.
    Run this directly: python -m src.search_tool
    """
    print(f"\n🔍 Testing Tavily search with query: '{query}'\n")
    tool = get_search_tool()
    results = tool.invoke(query)

    if isinstance(results, list):
        for i, result in enumerate(results, 1):
            print(f"Result {i}:")
            print(f"  Title:   {result.get('title', 'N/A')}")
            print(f"  URL:     {result.get('url', 'N/A')}")
            print(f"  Snippet: {result.get('content', 'N/A')[:150]}...\n")
    else:
        print(results)


# Run test if this file is executed directly
if __name__ == "__main__":
    test_search()