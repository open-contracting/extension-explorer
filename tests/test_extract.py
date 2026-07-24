from pathlib import Path
from tempfile import TemporaryDirectory

from extension_explorer.extract import extract_tag

tag = b"""
---
profile:
- slug: ppp
  title: Public Private Partnerships
  extensions:
    - bids
- slug: eu
  title: European Union
  extensions: []
  hidden: true
topic:
- slug: fiscal
  title: Fiscal extensions
"""


def assert_result(filename, content, method, expected):
    with TemporaryDirectory() as d:
        path = Path(d) / filename
        with path.open("wb") as f:
            f.write(content)

        with path.open("rb") as f:
            assert list(method(f, None, None, None)) == expected


def test_extract_tag():
    assert_result(
        "test.csv",
        tag,
        extract_tag,
        [
            (1, "", "Public Private Partnerships", ["/profile/0/title"]),
            (1, "", "European Union", ["/profile/1/title"]),
            (1, "", "Fiscal extensions", ["/topic/0/title"]),
        ],
    )
