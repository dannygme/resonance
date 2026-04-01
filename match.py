"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

match.py
Cosine similarity scoring, section-level breakdown, and gap analysis.
"""

import re
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocess import preprocess
from embed import get_embedding, embed_sections, get_embeddings_batch

_SECTION_WEIGHTS = {"skills": 0.45, "experience": 0.35, "education": 0.20}
_MATCH_THRESHOLD = 0.68

_NOISE = {
    "ability", "able", "abilities", "work", "working", "experience", "experienced",
    "strong", "good", "great", "excellent", "knowledge", "understanding",
    "including", "using", "use", "used", "provide", "support", "help",
    "team", "role", "position", "candidate", "applicant", "person",
    "ksas", "ksa", "accountability", "competency", "competencies",
    "meets", "meet", "build", "builds", "demonstrate", "demonstrates",
    "year", "years", "month", "months", "day", "days", "time", "hours",
    "hour", "schedule", "shift", "full", "part",
    "location", "remote", "hybrid", "office", "based", "flexible",
    "salary", "compensation", "benefits", "opportunity", "opportunities",
    "please", "apply", "application", "cover", "letter", "resume", "cv",
    "equal", "employer", "diversity", "inclusion", "accommodate",
    "fast", "paced", "environment", "dynamic", "growing", "busy",
    "startup", "collaborative", "motivated", "driven", "passionate",
    "multiple", "various", "manage", "managing", "efforts", "effort",
    "functional", "cross", "high", "level", "key", "main", "primary",
    "pm", "am", "et", "est", "pst", "gmt",
}

_NOISE_PATTERN = re.compile(
    r"^\d+$"
    r"|^\d{1,2}[:/]\d{2}"
    r"|^\d{4}$"
    r"|^.{1,2}$"
)


def cosine_score(a: np.ndarray, b: np.ndarray) -> float:
    if a.sum() == 0 or b.sum() == 0:
        return 0.0
    return float(cosine_similarity(a.reshape(1, -1), b.reshape(1, -1))[0][0])


def score_to_pct(score: float) -> int:
    remapped = (score - 0.20) / (0.95 - 0.20)
    return max(0, min(100, round(remapped * 100)))


def score_sections(
    jd_sections: dict[str, np.ndarray],
    resume_sections: dict[str, np.ndarray],
) -> dict[str, int]:
    return {
        sec: score_to_pct(cosine_score(jd_sections[sec], resume_sections[sec]))
        for sec in _SECTION_WEIGHTS
    }


def weighted_section_score(section_scores: dict[str, int]) -> int:
    return round(sum(section_scores[s] * _SECTION_WEIGHTS[s] for s in _SECTION_WEIGHTS))


def _extract_keywords(text: str, top_n: int = 20) -> list[str]:
    if not text.strip():
        return []

    sentences = [s.strip() for s in re.split(r"[.\n•\-]", text) if len(s.strip()) > 10]
    if len(sentences) < 3:
        sentences = [text]

    vec = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        max_features=500,
        min_df=1,
        token_pattern=r"(?u)\b[a-zA-Z][a-zA-Z0-9+#./\-]{2,}\b",
    )
    try:
        tfidf_matrix = vec.fit_transform(sentences)
    except ValueError:
        return []

    scores = np.asarray(tfidf_matrix.sum(axis=0)).flatten()
    terms = vec.get_feature_names_out()
    ranked = sorted(zip(terms, scores), key=lambda x: -x[1])

    results = []
    for term, _ in ranked:
        words = term.lower().split()
        if any(w in _NOISE or _NOISE_PATTERN.match(w) for w in words):
            continue
        if len(words) == 2 and sum(1 for w in words if w not in _NOISE) < 1:
            continue
        results.append(term)
        if len(results) >= top_n:
            break

    return results


def _keyword_match(keyword: str, resume_text: str) -> float | None:
    if keyword.lower() in resume_text.lower():
        return 1.0
    return None


def gap_analysis(jd_text: str, resume_text: str, top_n: int = 20) -> dict:
    keywords = _extract_keywords(jd_text, top_n=top_n)
    if not keywords:
        return {"strong_matches": [], "potential_gaps": [], "all_terms": []}

    results = []
    needs_embedding = []
    for kw in keywords:
        score = _keyword_match(kw, resume_text)
        if score is not None:
            results.append((kw, score))
        else:
            needs_embedding.append(kw)

    if needs_embedding:
        all_texts = needs_embedding + [resume_text]
        embs = get_embeddings_batch(all_texts)
        kw_embs = embs[:-1]
        resume_emb = embs[-1]
        for kw, emb in zip(needs_embedding, kw_embs):
            results.append((kw, round(cosine_score(emb, resume_emb), 3)))

    results.sort(key=lambda x: -x[1])

    return {
        "strong_matches": [(p, s) for p, s in results if s >= _MATCH_THRESHOLD],
        "potential_gaps":  [(p, s) for p, s in results if s < _MATCH_THRESHOLD],
        "all_terms":       results,
    }


def analyse(jd_raw: str, resume_raw: str) -> dict:
    jd_pp     = preprocess(jd_raw)
    resume_pp = preprocess(resume_raw)

    jd_emb     = get_embedding(jd_pp["full"])
    resume_emb = get_embedding(resume_pp["full"])

    jd_sec_embs     = embed_sections(jd_pp["sections"],     jd_pp["full"])
    resume_sec_embs = embed_sections(resume_pp["sections"], resume_pp["full"])

    overall_pct    = score_to_pct(cosine_score(jd_emb, resume_emb))
    section_scores = score_sections(jd_sec_embs, resume_sec_embs)
    weighted_pct   = weighted_section_score(section_scores)
    final_score    = round(0.40 * overall_pct + 0.60 * weighted_pct)

    gaps = gap_analysis(jd_pp["full"], resume_pp["full"])

    if final_score >= 75:   label = "Strong Match"
    elif final_score >= 55: label = "Moderate Match"
    elif final_score >= 35: label = "Partial Match"
    else:                   label = "Weak Match"

    return {
        "overall_score":  overall_pct,
        "section_scores": section_scores,
        "weighted_score": weighted_pct,
        "final_score":    final_score,
        "gaps":           gaps,
        "label":          label,
    }