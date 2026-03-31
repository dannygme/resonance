"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

anonymize.py
Strips PII from resume text before embedding.
Used by the Screen Applicants page when Incognito Mode is active.
"""

import re

_EMAIL   = re.compile(r'\S+@\S+\.\S+')
_PHONE   = re.compile(r'(\+?1?\s?)?(\(?\d{3}\)?[\s\-\.]?\d{3}[\s\-\.]?\d{4})')
_URL     = re.compile(r'https?://\S+|www\.\S+')
_ADDRESS = re.compile(
    r'\d+\s+\w+\s+(street|st|avenue|ave|road|rd|blvd|drive|dr|lane|ln|way)\b',
    re.IGNORECASE
)
_GRAD_YR = re.compile(r'\b(19|20)\d{2}\b')


def anonymize(text: str) -> str:
    text = _EMAIL.sub('[EMAIL]', text)
    text = _PHONE.sub('[PHONE]', text)
    text = _URL.sub('[URL]', text)
    text = _ADDRESS.sub('[ADDRESS]', text)
    text = _GRAD_YR.sub('[YEAR]', text)
    return text