"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

match.py
Cosine similarity scoring, section-level breakdown, and gap analysis.
"""

import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

from preprocess import preprocess
from embed import get_embedding, embed_sections, get_embeddings_batch

_SECTION_WEIGHTS = {"skills": 0.45, "experience": 0.35, "education": 0.20}
_MATCH_THRESHOLD = 0.68


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


def _extract_keyphrases(text: str, top_n: int = 15) -> list[str]:
    if not text.strip():
        return []
    vec = TfidfVectorizer(
        ngram_range=(1, 2),
        stop_words="english",
        max_features=200,
        min_df=1,
    )
    try:
        vec.fit([text])
        scores = dict(zip(vec.get_feature_names_out(), vec.idf_))
        return sorted(scores, key=lambda t: -scores[t])[:top_n]
    except ValueError:
        return []


def gap_analysis(
    jd_text: str,
    resume_text: str,
    top_n: int = 15,
) -> dict:
    jd_phrases = _extract_keyphrases(jd_text, top_n=top_n)
    if not jd_phrases:
        return {"strong_matches": [], "potential_gaps": [], "all_terms": []}

    all_texts   = jd_phrases + [resume_text]
    embs        = get_embeddings_batch(all_texts)
    phrase_embs = embs[:-1]
    resume_emb  = embs[-1]

    results = [
        (p, round(cosine_score(e, resume_emb), 3))
        for p, e in zip(jd_phrases, phrase_embs)
    ]
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