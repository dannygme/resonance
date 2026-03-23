"""
Resonance -- Resume / Job Matching System
Built by Danny Greene, 2026

preprocess.py
Text cleaning and section extraction for resume and job description inputs.
"""

import re

SECTION_PATTERNS = {
    "skills": re.compile(
        r"(technical\s+skills?|skills?(\s+(summary|profile|set|highlights?))?|"
        r"core\s+(competencies|skills?)|tools?\s*(&|and)?\s*technologies?|"
        r"technologies?|proficiencies?|expertise|competencies|languages?\s*&?\s*tools?)",
        re.IGNORECASE,
    ),
    "experience": re.compile(
        r"(work\s+experience|professional\s+experience|employment(\s+history)?|"
        r"career\s+history|work\s+history|relevant\s+experience|"
        r"key\s+responsibilities|responsibilities|internship(s)?|"
        r"positions?\s+held|experience)",
        re.IGNORECASE,
    ),
    "education": re.compile(
        r"(education(al)?(\s+(background|qualifications?|history|summary))?|"
        r"academic(\s+(background|history|qualifications?|profile))?|"
        r"degrees?\s*(earned|requirements?)?|qualifications?|"
        r"university|college|schooling|training(\s+and\s+education)?|"
        r"certifications?\s*(and\s+education)?)",
        re.IGNORECASE,
    ),
}

_NOISE      = re.compile(r"[^\w\s\-\'\+\#\.]")
_WHITESPACE = re.compile(r"\s+")


def clean_text(text: str) -> str:
    text = text.lower()
    text = _NOISE.sub(" ", text)
    text = _WHITESPACE.sub(" ", text)
    return text.strip()


def _split_into_lines(text: str) -> list[str]:
    return [ln.strip() for ln in text.splitlines() if ln.strip()]


def _is_section_header(line: str, pattern: re.Pattern) -> bool:
    stripped = line.strip(":*•–-— ").strip()
    if len(stripped.split()) > 7:
        return False
    return bool(pattern.fullmatch(stripped) or pattern.search(stripped))


def extract_sections(text: str) -> dict[str, str]:
    lines   = _split_into_lines(text)
    buckets: dict[str, list[str]] = {k: [] for k in SECTION_PATTERNS}
    buckets["other"] = []

    current = "other"
    for line in lines:
        matched = False
        for sec, pat in SECTION_PATTERNS.items():
            if _is_section_header(line, pat):
                current = sec
                matched = True
                break
        if not matched:
            buckets[current].append(line)

    return {k: clean_text(" ".join(v)) for k, v in buckets.items()}


def preprocess(text: str) -> dict:
    return {
        "full":     clean_text(text),
        "sections": extract_sections(text),
    }