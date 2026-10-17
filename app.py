
import streamlit as st
from src.rag_pipeline import ask_question

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="TechMarcus | AI Support",
    page_icon="💬",
    layout="wide",
    initial_sidebar_state="expanded",
)

# --------------------------------------------------
# CUSTOM STYLING
# --------------------------------------------------

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

    :root {
        --tm-blue: #315CF5;
        --tm-dark: #172033;
        --tm-muted: #687386;
        --tm-border: #E7EAF0;
        --tm-bg: #F7F8FC;
    }

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    .stApp {
        background: var(--tm-bg);
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: #FFFFFF;
        border-right: 1px solid var(--tm-border);
    }

    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1.5rem;
    }

    .tm-brand {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }

    .tm-logo {
        background: var(--tm-blue);
        color: white;
        width: 42px;
        height: 42px;
        border-radius: 13px;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 19px;
        font-weight: 800;
    }

    .tm-brand-name {
        font-size: 22px;
        font-weight: 800;
        color: var(--tm-dark);
        letter-spacing: -0.8px;
    }

    .tm-brand-subtitle {
        color: var(--tm-muted);
        font-size: 12px;
        margin-top: 2px;
    }

    .tm-topbar {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 12px;
        flex-wrap: wrap;
        padding: 10px 0 20px 0;
        border-bottom: 1px solid var(--tm-border);
        margin-bottom: 30px;
    }

    .tm-page-title {
        color: var(--tm-dark);
        font-size: 25px;
        font-weight: 750;
        letter-spacing: -0.8px;
        margin: 0;
    }

    .tm-page-subtitle {
        color: var(--tm-muted);
        font-size: 13px;
        margin-top: 6px;
    }

    .tm-status {
        display: inline-flex;
        align-items: center;
        gap: 7px;
        padding: 8px 12px;
        border: 1px solid var(--tm-border);
        background: white;
        border-radius: 20px;
        color: #344054;
        font-size: 12px;
        font-weight: 600;
    }

    .tm-status-dot {
        height: 8px;
        width: 8px;
        border-radius: 50%;
        background: #16A36A;
    }

    .tm-welcome {
        text-align: center;
        padding: 35px 10px 22px 10px;
    }

    .tm-welcome-icon {
        width: 68px;
        height: 68px;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        border-radius: 22px;
        background: #E9EEFF;
        font-size: 32px;
        margin-bottom: 18px;
    }

    .tm-welcome h2 {
        font-size: 30px;
        line-height: 1.3;
        letter-spacing: -1px;
        color: var(--tm-dark);
        margin: 0 0 12px 0;
    }

    .tm-welcome p {
        font-size: 14px;
        color: var(--tm-muted);
        line-height: 1.8;
        max-width: 520px;
        margin: auto;
    }

    .tm-section-label {
        color: #475467;
        font-size: 12px;
        font-weight: 700;
        letter-spacing: 0.5px;
        text-transform: uppercase;
        margin: 15px 0 8px 0;
    }

    .stButton > button {
        border-radius: 12px;
        border: 1px solid var(--tm-border);
        background: white;
        color: var(--tm-dark);
        font-weight: 600;
        min-height: 52px;
        transition: all 0.15s ease;
    }

    .stButton > button:hover {
        border-color: var(--tm-blue);
        color: var(--tm-blue);
        background: #F7F9FF;
    }

    /* Chat message container */
    [data-testid="stChatMessage"] {
        background: #FFFFFF !important;
        color: #172033 !important;
        border: 1px solid #E7EAF0;
        border-radius: 16px;
        padding: 16px 18px;
        margin-bottom: 14px;
    }

    /* Ensure chat text is readable */
    [data-testid="stChatMessage"] p,
    [data-testid="stChatMessage"] span,
    [data-testid="stChatMessage"] li,
    [data-testid="stChatMessage"] strong,
    [data-testid="stChatMessage"] em,
    [data-testid="stChatMessage"] h1,
    [data-testid="stChatMessage"] h2,
    [data-testid="stChatMessage"] h3,
    [data-testid="stChatMessage"] [data-testid="stMarkdownContainer"] {
        color: #172033 !important;
    }

    /* General Markdown readability */
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li {
        color: #172033;
    }

    [data-testid="stChatInput"] {
        border-color: var(--tm-border);
    }

    [data-testid="stChatInput"] textarea {
        font-family: 'Inter', sans-serif;
    }

    .tm-footer {
        text-align: center;
        color: var(--tm-muted);
        font-size: 11px;
        padding: 18px 0 8px 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# --------------------------------------------------
# SIDEBAR
# --------------------------------------------------

with st.sidebar:
    st.markdown(
        """
        <div class="tm-brand">
            <div class="tm-logo">TM</div>
            <div>
                <div class="tm-brand-name">TechMarcus</div>
                <div class="tm-brand-subtitle">AI Customer Support</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("---")

    if st.button(
        "＋  New conversation",
        use_container_width=True,
        type="primary",
    ):
        st.session_state.messages = []
        st.session_state.pending_prompt = None
        st.rerun()

    st.markdown("#### Conversation")

    if not st.session_state.messages:
        st.caption("Your conversation will appear here.")
    else:
        for message in st.session_state.messages:
            if message["role"] == "user":
                label = message["content"].replace("\n", " ")

                if len(label) > 35:
                    label = label[:35] + "..."

                st.markdown(f"💬 {label}")

    st.markdown("---")
    st.markdown("#### About TechMarcus")

    st.caption(
        "An AI support assistant that uses your indexed "
        "knowledge base to answer customer questions."
    )

    st.markdown(
        """
        <div style="
            padding: 12px;
            background: #F2F5FF;
            border-radius: 12px;
            font-size: 12px;
            color: #344054;
            line-height: 1.7;
        ">
            <strong>🔒 Local AI setup</strong><br>
            Your language model runs locally through Ollama.
        </div>
        """,
        unsafe_allow_html=True,
    )

# --------------------------------------------------
# MAIN HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="tm-topbar">
        <div>
            <div class="tm-page-title">
                Customer Support Assistant
            </div>
            <div class="tm-page-subtitle">
                Ask a question and get help from the TechMarcus knowledge base.
            </div>
        </div>
        <div class="tm-status">
            <span class="tm-status-dot"></span>
            Local AI
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# --------------------------------------------------
# WELCOME SCREEN AND SUGGESTED QUESTIONS
# --------------------------------------------------

if not st.session_state.messages:
    st.markdown(
        """
        <div class="tm-welcome">
            <div class="tm-welcome-icon">✦</div>
            <h2>How can we help today?</h2>
            <p>
                Ask us about product issues, returns, refunds, or support.
                Type your question below or start with one of these examples.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="tm-section-label">Suggested questions</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        if st.button(
            "📦  My item arrived damaged",
            use_container_width=True,
        ):
            st.session_state.pending_prompt = (
                "My item arrived damaged. Can I get a replacement?"
            )

        if st.button(
            "💳  Refund processing time",
            use_container_width=True,
        ):
            st.session_state.pending_prompt = (
                "How long does it take to receive an approved refund?"
            )

    with col2:
        if st.button(
            "🛠️  Product support",
            use_container_width=True,
        ):
            st.session_state.pending_prompt = (
                "What information should I provide when contacting support?"
            )

        if st.button(
            "🛡️  Warranty information",
            use_container_width=True,
        ):
            st.session_state.pending_prompt = (
                "What information is available about product warranties?"
            )

# --------------------------------------------------
# DISPLAY CHAT HISTORY
# --------------------------------------------------

for message in st.session_state.messages:
    role = message["role"]

    with st.chat_message(
        role,
        avatar="👤" if role == "user" else "🤖",
    ):
        st.markdown(message["content"])

# --------------------------------------------------
# PROCESS QUESTIONS
# --------------------------------------------------

typed_prompt = st.chat_input("Ask TechMarcus a question...")

prompt = typed_prompt

if not prompt and st.session_state.pending_prompt:
    prompt = st.session_state.pending_prompt
    st.session_state.pending_prompt = None

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    with st.chat_message("user", avatar="👤"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar="🤖"):
        with st.spinner("Thinking..."):
            try:
                result = ask_question(prompt)

                answer = result.get(
                    "answer",
                    "Sorry, I couldn't generate an answer.",
                )

                st.markdown(answer)

                # Store sources internally for future debugging,
                # but do not display them in the customer interface.
                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": answer,
                        "sources": result.get("sources", []),
                    }
                )

            except Exception as error:
                error_message = (
                    "Sorry, something went wrong while processing "
                    "your question. Please check that Ollama is running "
                    "and try again."
                )

                st.error(error_message)

                with st.expander("View technical error"):
                    st.code(str(error))

                st.session_state.messages.append(
                    {
                        "role": "assistant",
                        "content": error_message,
                        "sources": [],
                    }
                )

    st.rerun()

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.markdown(
    """
    <div class="tm-footer">
        TechMarcus AI Support · AI-generated responses may need verification.
    </div>
    """,
    unsafe_allow_html=True,
)
