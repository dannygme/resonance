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
        r"technologies?|proficiencies?|expertise|competencies|languages?\s*&?\s*tools?|"
        r"software(\s+&\s+tools?)?|applications?|programs?|platforms?|"
        r"design\s+(tools?|software|skills?)|creative\s+(tools?|skills?)|"
        r"technical\s+proficiencies?|key\s+skills?)",
        re.IGNORECASE,
    ),
    "experience": re.compile(
        r"(work\s+experience|professional\s+experience|employment(\s+history)?|"
        r"career\s+history|work\s+history|relevant\s+experience|"
        r"key\s+responsibilities|responsibilities|internship(s)?|"
        r"positions?\s+held|experience|projects?(\s+experience)?|"
        r"freelance(\s+experience)?|contract(\s+work)?|selected\s+work)",
        re.IGNORECASE,
    ),
    "education": re.compile(
        r"(education(al)?(\s+(background|qualifications?|history|summary))?|"
        r"academic(\s+(background|history|qualifications?|profile))?|"
        r"degrees?\s*(earned|requirements?)?|qualifications?|"
        r"schooling|training(\s+and\s+education)?|"
        r"certifications?\s*(and\s+education)?)",
        re.IGNORECASE,
    ),
}

_DEGREE_MAP: list[tuple[str, str]] = [
    (r"B\.?\s*B\.?\s*A\.?",  "bachelor of business administration"),
    (r"B\.?\s*F\.?\s*A\.?",  "bachelor of fine arts"),
    (r"M\.?\s*B\.?\s*A\.?",  "master of business administration"),
    (r"M\.?\s*F\.?\s*A\.?",  "master of fine arts"),
    (r"Ph\.?\s*D\.?",         "doctor of philosophy"),
    (r"J\.?\s*D\.?",          "juris doctor"),
    (r"M\.?\s*D\.?",          "doctor of medicine"),
    (r"B\.?\s*A\.?",          "bachelor of arts"),
    (r"B\.?\s*S\.?",          "bachelor of science"),
    (r"M\.?\s*A\.?",          "master of arts"),
    (r"M\.?\s*S\.?",          "master of science"),
]

_DEGREE_COMBINED = re.compile(
    r"\b(" + "|".join(p for p, _ in _DEGREE_MAP) + r")\b",
    re.IGNORECASE,
)
_DEGREE_LOOKUP = {
    re.compile(r"^" + p + r"$", re.IGNORECASE): repl
    for p, repl in _DEGREE_MAP
}

_SKILL_LIST_PATTERN = re.compile(
    r"^([\w\+\#\.\s\-/]{2,40})(,\s*[\w\+\#\.\s\-/]{2,40}){2,}$"
)
_PROSE_SIGNALS = re.compile(
    r"\b(in|or|and|with|for|of|the|is|are|a|an|to|that|which|required|preferred)\b",
    re.IGNORECASE,
)

_NOISE      = re.compile(r"[^\w\s\-\'\+\#\.]")
_WHITESPACE = re.compile(r"\s+")


def _normalize_degrees(text: str) -> str:
    def _replace(m: re.Match) -> str:
        token = m.group(0)
        for pat, repl in _DEGREE_LOOKUP.items():
            if pat.match(token):
                return repl
        return token
    return _DEGREE_COMBINED.sub(_replace, text)


def _expand_skill_list(text: str) -> str:
    lines = text.splitlines()
    expanded = []
    for line in lines:
        stripped = line.strip()
        if _SKILL_LIST_PATTERN.match(stripped) and not _PROSE_SIGNALS.search(stripped):
            items = [s.strip() for s in stripped.split(",") if s.strip()]
            expanded.append("proficient in " + ", skilled in ".join(items))
        else:
            expanded.append(stripped)
    return "\n".join(expanded)


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
    text = _normalize_degrees(text)
    text = _expand_skill_list(text)

    lines   = _split_into_lines(text)
    buckets: dict[str, list[str]] = {k: [] for k in SECTION_PATTERNS}
    buckets["other"] = []

    current = "other"
    for line in lines:
        matched_sec = None
        for sec, pat in SECTION_PATTERNS.items():
            if _is_section_header(line, pat):
                matched_sec = sec
                break
        if matched_sec:
            current = matched_sec
            if len(line.strip(":*•–-— ").strip().split()) > 2:
                buckets[current].append(line)
        else:
            buckets[current].append(line)

    return {k: clean_text(" ".join(v)) for k, v in buckets.items()}


def preprocess(text: str) -> dict:
    normalized = _normalize_degrees(_expand_skill_list(text))
    return {
        "full":     clean_text(normalized),
        "sections": extract_sections(text),
    }
