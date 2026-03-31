"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

batch.py
Scores multiple resumes against a single job description.
Returns a ranked dataframe for display and CSV export.
"""

import pandas as pd
import hashlib
from anonymize import anonymize


def screen_applicants(
    resumes: dict[str, str],
    jd_raw: str,
    incognito: bool = False,
) -> tuple[pd.DataFrame, dict]:
    from match import analyse
    rows = []
    key = {}

    for i, (filename, raw) in enumerate(resumes.items()):
        text = anonymize(raw) if incognito else raw
        result = analyse(jd_raw, text)
        if incognito:
            h = hashlib.md5(filename.encode()).hexdigest()[:6].upper()
            code = f"Applicant-{h}"
        else:
            code = filename.rsplit(".", 1)[0]
        key[code] = filename
        rows.append({
            "Applicant":      code,
            "Doc Similarity": result["overall_score"],
            "Skills":         result["section_scores"]["skills"],
            "Experience":     result["section_scores"]["experience"],
            "Education":      result["section_scores"]["education"],
            "Final Score":    result["final_score"],
            "Verdict":        result["label"],
        })

    df = pd.DataFrame(rows)
    df = df.sort_values("Final Score", ascending=False).reset_index(drop=True)
    df.index = [f"#{i+1}" for i in range(len(df))]
    df.index.name = "Rank"

    if incognito:
        ranked_key = {}
        for rank_label, row in df.iterrows():
            code = row["Applicant"]
            ranked_key[f"{rank_label} {code}"] = key[code]
        df = df.drop(columns=["Applicant"])
        return df, ranked_key

    df.index = [f"#{i+1} {df.iloc[i]['Applicant']}" for i in range(len(df))]
    df = df.drop(columns=["Applicant"])
    return df, {}


def extract_text(file) -> str:
    name = file.name.lower()
    if name.endswith(".pdf"):
        try:
            import pdfplumber
            with pdfplumber.open(file) as pdf:
                return "\n".join(
                    page.extract_text() or "" for page in pdf.pages
                )
        except Exception:
            return ""
    else:
        return file.read().decode("utf-8", errors="ignore")