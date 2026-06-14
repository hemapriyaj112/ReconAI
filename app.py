# ============================================================
# app.py — ReconAI Streamlit Web UI
#
# This is what users see in their browser.
# Run with: streamlit run app.py
#
# Streamlit works by re-running this entire file top-to-bottom
# every time the user interacts (clicks a button, types text).
# st.session_state is how we persist data between re-runs.
# ============================================================

import streamlit as st
import time
from src.agent import run_research
from src.report_writer import save_report, list_saved_reports, load_report


# ── Page Configuration ────────────────────────────────────
# Must be the first Streamlit command in the file
st.set_page_config(
    page_title="ReconAI — Research Agent",
    page_icon="🔍",
    layout="wide",          # Use full browser width
    initial_sidebar_state="expanded"
)


# ── Sidebar ───────────────────────────────────────────────
with st.sidebar:
    st.title("📂 Saved Reports")
    st.caption("Reports are saved automatically after each search.")

    saved = list_saved_reports()
    if saved:
        selected_report = st.selectbox(
            "Load a previous report:",
            options=["— select —"] + saved
        )
        if selected_report != "— select —":
            report_text = load_report(selected_report)
            # Store in session state so main area can display it
            st.session_state["loaded_report"] = report_text
            st.session_state["loaded_report_name"] = selected_report
    else:
        st.info("No saved reports yet. Run a search to generate one!")

    st.divider()
    st.caption("ReconAI v0.1 — Semester 1 Build")


# ── Main Area ─────────────────────────────────────────────
st.title("🔍 ReconAI")
st.subheader("Autonomous Research & Report Agent")
st.caption("Type a topic → ReconAI searches the web → generates a structured report")

st.divider()

# ── Search Input ──────────────────────────────────────────
col1, col2 = st.columns([4, 1])   # 4:1 ratio — wide input, narrow button

with col1:
    topic = st.text_input(
        label="Research Topic",
        placeholder="e.g. 'Impact of AI on healthcare 2025' or 'latest breakthroughs in fusion energy'",
        label_visibility="collapsed"   # Hide label (placeholder acts as label)
    )

with col2:
    search_clicked = st.button("🔍 Research", use_container_width=True, type="primary")


# ── Run Research Pipeline ─────────────────────────────────
if search_clicked:
    if not topic.strip():
        st.warning("⚠️ Please enter a research topic first.")
    else:
        # Show a progress spinner while the agent runs
        with st.spinner(f"Researching '{topic}'... this takes about 15-30 seconds"):
            start_time = time.time()

            try:
                # 🚀 This is the main call — runs the full pipeline
                result = run_research(topic)

                elapsed = round(time.time() - start_time, 1)

                # Save report to disk automatically
                filepath = save_report(topic, result["report"])

                # Store result in session state so it persists on re-run
                st.session_state["current_report"] = result["report"]
                st.session_state["current_topic"]  = topic
                st.session_state["elapsed_time"]   = elapsed
                st.session_state["sources"]        = result["sources"]

                # Clear any previously loaded report
                st.session_state.pop("loaded_report", None)

            except Exception as e:
                st.error(f"❌ Something went wrong: {str(e)}")
                st.info("Check your .env file has valid API keys for both ANTHROPIC_API_KEY and TAVILY_API_KEY.")


# ── Display Current Report ────────────────────────────────
if "current_report" in st.session_state:
    st.success(f"✅ Report generated in {st.session_state['elapsed_time']}s")

    # Metrics row
    m1, m2, m3 = st.columns(3)
    m1.metric("Sources Found", len(st.session_state.get("sources", [])))
    m2.metric("Time Taken", f"{st.session_state['elapsed_time']}s")
    m3.metric("Report Length", f"{len(st.session_state['current_report'])} chars")

    st.divider()

    # Download button — lets user save the .md file to their computer
    st.download_button(
        label="⬇️ Download Report (.md)",
        data=st.session_state["current_report"],
        file_name=f"reconai_{st.session_state['current_topic'].replace(' ', '_')}.md",
        mime="text/markdown"
    )

    # Display the report as rendered Markdown
    st.markdown(st.session_state["current_report"])


# ── Display Loaded Report (from sidebar) ─────────────────
elif "loaded_report" in st.session_state:
    st.info(f"📂 Viewing saved report: {st.session_state['loaded_report_name']}")
    st.markdown(st.session_state["loaded_report"])


# ── Empty State (first visit) ─────────────────────────────
else:
    st.markdown("""
    ### How it works:
    1. **Type** any research topic in the box above
    2. **Click** the Research button
    3. ReconAI **searches** the live web using Tavily
    4. **Claude** reads and summarizes the results
    5. You get a **structured report** in seconds

    ---
    **Example topics to try:**
    - `AI regulation in Europe 2025`
    - `breakthroughs in battery technology`
    - `impact of remote work on productivity`
    """)