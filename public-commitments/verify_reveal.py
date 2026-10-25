"""Check a Colony Zero reveal against its published commitments. Python 3 standard library only.

Usage: python3 verify_reveal.py reveal/EXP-CZ-001
Exits 0 when every check passes, 1 otherwise.
"""
import hashlib
import hmac
import json
import sys
from pathlib import Path

# Values published before the sealed run (EXP-CZ-001.md and EXP-CZ-001-freeze.txt).
EXPECTED = {
    "sealed_file_sha256": "0a60bd438ddabbea9e2cc92d640b6b0437ffac7f7db8bddf34881003d0cd8388",
    "sealed_salt_commitment": "944c6a61135558626cf27bc7897b3ced84bd8f71920bf8304dfbfd10587ebe4b",
    "manifest_salt_commitment": "e95cdac1cc593d6c98df55e7d39bbbe00c92d003cc7f28b5f97c483be929eb51",
    "manifest_file_sha256": "08422b7b06dbe82fe50171b72d7bbeeaaa0639fdf795d814eedafa5a1af24d4a",
    "commitment_root": "c95f852c4967ede66f40f29bdfff8d3666127c940efef2fbe858e3b222d52ef9",
}


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def manifest_root(manifest, salt):
    # Each field gets its own salt, HMAC-SHA256(manifest salt, field name); its leaf is
    # SHA-256(field salt | canonical JSON of the value); the root hashes the leaves in field-name order.
    leaves = {}
    for name, value in manifest.items():
        field_salt = hmac.new(salt, name.encode(), hashlib.sha256).digest()
        leaves[name] = hashlib.sha256(field_salt + b"|" + canonical_json(value)).hexdigest()
    return hashlib.sha256(b"".join(bytes.fromhex(leaves[k]) for k in sorted(leaves))).hexdigest()


def main(folder):
    d = Path(folder)
    sha = lambda b: hashlib.sha256(b).hexdigest()
    sealed_salt = bytes.fromhex(d.joinpath("sealed_salt.hex").read_text().strip())
    manifest_salt = bytes.fromhex(d.joinpath("manifest_salt.hex").read_text().strip())
    manifest_bytes = d.joinpath("manifest.json").read_bytes()
    checks = {
        "sealed task file matches its hash": sha(d.joinpath("sealed1200.jsonl").read_bytes()) == EXPECTED["sealed_file_sha256"],
        "sealed salt matches its commitment": sha(b"cz-salt-commit-v1|" + sealed_salt) == EXPECTED["sealed_salt_commitment"],
        "manifest salt matches its commitment": sha(b"cz-manifest-salt-commit-v1|" + manifest_salt) == EXPECTED["manifest_salt_commitment"],
        "manifest file matches its hash": sha(manifest_bytes) == EXPECTED["manifest_file_sha256"],
        "manifest reproduces the commitment root": manifest_root(json.loads(manifest_bytes), manifest_salt) == EXPECTED["commitment_root"],
    }
    for name, ok in checks.items():
        print(("PASS " if ok else "FAIL ") + name)
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "reveal/EXP-CZ-001"))
