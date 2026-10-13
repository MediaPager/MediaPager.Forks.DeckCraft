from pathlib import Path
import sys

root = Path(sys.argv[1])
src = root / "crates/ui-egui/src"

def hide_link(label):
    before = f'ui.hyperlink_to("{label}", deckcraft_engine::links::DISCORD);'
    after = f'#[cfg(not(target_arch = "wasm32"))]\n        {before}'
    count = 0
    for path in src.rglob("*.rs"):
        text = path.read_text(encoding="utf-8")
        n = text.count(before)
        if n:
            path.write_text(text.replace(before, after), encoding="utf-8")
            count += n
    if not count:
        raise SystemExit(f"DeckCraft Discord patch anchor missing: {label}")

hide_link("Join the ArtCraft community on Discord")
hide_link("Join our community on Discord")
