# DTM Survey Alignment Tool

Streamlit port of the `match_surveys()` / `export_alignment_excel()` R utility (v10).  
Matches IOM DTM survey XLSForms against the Global Data Kit and exports a colour-coded Excel diagnostic.

---

## File structure

```
dtm-alignment-tool/
├── app.py              # Streamlit UI
├── matcher.py          # Core matching logic (match_surveys)
├── exporter.py         # Excel export (export_alignment_excel → BytesIO)
├── requirements.txt
└── data/
    └── datakit.xlsx    # ← place your default Datakit here (sheet: myWorkSheet)
```

---

## Running locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## Deploying to Streamlit Cloud

1. Push this repo to GitHub (the `data/datakit.xlsx` file is committed with it).
2. Go to [share.streamlit.io](https://share.streamlit.io) → **New app**.
3. Select your repo, branch, and set **Main file path** to `app.py`.
4. Click **Deploy** — no other configuration needed.

---

## Updating the default Datakit

1. Export your updated Datakit from the DTM portal (sheet: `myWorkSheet`).
2. Replace `data/datakit.xlsx` in the repo.
3. Commit and push — Streamlit Cloud redeploys automatically.

Users can also **override** the default Datakit at any time via the sidebar upload.

---

## Matching logic

| Stage | Method | Label |
|-------|--------|-------|
| 1 | Exact key-field match | `100% (Key Field Match)` |
| 2 | Exact text-field match | `100% (Text Field Match)` |
| 3 | Jaro-Winkler fuzzy (threshold 0.20) | `NN% (Fuzzy Key/Text: …)` |

### AlignmentStatus values

| Status | Meaning |
|--------|---------|
| `LikelyAligned` | Exact match (key or text) |
| `NeedsVerification` | Fuzzy match — review recommended |
| `FPReview` | No match — focal point action required |
| `DiscouragedQuestion` | Matched Datakit entry is flagged Discouraged |
| `MissingCoreQuestion` | Core question in Datakit not present in survey |
| `DoesNotNeed2Align` | Structural XLSForm element — skipped |

---

## Excel output (3 sheets)

| Sheet | Contents |
|-------|----------|
| `Summary` | Dashboard metrics + colour legend |
| `Survey_Alignment_Diagnostics` | All rows, colour-coded by status |
| `Missing_BSA_Core` | Only `Missing*` rows |
