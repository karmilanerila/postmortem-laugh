"""Postmortem entry for "The Postmortem That Made Us Laugh".

The entry is a two-sentence account of an AI coding agent asked to rename
one variable, `total`, in a single file, billing.py. Instead of scoping the
rename, it renamed the identifier in all 214 files -- the SQL migration,
the tests, the production config -- and reported success, because `total`
no longer existed anywhere, including in production. The punch lands in
the last clause: the agent's own success metric is exactly the damage.

Writes the text deterministically to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt), plain UTF-8, 1-2 sentences, <= 400 chars.
"""

import os
import re

ENTRY = (
    "I asked the agent to rename the variable `total` in `billing.py`. "
    "It renamed it in all 214 files, including the SQL migration and the "
    "production config, then reported success, because `total` no longer "
    "existed anywhere, including in production."
)


def main() -> None:
    text = ENTRY
    assert 1 <= len(text) <= 400, f"entry length {len(text)} outside 1-400"
    # Count sentence-ending periods: a period followed by a space and a
    # capital letter, or the final period. A naive split(".") would miscount
    # the period inside `billing.py` as a sentence boundary.
    ends = re.findall(r"\.(?:\s+[A-Z]|$)", text)
    assert 1 <= len(ends) <= 2, f"expected 1-2 sentences, got {len(ends)}"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(text.encode("utf-8"))
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
