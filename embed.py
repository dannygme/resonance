"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

embed.py
Local sentence-transformer embeddings. No external APIs.
Model: all-MiniLM-L6-v2 (~80 MB, CPU-friendly, cached after first download).
"""
import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"

import numpy as np
from functools import lru_cache
from sentence_transformers import SentenceTransformer

DEFAULT_MODEL = "all-MiniLM-L6-v2"


@lru_cache(maxsize=1)
def _load_model(model_name: str = DEFAULT_MODEL) -> SentenceTransformer:
    return SentenceTransformer(model_name)


def get_embedding(text: str, model_name: str = DEFAULT_MODEL) -> np.ndarray:
    if not text or not text.strip():
        model = _load_model(model_name)
        dim = model.get_sentence_embedding_dimension()
        return np.zeros(dim, dtype=np.float32)
    model = _load_model(model_name)
    emb = model.encode(text, convert_to_numpy=True, normalize_embeddings=True)
    return emb.astype(np.float32)


def get_embeddings_batch(texts: list[str], model_name: str = DEFAULT_MODEL) -> np.ndarray:
    model = _load_model(model_name)
    embs = model.encode(
        texts,
        convert_to_numpy=True,
        normalize_embeddings=True,
        batch_size=32,
        show_progress_bar=False,
    )
    return embs.astype(np.float32)


def embed_sections(
    sections: dict[str, str],
    full_text: str = "",
    model_name: str = DEFAULT_MODEL,
) -> dict[str, np.ndarray]:
    fallback = get_embedding(full_text, model_name) if full_text.strip() else None
    result: dict[str, np.ndarray] = {}
    for k, v in sections.items():
        if v.strip():
            result[k] = get_embedding(v, model_name)
        elif fallback is not None:
            result[k] = fallback
        else:
            model = _load_model(model_name)
            result[k] = np.zeros(model.get_sentence_embedding_dimension(), dtype=np.float32)
    return result