"""
Vercel entrypoint for Learn Japanese — serves all 8 packs via the hub.

    /                       -> Pack chooser (hub landing page)
    /hiragana/              -> Hiragana
    /katakana/              -> Katakana
    ... and so on for all 8 packs.

Set QUEST_PACK env var for single-pack mode. Leave unset for the full hub.
"""

import os
import sys
from pathlib import Path

_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(_ROOT))

import learn_japanese as _pkg  # noqa: E402
_PACKS_DIR = str(Path(_pkg.__file__).parent / "skill-packs")
os.environ.setdefault("QUEST_SKILL_PACKS_DIR", _PACKS_DIR)

from engine.skill_pack import load_skill_pack  # noqa: E402

_JAPANESE_PACKS = [
    "hiragana", "katakana", "greetings_jp", "numbers_jp", "food_jp", "daily_jp", "travel_jp", "culture_jp",
]


def _make_app():
    _single_pack = os.environ.get("QUEST_PACK", "")
    if _single_pack:
        from engine.web.server import create_app
        return create_app(load_skill_pack(_single_pack, packs_dir=_PACKS_DIR))
    from engine.web.hub import create_hub_app
    _packs = [load_skill_pack(p, packs_dir=_PACKS_DIR) for p in _JAPANESE_PACKS]
    return create_hub_app(_packs)


app = _make_app()
