"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

discover.py
Semantic role discovery -- finds roles closest to a resume profile
using pre-computed embeddings of the role taxonomy.
All processing is local. No external APIs.
"""

import numpy as np
from functools import lru_cache
from sklearn.metrics.pairwise import cosine_similarity

from embed import get_embedding, get_embeddings_batch, DEFAULT_MODEL
from preprocess import clean_text
from roles_taxonomy import ROLES


@lru_cache(maxsize=1)
def _role_embeddings(model_name: str = DEFAULT_MODEL):
    titles  = [r[0] for r in ROLES]
    descs   = [r[1] for r in ROLES]
    matrix  = get_embeddings_batch(descs, model_name)
    return titles, descs, matrix


def discover_roles(
    resume_raw: str,
    top_n: int = 8,
    model_name: str = DEFAULT_MODEL,
) -> list[dict]:
    resume_clean = clean_text(resume_raw)
    resume_emb   = get_embedding(resume_clean, model_name).reshape(1, -1)

    titles, descs, matrix = _role_embeddings(model_name)

    sims    = cosine_similarity(resume_emb, matrix)[0]
    top_idx = np.argsort(sims)[::-1][:top_n]

    results = []
    for idx in top_idx:
        raw = float(sims[idx])
        pct = max(0, min(100, round((raw - 0.20) / (0.95 - 0.20) * 100)))
        results.append({
            "title":       titles[idx],
            "description": descs[idx],
            "score":       pct,
            "jd_text":     _build_jd(titles[idx], descs[idx]),
        })
    return results


def _build_jd(title: str, description: str) -> str:
    return (
        f"Role: {title}\n\n"
        f"About the role:\n{description}\n\n"
        f"We are looking for a {title} to join our team. "
        f"The ideal candidate will bring relevant experience and skills "
        f"aligned with the responsibilities described above."
    )