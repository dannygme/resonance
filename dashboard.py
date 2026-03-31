"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026
Local-first. Privacy-preserving. No data leaves your machine.
"""

import streamlit as st
import datetime
import pandas as pd
from match import analyse
from discover import discover_roles

st.set_page_config(page_title="Resonance.exe", page_icon=None, layout="centered",
                   initial_sidebar_state="collapsed")

for k, v in [
    ("active_window",    "discover"),
    ("resume_text",      ""),
    ("prefill_jd",       ""),
    ("prefill_role",     ""),
    ("discovered_roles", None),
    ("expanded_cards",   set()),
    ("start_menu_open",  False),
    ("incognito",        False),
    ("show_key",         False),
    ("reveal_key",       {}),
    ("screen_df",        None),
]:
    if k not in st.session_state:
        st.session_state[k] = v

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');

html, body, [class*="css"], .stApp {
    background: #008080 !important;
    color: #000 !important;
    font-family: 'MS Sans Serif', Tahoma, Arial, sans-serif !important;
    font-size: 13px !important;
}
.block-container {
    padding: 10px 10px 80px !important;
    max-width: 860px !important;
}
#MainMenu, footer, header { visibility: hidden; }
.stDeployButton { display: none; }
div[data-testid="column"] { padding: 0 4px !important; }

.stApp::before {
    content: '';
    position: fixed; inset: 0;
    background-image: radial-gradient(circle, #009090 1px, transparent 1px);
    background-size: 16px 16px;
    opacity: 0.18;
    pointer-events: none; z-index: 0;
}

.win-window {
    background: #c0c0c0;
    box-shadow: inset 1px 1px #fff, inset -1px -1px #808080,
                inset 2px 2px #dfdfdf, inset -2px -2px #404040, 3px 3px 0 #000;
    margin-bottom: 10px; width: 100%; box-sizing: border-box;
    animation: wopen .12s ease-out;
}
@keyframes wopen {
    from { transform: scale(.96) translateY(5px); opacity:.5; }
    to   { transform: scale(1) translateY(0); opacity:1; }
}
.win-titlebar {
    background: linear-gradient(90deg,#000080,#1084d0);
    color:#fff; font-size:12px; font-weight:bold;
    padding:3px 6px 3px 8px;
    display:flex; align-items:center; justify-content:space-between; user-select:none;
}
.win-titlebar-btns { display:flex; gap:2px; }
.win-titlebar-btn {
    width:16px; height:14px; background:#c0c0c0;
    box-shadow:inset 1px 1px #fff,inset -1px -1px #808080;
    display:flex; align-items:center; justify-content:center;
    font-size:9px; color:#000; font-weight:bold;
}
.win-body { padding:10px 12px 12px; }

textarea, .stTextArea textarea {
    background:#fff !important; border:none !important;
    box-shadow: inset 1px 1px #808080, inset -1px -1px #fff,
                inset 2px 2px #404040, inset -2px -2px #dfdfdf !important;
    border-radius:0 !important; color:#000 !important;
    font-family:'MS Sans Serif',Arial,sans-serif !important;
    font-size:12px !important; line-height:1.5 !important;
    padding:4px 6px !important; width:100% !important;
    box-sizing:border-box !important; resize:vertical !important;
}
textarea::placeholder { color:#808080 !important; }

.stButton > button {
    background:#c0c0c0 !important; color:#000 !important;
    border:none !important; border-radius:0 !important;
    font-family:'MS Sans Serif',Arial,sans-serif !important;
    font-size:12px !important; font-weight:normal !important;
    padding:4px 16px !important; min-height:26px !important;
    box-shadow: inset 1px 1px #fff, inset -1px -1px #808080,
                inset 2px 2px #dfdfdf, inset -2px -2px #404040 !important;
    transition:none !important; cursor:pointer !important; white-space:nowrap !important;
}
.stButton > button:hover { background:#d4d0c8 !important; }
.stButton > button:active {
    box-shadow: inset 1px 1px #808080, inset -1px -1px #fff,
                inset 2px 2px #404040, inset -2px -2px #dfdfdf !important;
}
.stButton > button[kind="primary"] { font-weight:bold !important; }
.stButton > button:disabled { color:#808080 !important; }

.field-label { font-size:11px; font-weight:bold; color:#000080; text-transform:uppercase; letter-spacing:.07em; margin-bottom:4px; }
.notice { background:#ffffc0; box-shadow:inset 1px 1px #808080,inset -1px -1px #fff; padding:6px 10px; font-size:11px; color:#000; line-height:1.55; margin-bottom:10px; }
.role-card { background:#c0c0c0; box-shadow:inset 1px 1px #fff,inset -1px -1px #808080,inset 2px 2px #dfdfdf,inset -2px -2px #404040; margin-bottom:8px; width:100%; box-sizing:border-box; }
.role-card-titlebar { background:#000080; color:#fff; font-size:11px; font-weight:bold; padding:2px 8px; display:flex; align-items:center; justify-content:space-between; }
.role-card-body { padding:8px 10px; }
.role-card-desc { font-size:11px; color:#000; line-height:1.55; margin-bottom:6px; }
.score-hero { background:#c0c0c0; box-shadow:inset 1px 1px #fff,inset -1px -1px #808080,inset 2px 2px #dfdfdf,inset -2px -2px #404040; margin-bottom:10px; width:100%; }
.score-hero-titlebar { background:#000080; color:#fff; font-size:11px; font-weight:bold; padding:2px 8px; }
.score-hero-body { padding:12px 16px 14px; text-align:center; }
.score-number { font-family:'VT323',monospace; font-size:5rem; color:#000080; line-height:1; margin-bottom:4px; }
.score-chip { display:inline-block; font-size:11px; font-weight:bold; padding:2px 10px; box-shadow:inset 1px 1px #fff,inset -1px -1px #808080; background:#c0c0c0; }
.chip-strong { color:#000080; } .chip-moderate,.chip-partial { color:#804000; } .chip-weak { color:#800000; }
.breakdown-card { background:#c0c0c0; box-shadow:inset 1px 1px #fff,inset -1px -1px #808080,inset 2px 2px #dfdfdf,inset -2px -2px #404040; text-align:center; width:100%; }
.breakdown-card-title { background:#000080; color:#fff; font-size:10px; font-weight:bold; padding:2px 4px; }
.breakdown-card-body { padding:8px 4px; }
.breakdown-score { font-family:'VT323',monospace; font-size:2.4rem; line-height:1; }
.score-high { color:#000080; } .score-mid { color:#804000; } .score-low { color:#800000; }
.chips-row { display:flex; flex-wrap:wrap; gap:4px; margin-bottom:6px; }
.chip { font-size:11px; padding:1px 8px; background:#c0c0c0; color:#000; box-shadow:inset 1px 1px #fff,inset -1px -1px #808080; }
.chip-match { background:#c0ffc0; color:#005000; box-shadow:inset 1px 1px #80ff80,inset -1px -1px #408040; }
.chip-gap   { background:#ffc0c0; color:#500000; box-shadow:inset 1px 1px #ff8080,inset -1px -1px #804040; }
.chip-neutral { background:#c0c0c0; color:#000; }
.why-panel { background:#fff; box-shadow:inset 1px 1px #808080,inset -1px -1px #fff; padding:8px 10px; margin-top:4px; }
.why-panel-heading { font-size:10px; font-weight:bold; color:#000080; text-transform:uppercase; letter-spacing:.08em; margin-bottom:6px; }
.stProgress > div > div { background:#000080 !important; border-radius:0 !important; height:14px !important; }
.stProgress > div { background:#fff !important; border-radius:0 !important; height:14px !important; box-shadow:inset 1px 1px #808080,inset -1px -1px #fff !important; }
.streamlit-expanderHeader { background:#c0c0c0 !important; color:#000 !important; font-family:'MS Sans Serif',Arial,sans-serif !important; font-size:12px !important; font-weight:bold !important; border:none !important; border-radius:0 !important; box-shadow:inset 1px 1px #fff,inset -1px -1px #808080 !important; }
.streamlit-expanderContent { background:#c0c0c0 !important; border:none !important; }
.divider { border:none; border-top:1px solid #808080; border-bottom:1px solid #fff; margin:8px 0; }
.footnote { font-size:10px; color:#444; text-align:center; margin-top:8px; }
</style>
""", unsafe_allow_html=True)


def score_color_class(v):
    return "score-high" if v >= 65 else ("score-mid" if v >= 40 else "score-low")

def score_ring_svg(val, size=44):
    r = 16; circ = 2*3.14159*r; fill = (val/100)*circ
    color = "#000080" if val >= 65 else ("#804000" if val >= 40 else "#800000")
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 40 40">'
            f'<circle cx="20" cy="20" r="{r}" fill="#fff" stroke="#808080" stroke-width="1"/>'
            f'<circle cx="20" cy="20" r="{r}" fill="none" stroke="{color}" stroke-width="4"'
            f' stroke-dasharray="{fill:.1f} {circ:.1f}" stroke-linecap="butt"'
            f' transform="rotate(-90 20 20)"/>'
            f'<text x="20" y="20" text-anchor="middle" dominant-baseline="central"'
            f' font-family="VT323,monospace" font-size="11" font-weight="bold"'
            f' fill="{color}">{val}%</text></svg>')

clock_str = datetime.datetime.now().strftime("%I:%M %p")


@st.dialog("README.TXT -- Resonance.exe")
def show_readme():
    st.markdown("""
    <style>
    div[data-testid="stDialog"] > div > div {
        background: #c0c0c0 !important;
        border: none !important;
        box-shadow: inset 1px 1px #fff, inset -1px -1px #808080,
                    inset 2px 2px #dfdfdf, inset -2px -2px #404040,
                    4px 4px 0 #000 !important;
        border-radius: 0 !important;
        padding: 0 !important;
    }
    div[data-testid="stDialog"] h2 {
        background: linear-gradient(90deg, #000080, #1084d0) !important;
        color: #fff !important;
        font-family: 'MS Sans Serif', Arial, sans-serif !important;
        font-size: 12px !important;
        font-weight: bold !important;
        padding: 4px 8px !important;
        margin: 0 !important;
        border-radius: 0 !important;
    }
    div[data-testid="stDialog"] p,
    div[data-testid="stDialog"] li {
        font-family: 'MS Sans Serif', Arial, sans-serif !important;
        font-size: 12px !important;
        color: #000 !important;
        line-height: 1.6 !important;
    }
    div[data-testid="stDialog"] strong { color: #000080 !important; }
    div[data-testid="stDialog"] button[data-testid="stBaseButton-headerNoPadding"] {
        background: #c0c0c0 !important;
        color: #000 !important;
        border: none !important;
        box-shadow: inset 1px 1px #fff, inset -1px -1px #808080 !important;
        border-radius: 0 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
**What is Resonance?**
A fully local, privacy-first resume-to-job matching system built by Danny Greene.
No data ever leaves your machine. No APIs, no cloud processing, no storage.

**Discover Roles**
Paste your resume and click Find Roles. The system compares your profile
semantically against a curated taxonomy of ~55 role descriptions.
- Scores reflect semantic similarity, not keyword overlap
- Click Why this? to see key terms for a role
- Click Analyse Fit to run a deeper match against a real job description

**Match to Job Description**
Paste any job description alongside your resume and click Analyse Match.
- Overall score: full document cosine similarity
- Section scores: Skills 45%, Experience 35%, Education 20%
- Final score: 40% overall + 60% section-weighted blend
- Insights: key phrases from the job description scored against your resume

**Screen Applicants**
Upload multiple resumes (PDF or TXT) and a job description.
All candidates are scored and ranked locally.
- Enable Bias Reduction Mode to anonymize applicant identities before scoring
- Reveal the identity key after shortlisting to reduce unconscious bias
- Export results as CSV with the identity key included
                                
**Scoring Guide**
- 75-100%: Strong Match
- 55-74%: Moderate Match
- 35-54%: Partial Match
- 0-34%: Weak Match

**Privacy**
Zero data retention. All processing runs in memory on your machine.
The embedding model (~80 MB) is cached locally after first download.
    """)


win_title = (
    f"Fit Analysis: {st.session_state.prefill_role}"
    if st.session_state.active_window == "matcher" and st.session_state.prefill_role
    else ("Discover Roles" if st.session_state.active_window == "discover"
          else "Match to Job Description")
)
st.markdown(f"""
<div class="win-window">
  <div class="win-titlebar">
    <span>Resonance.exe -- {win_title}</span>
    <div class="win-titlebar-btns">
      <div class="win-titlebar-btn">_</div>
      <div class="win-titlebar-btn">&#9633;</div>
      <div class="win-titlebar-btn">&#10005;</div>
    </div>
  </div>
</div>
""", unsafe_allow_html=True)


if st.session_state.active_window == "discover":

    st.markdown("""
    <div class="win-window">
      <div class="win-titlebar">
        <span>Find Roles Matching Your Profile</span>
        <div class="win-titlebar-btns">
          <div class="win-titlebar-btn">_</div>
          <div class="win-titlebar-btn">&#9633;</div>
        </div>
      </div>
      <div class="win-body">
        <p style="margin:0;font-size:12px;">Paste your resume below. The system maps your
        profile semantically across a curated role taxonomy, surfacing strong fits including
        roles you may not have considered.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<div class='field-label'>Resume text</div>", unsafe_allow_html=True)
    resume_input = st.text_area(
        label="r_discover", value=st.session_state.resume_text,
        height=180, placeholder="Paste your full resume text here...",
        label_visibility="collapsed",
    )
    rc, _ = st.columns([1, 4])
    with rc:
        discover_run = st.button("Find Roles", key="discover_btn", type="primary",
                                 disabled=not resume_input.strip())

    if discover_run:
        st.session_state.resume_text = resume_input
        with st.spinner("Analysing profile..."):
            st.session_state.discovered_roles = discover_roles(resume_input, top_n=8)
        st.session_state.expanded_cards = set()

    if st.session_state.discovered_roles:
        roles = st.session_state.discovered_roles
        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='field-label'>Results</div>", unsafe_allow_html=True)
        st.markdown("""
        <div class="notice"><b>Note:</b> Discovery scores compare your resume against a short
        role description. Clicking <b>Analyse Fit</b> recalculates against a full job
        description -- some variance is expected.</div>
        """, unsafe_allow_html=True)

        for i, role in enumerate(roles):
            ring = score_ring_svg(role["score"], size=40)
            st.markdown(f"""
            <div class="role-card">
              <div class="role-card-titlebar">
                <span>{role['title']}</span>
                <span style="font-family:VT323,monospace;font-size:14px;">{role['score']}% match</span>
              </div>
              <div class="role-card-body">
                <div style="display:flex;align-items:flex-start;gap:10px;">
                  <div style="flex-shrink:0;margin-top:2px;">{ring}</div>
                  <div class="role-card-desc">{role['description']}</div>
                </div>
              </div>
            </div>
            """, unsafe_allow_html=True)

            c1, c2, _ = st.columns([1, 1, 3])
            with c1:
                if st.button("Analyse Fit", key=f"fit_{i}", type="primary"):
                    st.session_state.prefill_jd    = role["jd_text"]
                    st.session_state.prefill_role  = role["title"]
                    st.session_state.active_window = "matcher"
                    st.rerun()
            with c2:
                exp = i in st.session_state.expanded_cards
                if st.button("Hide" if exp else "Why this?", key=f"why_{i}"):
                    if exp: st.session_state.expanded_cards.discard(i)
                    else:   st.session_state.expanded_cards.add(i)
                    st.rerun()

            if i in st.session_state.expanded_cards:
                dw = [w.strip(".,()").lower() for w in role["description"].split() if len(w) > 4]
                chips_html = "".join(f"<span class='chip chip-neutral'>{w}</span>"
                                      for w in list(dict.fromkeys(dw))[:12])
                st.markdown(f"""
                <div class="why-panel">
                  <div class="why-panel-heading">Key areas this role covers</div>
                  <div class="chips-row">{chips_html}</div>
                  <div style="font-size:11px;color:#444;margin-top:6px;line-height:1.5;">
                    Paste a real job description and click Analyse Fit for specific matches and gaps.
                  </div>
                </div>
                """, unsafe_allow_html=True)

        st.markdown("<div class='footnote'>Scores reflect semantic similarity only.</div>",
                    unsafe_allow_html=True)


elif st.session_state.active_window == "matcher":

    st.markdown("""
    <div class="win-window">
      <div class="win-titlebar">
        <span>Match Resume to Job Description</span>
        <div class="win-titlebar-btns">
          <div class="win-titlebar-btn">_</div>
          <div class="win-titlebar-btn">&#9633;</div>
        </div>
      </div>
      <div class="win-body">
        <p style="margin:0;font-size:12px;">Semantic analysis across skills, experience, and
        education. Paste the full job posting for the most accurate results.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    col_jd, col_res = st.columns(2, gap="small")
    with col_jd:
        st.markdown("<div class='field-label'>Job Description</div>", unsafe_allow_html=True)
        jd_text = st.text_area(
            label="jd", value=st.session_state.prefill_jd,
            height=220, placeholder="Paste the full job posting here...",
            label_visibility="collapsed",
        )
    with col_res:
        st.markdown("<div class='field-label'>Resume</div>", unsafe_allow_html=True)
        resume_text = st.text_area(
            label="resume_match", value=st.session_state.resume_text,
            height=220, placeholder="Paste your resume here...",
            label_visibility="collapsed",
        )

    _, bc, _ = st.columns([2, 2, 2])
    with bc:
        run = st.button("Analyse Match", key="match_btn", type="primary",
                        disabled=not (jd_text.strip() and resume_text.strip()))

    if run:
        st.session_state.prefill_jd   = ""
        st.session_state.prefill_role = ""
        st.session_state.resume_text  = resume_text
        with st.spinner("Running semantic analysis..."):
            result = analyse(jd_text, resume_text)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)

        chip_cls = {"Strong Match":"chip-strong","Moderate Match":"chip-moderate",
                    "Partial Match":"chip-partial","Weak Match":"chip-weak"}.get(
                        result["label"],"chip-partial")

        st.markdown(f"""
        <div class="score-hero">
          <div class="score-hero-titlebar">Analysis Result</div>
          <div class="score-hero-body">
            <div class="score-number">{result['final_score']}%</div>
            <div><span class="score-chip {chip_cls}">{result['label']}</span></div>
          </div>
        </div>
        """, unsafe_allow_html=True)
        st.progress(result["final_score"] / 100)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='field-label'>Section Breakdown</div>", unsafe_allow_html=True)

        sc = result["section_scores"]
        b1, b2, b3 = st.columns(3, gap="small")
        for col, (lbl, val) in zip([b1,b2,b3],
            [("Skills",sc["skills"]),("Experience",sc["experience"]),("Education",sc["education"])]):
            with col:
                ring  = score_ring_svg(val, size=44)
                css_c = score_color_class(val)
                st.markdown(f"""
                <div class="breakdown-card">
                  <div class="breakdown-card-title">{lbl}</div>
                  <div class="breakdown-card-body">
                    <div style="display:flex;align-items:center;justify-content:center;gap:6px;">
                      {ring}<div class="breakdown-score {css_c}">{val}%</div>
                    </div>
                  </div>
                </div>
                """, unsafe_allow_html=True)
            st.progress(val / 100)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='field-label'>Insights</div>", unsafe_allow_html=True)

        ins1, ins2 = st.columns(2, gap="small")
        with ins1:
            st.markdown("<div style='font-size:11px;font-weight:bold;color:#005000;margin-bottom:4px;'>Strong Alignment</div>", unsafe_allow_html=True)
            matches = result["gaps"]["strong_matches"]
            if matches:
                mc = "".join(f"<span class='chip chip-match'>{p} &nbsp;{round(s*100)}%</span>"
                             for p,s in matches[:10])
                st.markdown(f"<div class='chips-row'>{mc}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='font-size:11px;color:#444;'>No strong alignments found.</span>", unsafe_allow_html=True)

        with ins2:
            st.markdown("<div style='font-size:11px;font-weight:bold;color:#500000;margin-bottom:4px;'>Potential Gaps</div>", unsafe_allow_html=True)
            gaps = result["gaps"]["potential_gaps"]
            if gaps:
                gc = "".join(f"<span class='chip chip-gap'>{p} &nbsp;{round(s*100)}%</span>"
                             for p,s in gaps[:10])
                st.markdown(f"<div class='chips-row'>{gc}</div>", unsafe_allow_html=True)
            else:
                st.markdown("<span style='font-size:11px;color:#005000;'>No significant gaps.</span>", unsafe_allow_html=True)

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        with st.expander("Scoring Methodology"):
            st.markdown("""
**Formula:** `final = 0.40 x overall + 0.60 x weighted_sections`

Sections: Skills 45% / Experience 35% / Education 20%

| Score | Label | Meaning |
|---|---|---|
| 75-100% | Strong Match | Resume closely mirrors the job description. |
| 55-74% | Moderate Match | Good alignment; targeted additions would help. |
| 35-54% | Partial Match | Noticeable gaps. Tailor before applying. |
| 0-34% | Weak Match | Significant mismatch. |
            """)
        st.markdown("<div class='footnote'>All processing is local. No text leaves your machine.</div>",
                    unsafe_allow_html=True)


elif st.session_state.active_window == "screen":
    from batch import screen_applicants, extract_text

    incognito = st.session_state.incognito
    win_label = "Screen Applicants -- Bias Reduction Mode" if incognito else "Screen Applicants"

    st.markdown(f"""
    <div class="win-window">
      <div class="win-titlebar" style="{'background:linear-gradient(90deg,#2d0060,#6b00b3);' if incognito else ''}">
        <span>{win_label}</span>
        <div class="win-titlebar-btns">
          <div class="win-titlebar-btn">_</div>
          <div class="win-titlebar-btn">&#9633;</div>
        </div>
      </div>
      <div class="win-body">
        <p style="margin:0;font-size:12px;">Upload resumes and a job description.
        All applicants are scored and ranked locally.
        Enable Bias Reduction Mode to strip names, emails, and other identifying
        details before analysis.</p>
      </div>
    </div>
    """, unsafe_allow_html=True)

    incog_col, _ = st.columns([2, 5])
    with incog_col:
        if st.button(
            "Bias Reduction Mode: ON" if incognito else "Bias Reduction Mode: OFF",
            key="incog_toggle",
            type="primary" if incognito else "secondary",
        ):
            st.session_state.incognito = not incognito
            st.rerun()

    if incognito:
        st.markdown("""
        <div class="notice">
          Bias Reduction Mode is active. Names, emails, phone numbers, addresses,
          and graduation years will be stripped before analysis.
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<div class='field-label'>Job Description</div>", unsafe_allow_html=True)
    jd_input = st.text_area(
        label="jd_batch", height=160,
        placeholder="Paste the job description here...",
        label_visibility="collapsed",
    )

    st.markdown("<div class='field-label'>Upload Resumes (PDF or TXT)</div>",
                unsafe_allow_html=True)
    uploaded = st.file_uploader(
        label="resumes",
        type=["pdf", "txt"],
        accept_multiple_files=True,
        label_visibility="collapsed",
    )

    run_col, _ = st.columns([1, 4])
    with run_col:
        run_batch = st.button(
            "Screen", key="screen_btn", type="primary",
            disabled=not (jd_input.strip() and uploaded),
        )

    if run_batch:
        resumes = {f.name: extract_text(f) for f in uploaded}
        resumes = {k: v for k, v in resumes.items() if v.strip()}
        if not resumes:
            st.warning("Could not extract text from the uploaded files.")
        else:
            with st.spinner(f"Screening {len(resumes)} applicant(s)..."):
                df, reveal_key = screen_applicants(resumes, jd_input,
                                                   incognito=st.session_state.incognito)
                st.session_state.screen_df  = df
                st.session_state.reveal_key = reveal_key
                st.session_state.show_key   = False

    if st.session_state.screen_df is not None:
        df         = st.session_state.screen_df
        reveal_key = st.session_state.reveal_key

        st.markdown("<hr class='divider'>", unsafe_allow_html=True)
        st.markdown("<div class='field-label'>Results</div>", unsafe_allow_html=True)
        st.dataframe(df, use_container_width=True)

        if st.session_state.incognito and reveal_key:
            st.markdown("<hr class='divider'>", unsafe_allow_html=True)
            if st.button("Reveal Identity Key", key="reveal_btn"):
                st.session_state.show_key = not st.session_state.show_key
                st.rerun()
            if st.session_state.show_key:
                key_df = pd.DataFrame(
                    list(reveal_key.items()),
                    columns=["Rank + Code", "File"]
                )
                key_df.index = range(1, len(key_df) + 1)
                st.markdown("<div class='field-label'>Identity Key</div>",
                            unsafe_allow_html=True)
                st.dataframe(key_df, use_container_width=True)

        if st.session_state.incognito and reveal_key:
            key_rows = pd.DataFrame(
                list(reveal_key.items()),
                columns=["Rank + Code", "File"]
            )
            csv = df.to_csv(index_label="Rank") + "\n\nIdentity Key\n" + key_rows.to_csv(index=False)
        else:
            csv = df.to_csv(index_label="Rank")

        st.download_button(
            "Export CSV", csv,
            file_name="screening_results.csv",
            mime="text/csv",
            key="export_csv",
        )


st.markdown("""
<div style="
    margin-top: 20px;
    border-top: 2px solid #808080;
    border-bottom: 2px solid #ffffff;
    background: transparent;
    margin-bottom: 6px;
"></div>
""", unsafe_allow_html=True)

col_l, col1, col2, col3, col4, col_r = st.columns([1, 1, 2, 3, 2, 1])
with col1:
    if st.button("Start", key="tb_readme"):
        show_readme()
with col2:
    if st.button("Discover Roles", key="tb_discover"):
        st.session_state.active_window   = "discover"
        st.session_state.start_menu_open = False
        st.rerun()
with col3:
    if st.button("Match to Job Description", key="tb_matcher"):
        st.session_state.active_window   = "matcher"
        st.session_state.start_menu_open = False
        st.rerun()
with col4:
    if st.button("Screen Applicants", key="tb_screen"):
        st.session_state.active_window   = "screen"
        st.session_state.start_menu_open = False
        st.rerun()


st.markdown("""
<style>
@keyframes hamster-walk {
    0%   { left: 12%; }
    45%  { left: 82%; }
    50%  { left: 82%; }
    95%  { left: 12%; }
    100% { left: 12%; }
}
@keyframes hamster-flip {
    0%,45%  { transform: scaleX(1); }
    50%,95% { transform: scaleX(-1); }
    100%    { transform: scaleX(1); }
}
@keyframes bob {
    0%,100% { margin-bottom: 0px; }
    50%     { margin-bottom: 3px; }
}
@keyframes doc-wave {
    0%,100% { transform: rotate(-4deg); }
    50%     { transform: rotate(4deg); }
}
@keyframes building-pulse {
    0%,100% { opacity: 1; }
    50%     { opacity: 0.85; }
}
.hamster-scene {
    position: relative;
    width: 100%;
    height: 52px;
    margin-top: 8px;
    margin-bottom: 4px;
    overflow: visible;
}
.sprite-resume {
    position: absolute; left: 4%; bottom: 0;
    text-align: center; pointer-events: none;
    animation: doc-wave 2.5s ease-in-out infinite;
    transform-origin: bottom center;
}
.sprite-resume .icon { font-size: 26px; line-height: 1; display: block; }
.sprite-resume .lbl {
    font-family: 'MS Sans Serif', Arial, sans-serif;
    font-size: 8px; color: #fff; display: block; margin-top: 1px;
    text-shadow: 1px 1px #000,-1px -1px #000,1px -1px #000,-1px 1px #000;
    white-space: nowrap;
}
.sprite-company {
    position: absolute; right: 4%; bottom: 0;
    text-align: center; pointer-events: none;
    animation: building-pulse 3s ease-in-out infinite;
}
.sprite-company .icon { font-size: 26px; line-height: 1; display: block; }
.sprite-company .lbl {
    font-family: 'MS Sans Serif', Arial, sans-serif;
    font-size: 8px; color: #fff; display: block; margin-top: 1px;
    text-shadow: 1px 1px #000,-1px -1px #000,1px -1px #000,-1px 1px #000;
    white-space: nowrap;
}
.hamster-wrap {
    position: absolute; bottom: 4px; pointer-events: none;
    animation: hamster-walk 120s linear infinite;
}
.hamster-wrap .icon {
    font-size: 22px; line-height: 1; display: block;
    animation: hamster-flip 120s linear infinite, bob 0.5s ease-in-out infinite;
}
.hamster-wrap .lbl {
    font-family: 'MS Sans Serif', Arial, sans-serif;
    font-size: 8px; color: #fff; text-align: center; display: block;
    text-shadow: 1px 1px #000,-1px -1px #000,1px -1px #000,-1px 1px #000;
    white-space: nowrap; margin-top: 1px;
}
.hamster-path {
    position: absolute; bottom: 10px;
    left: 13%; right: 13%;
    border-bottom: 1px dashed rgba(255,255,255,0.25);
    pointer-events: none;
}
</style>

<div class="hamster-scene">
  <div class="sprite-resume">
    <span class="icon">&#x1F4C4;</span>
    <span class="lbl">resume.doc</span>
  </div>
  <div class="hamster-path"></div>
  <div class="hamster-wrap">
    <span class="icon">&#x1F439;</span>
    <span class="lbl">job_hamster.exe</span>
  </div>
  <div class="sprite-company">
    <span class="icon">&#x1F3E2;</span>
    <span class="lbl">company.exe</span>
  </div>
</div>
""", unsafe_allow_html=True)
