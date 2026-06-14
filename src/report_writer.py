# ============================================================
# src/report_writer.py — Save Reports to Disk
#
# Takes the report text from the agent and saves it as a
# Markdown file in the /reports folder with a timestamp.
# (Semester 2 will add PDF/Word export here)
# ============================================================

import os
from datetime import datetime
from src.config import REPORTS_DIR


def save_report(topic: str, report_text: str) -> str:
    """
    Saves a generated report to the /reports directory as a .md file.

    File naming: reports/quantum_computing_2025-01-15_14-30.md
    (spaces in topic replaced with underscores, timestamp appended)

    Args:
        topic (str):       The research topic (used in filename)
        report_text (str): The full markdown report content

    Returns:
        str: The full file path where the report was saved
    """
    # Make sure the reports directory exists
    os.makedirs(REPORTS_DIR, exist_ok=True)

    # Build a clean filename from the topic
    # e.g. "Quantum Computing 2025" → "quantum_computing_2025"
    safe_topic = topic.lower().replace(" ", "_").replace("/", "-")[:50]
    timestamp  = datetime.now().strftime("%Y-%m-%d_%H-%M")
    filename   = f"{safe_topic}_{timestamp}.md"
    filepath   = os.path.join(REPORTS_DIR, filename)

    # Write the report to disk
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report_text)

    print(f"💾 Report saved to: {filepath}")
    return filepath


def list_saved_reports() -> list[str]:
    """
    Returns a list of all saved report filenames in /reports.
    Used by the Streamlit UI to show previous reports.

    Returns:
        list[str]: Filenames (not full paths) of saved .md files
    """
    if not os.path.exists(REPORTS_DIR):
        return []

    files = [f for f in os.listdir(REPORTS_DIR) if f.endswith(".md")]
    return sorted(files, reverse=True)   # newest first


def load_report(filename: str) -> str:
    """
    Loads a previously saved report from /reports by filename.

    Args:
        filename (str): Just the filename, e.g. "quantum_2025.md"

    Returns:
        str: The full report text
    """
    filepath = os.path.join(REPORTS_DIR, filename)
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()