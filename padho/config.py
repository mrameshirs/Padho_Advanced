"""Settings, languages and reading levels."""

import os
from datetime import timedelta, timezone

import streamlit as st


def get_secret(name: str, default: str = "") -> str:
    """Read from st.secrets first, then environment. Never from source code."""
    try:
        if name in st.secrets:
            return str(st.secrets[name]).strip()
    except Exception:
        pass
    return os.getenv(name, default).strip()


SCHOOL_NAME = get_secret("SCHOOL_NAME", "Suthukeny Government High School")
TEACHER_PIN = get_secret("TEACHER_PIN")
TEACHER_NAME = get_secret("TEACHER_NAME", "K M Ramyasri")
TEACHER_ROLE = get_secret("TEACHER_ROLE", "Primary School Teacher (PST)")

IST = timezone(timedelta(hours=5, minutes=30))

LANGS = {
    "hi": {"label": "हिंदी · Hindi", "sr": "hi-IN"},
    "mr": {"label": "मराठी · Marathi", "sr": "mr-IN"},
    "ta": {"label": "தமிழ் · Tamil", "sr": "ta-IN"},
    "te": {"label": "తెలుగు · Telugu", "sr": "te-IN"},
    "bn": {"label": "বাংলা · Bengali", "sr": "bn-IN"},
    "gu": {"label": "ગુજરાતી · Gujarati", "sr": "gu-IN"},
    "en": {"label": "English", "sr": "en-IN"},
}

# Reference bands, NOT an examination standard.
# NIPUN Bharat aims for about 60 wpm by the end of Class 3 (= Level 3 here).
LEVELS = {
    1: {"name": "Sprout", "emoji": "🌱", "wpm": 30, "acc": 80, "color": "#38B26B",
        "desc": "Short, simple sentences"},
    2: {"name": "Explorer", "emoji": "🧭", "wpm": 45, "acc": 85, "color": "#2193B0",
        "desc": "A short paragraph read with understanding"},
    3: {"name": "Climber", "emoji": "🧗", "wpm": 60, "acc": 90, "color": "#F2994A",
        "desc": "NIPUN Bharat target: fluent reading with comprehension"},
    4: {"name": "Voyager", "emoji": "⛵", "wpm": 75, "acc": 92, "color": "#8E2DE2",
        "desc": "Longer text, smooth and expressive"},
    5: {"name": "Star Reader", "emoji": "🌟", "wpm": 90, "acc": 94, "color": "#E23D33",
        "desc": "A full story at near-adult pace"},
}
MAX_LEVEL = max(LEVELS)

# A "target reading" must also cover at least this much of the passage,
# so a child cannot qualify by racing through three words.
MIN_COVERAGE_FOR_TARGET = 80
# Target readings needed at the current level to be promoted.
MET_TO_PROMOTE = 3

CLASSES = ["Balvatika"] + [f"Class {i}" for i in range(1, 9)]

# How strictly a heard word must match the passage word to count as correct.
# Strict is the default: a changed vowel or sound is marked as misread.
STRICTNESS = {
    "Strict (recommended)": 1.0,
    "Standard": 0.90,
    "Lenient": 0.80,
}
