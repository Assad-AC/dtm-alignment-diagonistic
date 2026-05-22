# ============================================================
# DTM Survey Alignment Tool — config.py
# Page config, default parameters, and CSS
# ============================================================

import streamlit as st

# ────────────────────────────────────────────────────────────
# Page configuration
# ────────────────────────────────────────────────────────────

PAGE_CONFIG = {
    "page_title": "DTM Survey Alignment Tool",
    "page_icon":  "🗺️",
    "layout":     "wide",
    "initial_sidebar_state": "expanded",
    "menu_items": {
        "About": (
            "**DTM Survey Alignment Tool**  \n"
            "Matches IOM DTM survey XLSForms against the Global Data Kit.  \n"
            "Produces a colour-coded Excel diagnostic report."
        ),
    },
}

# ────────────────────────────────────────────────────────────
# Default parameters
# ────────────────────────────────────────────────────────────

DEFAULTS = {
    "datakit_sheet":    "myWorkSheet",
    "survey_sheet":     "survey_raw",
    "formcomponents":   "Baseline Sub-Area Assessment",
    "fuzzy_threshold":  0.20,
    "df1_key_col":      "name",
    "df1_text_col":     "label",
    "df1_type_col":     "type",
    "df2_key_col":      "FieldName",
    "df2_text_col":     "QuestionText(en)",
    "df2_id_col":       "FieldUniqueId",
    "df2_type_col":     "QuestionAnswerType",
    "df2_comp_col":     "QuestionComponent",
}

# ────────────────────────────────────────────────────────────
# Status colour palette  (used in both UI and Excel export)
# ────────────────────────────────────────────────────────────

STATUS_COLOURS_HEX = {
    "LikelyAligned":       "#C6EFCE",
    "NeedsVerification":   "#FFEB9C",
    "FPReview":            "#FFC7CE",
    "DiscouragedQuestion": "#FCE4D6",
    "MissingCoreQuestion": "#E2D9F3",
    "DoesNotNeed2Align":   "#F5F5F5",
}

STATUS_FONT_HEX = {
    "LikelyAligned":       "#375623",
    "NeedsVerification":   "#9C6500",
    "FPReview":            "#9C0006",
    "DiscouragedQuestion": "#833C00",
    "MissingCoreQuestion": "#4B2E83",
    "DoesNotNeed2Align":   "#666666",
}

STATUS_EMOJI = {
    "LikelyAligned":       "✅",
    "NeedsVerification":   "🔍",
    "FPReview":            "⚠️",
    "DiscouragedQuestion": "🚫",
    "MissingCoreQuestion": "🔴",
    "DoesNotNeed2Align":   "—",
}

# ────────────────────────────────────────────────────────────
# CSS
# ────────────────────────────────────────────────────────────

CUSTOM_CSS = """
/* ── Brand colours ───────────────────────────────────────── */
:root {
    --dtm-dark-blue:  #1F3864;
    --dtm-mid-blue:   #2E5797;
    --dtm-light-blue: #D6E4F7;
    --dtm-grey:       #F5F5F5;
    --dtm-border:     #DEE2E6;
    --dtm-text:       #212529;
    --dtm-muted:      #6C757D;
}

/* ── App header ──────────────────────────────────────────── */
.dtm-title {
    color: var(--dtm-dark-blue);
    font-size: 1.85rem;
    font-weight: 700;
    margin-bottom: 0.1rem;
    line-height: 1.2;
}
.dtm-sub {
    color: var(--dtm-muted);
    font-size: 0.88rem;
    margin-top: 0.1rem;
    margin-bottom: 0;
}

/* ── Sidebar ─────────────────────────────────────────────── */
[data-testid="stSidebar"] {
    background-color: #F8FAFD;
    border-right: 1px solid var(--dtm-border);
}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {
    color: var(--dtm-dark-blue);
}
.sidebar-section {
    font-weight: 600;
    color: var(--dtm-dark-blue);
    font-size: 0.92rem;
    letter-spacing: 0.01em;
    margin-top: 0.25rem;
    margin-bottom: 0.25rem;
}

/* ── Metric cards ────────────────────────────────────────── */
div[data-testid="metric-container"] {
    background-color: #FFFFFF;
    border: 1px solid var(--dtm-border);
    border-left: 4px solid var(--dtm-mid-blue);
    border-radius: 6px;
    padding: 0.7rem 0.9rem;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
}
div[data-testid="metric-container"] label {
    font-size: 0.78rem !important;
    color: var(--dtm-muted) !important;
    font-weight: 500;
}
div[data-testid="metric-container"] [data-testid="stMetricValue"] {
    font-size: 1.6rem !important;
    font-weight: 700;
    color: var(--dtm-dark-blue);
}

/* ── Primary button (Run) ────────────────────────────────── */
div[data-testid="stButton"] > button[kind="primary"] {
    background-color: var(--dtm-dark-blue);
    color: #FFFFFF;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    padding: 0.55rem 1.2rem;
    transition: background-color 0.2s ease;
}
div[data-testid="stButton"] > button[kind="primary"]:hover {
    background-color: var(--dtm-mid-blue);
    color: #FFFFFF;
}
div[data-testid="stButton"] > button[kind="primary"]:disabled {
    background-color: #B0BEC5;
    color: #ECEFF1;
}

/* ── Download button ─────────────────────────────────────── */
div[data-testid="stDownloadButton"] > button {
    background-color: var(--dtm-dark-blue);
    color: #FFFFFF;
    border: none;
    border-radius: 6px;
    font-weight: 600;
    width: 100%;
    transition: background-color 0.2s ease;
}
div[data-testid="stDownloadButton"] > button:hover {
    background-color: var(--dtm-mid-blue);
    color: #FFFFFF;
}

/* ── File uploader ───────────────────────────────────────── */
[data-testid="stFileUploader"] {
    border: 1.5px dashed var(--dtm-mid-blue);
    border-radius: 6px;
    padding: 0.4rem 0.6rem;
    background-color: #F8FAFD;
}
[data-testid="stFileUploader"]:hover {
    border-color: var(--dtm-dark-blue);
    background-color: var(--dtm-light-blue);
}

/* ── Section divider ─────────────────────────────────────── */
hr {
    border: none;
    border-top: 1px solid var(--dtm-border);
    margin: 1rem 0;
}

/* ── Expander ────────────────────────────────────────────── */
[data-testid="stExpander"] summary {
    font-size: 0.88rem;
    font-weight: 500;
    color: var(--dtm-mid-blue);
}
[data-testid="stExpander"] summary:hover {
    color: var(--dtm-dark-blue);
}

/* ── Dataframe header ────────────────────────────────────── */
[data-testid="stDataFrame"] th {
    background-color: var(--dtm-dark-blue) !important;
    color: #FFFFFF !important;
    font-weight: 600;
    font-size: 0.82rem;
}

/* ── Progress bar ────────────────────────────────────────── */
[data-testid="stProgressBar"] > div > div {
    background-color: var(--dtm-mid-blue);
}

/* ── Success / info / error banners ─────────────────────── */
[data-testid="stAlert"][data-baseweb="notification"][kind="positive"] {
    border-left: 4px solid #375623;
    background-color: #C6EFCE44;
}
[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
    border-left: 4px solid var(--dtm-mid-blue);
    background-color: var(--dtm-light-blue);
}

/* ── Toggle / checkbox ───────────────────────────────────── */
[data-testid="stToggle"] span[data-checked="true"] {
    background-color: var(--dtm-mid-blue) !important;
}

/* ── Text inputs ─────────────────────────────────────────── */
[data-testid="stTextInput"] input {
    border-radius: 4px;
    border-color: var(--dtm-border);
    font-size: 0.88rem;
}
[data-testid="stTextInput"] input:focus {
    border-color: var(--dtm-mid-blue);
    box-shadow: 0 0 0 2px rgba(46, 87, 151, 0.15);
}

/* ── Slider ──────────────────────────────────────────────── */
[data-testid="stSlider"] [data-baseweb="slider"] [role="slider"] {
    background-color: var(--dtm-mid-blue);
}

/* ── Hide Streamlit branding ─────────────────────────────── */
#MainMenu { visibility: hidden; }
footer    { visibility: hidden; }
header    { visibility: hidden; }
"""


def inject_css() -> None:
    """Inject the CUSTOM_CSS block into the Streamlit app."""
    st.markdown(f"<style>{CUSTOM_CSS}</style>", unsafe_allow_html=True)
