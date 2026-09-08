import json
from pathlib import Path


EXTENSION_DIR = Path(__file__).resolve().parents[2] / "flow-extension"


def test_manifest_allows_new_and_legacy_flow_pages():
    manifest = json.loads((EXTENSION_DIR / "manifest.json").read_text(encoding="utf-8"))

    assert "https://flow.google.com/*" in manifest["host_permissions"]
    assert "https://flow.google.com/*" in manifest["content_scripts"][0]["matches"]
    assert "https://flow.google.com/*" in manifest["web_accessible_resources"][0]["matches"]
    assert "https://labs.google/fx/tools/flow*" in manifest["content_scripts"][0]["matches"]


def test_background_uses_precise_flow_page_eligibility_and_shared_tab_patterns():
    source = (EXTENSION_DIR / "background.js").read_text(encoding="utf-8")

    assert "'https://flow.google.com/*'" in source
    assert "parsed.hostname === 'flow.google.com'" in source
    assert "parsed.hostname !== 'labs.google'" in source
    assert "return createdTab;" in source
    assert "url: '*://labs.google/*'" not in source
    assert source.count("url: FLOW_TAB_URLS") >= 3

