"""
learn_japanese/main.py — Entry points for Learn Japanese.

Sets the skill-packs directory for the engine, then launches
the appropriate pack.
"""

import os
import sys
from pathlib import Path

# Ensure UTF-8 output (handles Japanese characters, romaji, etc.)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

_HERE = Path(__file__).parent
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", str(_HERE / "skill-packs"))

from engine.main import run, run_campaign          # noqa: E402
from engine.updater import check_and_prompt        # noqa: E402

_PACKAGE = "learn-japanese"
_PACKS_DIR = str(_HERE / "skill-packs")

_WEB = "--web" in sys.argv

JAPANESE_PACKS = [
    "hiragana", "katakana", "greetings_jp", "numbers_jp",
    "food_jp", "daily_jp", "travel_jp", "culture_jp", "colors_nature", "shopping_jp", "directions_jp", "family_jp", "weather_jp",
]


def _web(pack_name: str, port: int = 8080):
    """Launch the web interface for *pack_name*."""
    from engine.web.server import serve
    serve(pack_name, port=port, packs_dir=_PACKS_DIR)


def main_japanese():
    if _WEB:
        from engine.web.hub import serve_hub
        serve_hub(JAPANESE_PACKS, port=8080, packs_dir=_PACKS_DIR)
        return
    check_and_prompt(_PACKAGE)
    run_campaign("learn_japanese")


def main_hiragana():
    if _WEB:
        _web("hiragana")
        return
    check_and_prompt(_PACKAGE)
    run("hiragana")


def main_katakana():
    if _WEB:
        _web("katakana")
        return
    check_and_prompt(_PACKAGE)
    run("katakana")


def main_greetings_jp():
    if _WEB:
        _web("greetings_jp")
        return
    check_and_prompt(_PACKAGE)
    run("greetings_jp")


def main_numbers_jp():
    if _WEB:
        _web("numbers_jp")
        return
    check_and_prompt(_PACKAGE)
    run("numbers_jp")


def main_food_jp():
    if _WEB:
        _web("food_jp")
        return
    check_and_prompt(_PACKAGE)
    run("food_jp")


def main_daily_jp():
    if _WEB:
        _web("daily_jp")
        return
    check_and_prompt(_PACKAGE)
    run("daily_jp")


def main_travel_jp():
    if _WEB:
        _web("travel_jp")
        return
    check_and_prompt(_PACKAGE)
    run("travel_jp")


def main_culture_jp():
    if _WEB:
        _web("culture_jp")
        return
    check_and_prompt(_PACKAGE)
    run("culture_jp")
