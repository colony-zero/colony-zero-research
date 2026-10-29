"""Check a Colony Zero reveal against its published commitments. Python 3 standard library only.

Usage:
  python3 verify_reveal.py reveal/EXP-CZ-001
  python3 verify_reveal.py reveal/EXP-CZ-009-011
  python3 verify_reveal.py reveal/EXP-CZ-017
  python3 verify_reveal.py reveal/EXP-CZ-003a
  python3 verify_reveal.py --self-test

A reveal folder holds one experiment's files, or, when several experiments share one sealed set, the shared
sealed file and its salt at the top and one subfolder per experiment (EXP-CZ-009/, EXP-CZ-010/, ...).
Exits 0 when every check passes, 1 otherwise.
"""
import hashlib
import hmac
import json
import os
import sys
import tempfile
from pathlib import Path

# Values published before the reveal, copied from the commitment pages in this folder (EXP-CZ-0xx.md and
# EXP-CZ-0xx-freeze.txt). The freeze ledger root covers the freeze event, which records every other value here,
# so the OpenTimestamps proof of the freeze record dates all of them.
SET2 = {
    "sealed_file": "sealed1200-s2.jsonl",
    "sealed_file_sha256": "578bc7a8e63dd1602a88318bed24ba24ffd9281a06c311a58130e1e1911a4297",
    "sealed_salt_commitment": "e9dd57a6be3b5dd871476b54441710d5614007d0dd3f1b01a207ef449b3ce4b4",
}
EXPECTED = {
    "EXP-CZ-001": {
        "sealed_file": "sealed1200.jsonl",
        "sealed_file_sha256": "0a60bd438ddabbea9e2cc92d640b6b0437ffac7f7db8bddf34881003d0cd8388",
        "sealed_salt_commitment": "944c6a61135558626cf27bc7897b3ced84bd8f71920bf8304dfbfd10587ebe4b",
        "manifest_salt_commitment": "e95cdac1cc593d6c98df55e7d39bbbe00c92d003cc7f28b5f97c483be929eb51",
        "manifest_digest": "58e9b7bd900eb86d80c5e520caff28c69a3c7e5ab9db02bd6c065ef02e976fe5",
        "commitment_root": "c95f852c4967ede66f40f29bdfff8d3666127c940efef2fbe858e3b222d52ef9",
        "manifest_file_sha256": None,  # not published for EXP-CZ-001; its digest is checked instead
        "freeze_ledger_root": "c59b3e3ca3468feb0097fde5117642d796a735cae37149502b50a4f886afacdf",
        "freeze_ledger_required": False,  # the EXP-CZ-001 reveal did not include its freeze ledger
    },
    "EXP-CZ-009": dict(SET2,
        manifest_salt_commitment="35c6b2c33583e4e4b7864add1b0ef5897edf0ad431856463c48c4aa301104356",
        manifest_digest="1d8b7861b34343caa3c761e3147e468b881255b6a3b205cef9d1cc0290830651",
        commitment_root="1d3dc84533898b3375b5f936508ca3f774f596d0dbf47bbb7ced667a9fa1327c",
        manifest_file_sha256="79aadf666e33049ab3581c21c4baf9b861e2b473928a366dd1a6feb45d873cf1",
        freeze_ledger_root="aade5eba2744874c63df6f2a56ec2987039aa4c6436f52f8dff2525609ec852c",
    ),
    "EXP-CZ-010": dict(SET2,
        manifest_salt_commitment="1e23a0f06cdd7c1469f0fbc973d05b67de14916292aae53d72855ec3372bff15",
        manifest_digest="0aa38df1b86d030daba8f21512b9c0802cce48bc676d142d47ab5beae1e24d98",
        commitment_root="1468e1c64dbae2ac9b6cf2e482db2bf46a6cee122c6a4f1160ff2c85b9a70237",
        manifest_file_sha256="0cb7e715fa333564b44b1c6050e926f6d8c14a99d0b9be31db68f97cda4d8965",
        freeze_ledger_root="7f0b925d9e5fd4d7b55f32637e2943def7a10300e45d87a50c190b428e6cefdf",
    ),
    "EXP-CZ-011": dict(SET2,
        manifest_salt_commitment="a7cd3a0287c0ce36e57b61bff9e2781cfa03a69bef230778e6148e67b71f83aa",
        manifest_digest="d0c4ba78408ec0551903f93a6e5040ba9822ab87a93db9d7a0670226cb54a7ed",
        commitment_root="5a7eed654b0dc2c7a9ca508b3fd99d8ad8f8ad59d0ac41dc6c92b179a56bd67f",
        manifest_file_sha256="4a84aa5b5df3eedb9fb0f7769bf2f00b956d8462fc97214f8c8dde68cdb889e4",
        freeze_ledger_root="da1c6550535b33e827aba29b3743f7adc928e1f1dd77cba39ef71505a1d7b3bd",
    ),
    "EXP-CZ-017": {
        "sealed_file": "sealed-s3-scored.jsonl",
        "sealed_file_sha256": "7531dc118f7991dbaaf7720c4a512923b0fc072ec2f146e1ee932dee78873136",
        "sealed_salt_commitment": "4ed91e22a8e6b450cf04d4d76af727766dab0429249be008dfe67dd531e67dfe",
        "manifest_salt_commitment": "18bbfdc47bc251e5fbc1b4580a57a278aa0f64d28e2e71876cf198cc3f35b3fb",
        "manifest_digest": "4c2b76347d85c79e643858b905b69ea4d6e43d214e4713dca1a48b5422466d05",
        "commitment_root": "55a51dd37ca213dbc6ee99f51ca59b5baca1f747919a1ce567d06c9b7dd9500a",
        "manifest_file_sha256": "2c5ab6893fddd502a8bbbdb0d067f04ea7c6b06e1d3991443df7cded83f29aa1",
        "freeze_ledger_root": "35c648e696ae3b8c601fce5fb4930927c8179db5488f6b9155e8f851ebaf57b8",
    },    "EXP-CZ-003a": {
        "sealed_file": "sealed-s4-scored.jsonl",
        "sealed_file_sha256": "525da50809ff284fe5e4ee458320e5a01152717e8c7ca089b72317435914a530",
        "sealed_salt_commitment": "0d3724b9d80714aa27a0284d6fc525e150a0c055176f0a7aa7e15d2312a2d617",
        "manifest_salt_commitment": "63eb8c0e1be202d8bc1cfe493126cc46508f61c7056093c82113ade9356ad804",
        "manifest_digest": "e455e58c029263e0c3e50d948083578ebe8cf560a7fedf7cf693563fa7ba7574",
        "commitment_root": "a8f0663504e03c7c2ce455aff69203351ca3432842b958b39d52b802d18c2c6e",
        "manifest_file_sha256": "5a114f2bc73696ea5a3a2e8bf87dda6fc4db4c4ab41b35bead47a7b6dbbe1227",
        "freeze_ledger_root": "5123db066ad93aef1bf0c5aba30453cc8619b3362443b53ec076ca8fa0f2d988",
    },
}
GENESIS = "0" * 64


def sha(b):
    return hashlib.sha256(b).hexdigest()


def canonical_json(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def field_salt(salt, name):
    # Each field gets its own salt, HMAC-SHA256(manifest salt, field name).
    return hmac.new(salt, name.encode(), hashlib.sha256).digest()


def leaf(fsalt, value):
    # A field's leaf is SHA-256(field salt | canonical JSON of the value).
    return sha(fsalt + b"|" + canonical_json(value))


def root_of(leaves):
    # The root hashes the leaves in field-name order.
    return sha(b"".join(bytes.fromhex(leaves[k]) for k in sorted(leaves)))


def manifest_root(manifest, salt):
    return root_of({name: leaf(field_salt(salt, name), value) for name, value in manifest.items()})


def partial_root(rev, salt):
    # Root from a selective reveal: revealed fields are re-hashed, withheld fields contribute their published leaf.
    leaves = dict(rev.get("other_leaves", {}))
    for name, value in rev["revealed"].items():
        if rev["field_salts"].get(name) != field_salt(salt, name).hex():
            return None
        leaves[name] = leaf(field_salt(salt, name), value)
    return root_of(leaves)


def event_hash(ev):
    body = {k: ev[k] for k in ("schema", "seq", "run_id", "kind", "actor", "payload", "prev_hash")}
    return sha(canonical_json(body))


def ledger_root(path):
    # Every event must hash correctly and point at the one before it; the root is the last event's hash.
    prev, events = GENESIS, []
    for i, line in enumerate(l for l in path.read_text(encoding="utf-8").split("\n") if l):
        ev = json.loads(line)
        if ev["seq"] != i or ev["prev_hash"] != prev or ev["hash"] != event_hash(ev):
            return None, events
        prev = ev["hash"]
        events.append(ev)
    return prev, events


def read_hex(path):
    return bytes.fromhex(path.read_text().strip())


def check_experiment(exp_id, d, shared, exp):
    """Return a list of (status, text) for one experiment. d holds its manifest files; shared holds the sealed set."""
    out = []

    def check(name, fn):
        try:
            ok = bool(fn())
        except (OSError, ValueError, KeyError, TypeError) as exc:
            ok, name = False, f"{name} ({type(exc).__name__}: {exc})"
        out.append(("PASS" if ok else "FAIL", name))

    check("sealed task file matches its hash", lambda: sha(shared.joinpath(exp["sealed_file"]).read_bytes()) == exp["sealed_file_sha256"])
    check("sealed salt matches its commitment", lambda: sha(b"cz-salt-commit-v1|" + read_hex(shared / "sealed_salt.hex")) == exp["sealed_salt_commitment"])
    check("manifest salt matches its commitment", lambda: sha(b"cz-manifest-salt-commit-v1|" + read_hex(d / "manifest_salt.hex")) == exp["manifest_salt_commitment"])

    if d.joinpath("manifest.json").exists():
        raw = d.joinpath("manifest.json").read_bytes()
        if exp.get("manifest_file_sha256"):
            check("manifest file matches its SHA-256", lambda: sha(raw) == exp["manifest_file_sha256"])
        check("manifest matches its digest (SHA-256 of canonical JSON)", lambda: sha(canonical_json(json.loads(raw))) == exp["manifest_digest"])
        check("manifest reproduces the commitment root", lambda: manifest_root(json.loads(raw), read_hex(d / "manifest_salt.hex")) == exp["commitment_root"])
    elif d.joinpath("manifest_reveal.json").exists():
        rev = json.loads(d.joinpath("manifest_reveal.json").read_text(encoding="utf-8"))
        withheld = ", ".join(sorted(rev.get("other_leaves", {}))) or "none"
        out.append(("SKIP", f"manifest file hash and digest: manifest.json not in this reveal (withheld fields: {withheld})"))
    else:
        out.append(("FAIL", "manifest: neither manifest.json nor manifest_reveal.json is present"))

    if d.joinpath("manifest_reveal.json").exists():
        def reveal_ok():
            rev = json.loads(d.joinpath("manifest_reveal.json").read_text(encoding="utf-8"))
            if d.joinpath("manifest.json").exists():
                m = json.loads(d.joinpath("manifest.json").read_bytes())
                if any(m.get(k) != v for k, v in rev["revealed"].items()):
                    return False
            return rev.get("root") == exp["commitment_root"] and partial_root(rev, read_hex(d / "manifest_salt.hex")) == exp["commitment_root"]
        check("manifest_reveal.json reproduces the commitment root, field by field", reveal_ok)

    if d.joinpath("freeze.jsonl").exists():
        def freeze_ok():
            root, events = ledger_root(d / "freeze.jsonl")
            if root != exp["freeze_ledger_root"] or len(events) != 1:
                return False
            p = events[0]["payload"]
            want = {k: exp[k] for k in ("commitment_root", "manifest_digest", "manifest_salt_commitment",
                                        "sealed_file_sha256", "sealed_salt_commitment", "manifest_file_sha256") if exp.get(k)}
            return p.get("exp_id") == exp_id and all(p.get(k) == v for k, v in want.items())
        check("freeze ledger reproduces its root and records these commitments", freeze_ok)
    elif exp.get("freeze_ledger_required", True):
        out.append(("FAIL", "freeze ledger: freeze.jsonl is missing"))
    else:
        out.append(("SKIP", "freeze ledger: not part of this reveal"))
    return out


def verify(folder, expected=None):
    expected = expected or EXPECTED
    top = Path(folder)
    subs = sorted(p for p in top.iterdir() if p.is_dir() and p.name in expected)
    targets = [(p.name, p) for p in subs] or [(top.name, top)]
    all_ok = True
    for exp_id, d in targets:
        if exp_id not in expected:
            print(f"FAIL {exp_id}: no published commitments are known for this folder name")
            return 1
        print(f"{exp_id}")
        for status, text in check_experiment(exp_id, d, top, expected[exp_id]):
            print(f"  {status} {text}")
            all_ok &= status != "FAIL"
    return 0 if all_ok else 1


def self_test():
    """Build fake reveals from random salts and a fake manifest, check that they pass, then that tampering fails."""
    import contextlib
    import io

    def run(folder, expected):
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            code = verify(folder, expected)
        return code, buf.getvalue()

    def build(top, exp_id, shared, sealed_name, reveal_mode, salt):
        msalt = os.urandom(32)
        d = top / exp_id if shared else top
        d.mkdir(parents=True, exist_ok=True)
        sealed = b'{"id":"t0","prompt":"fake","answer":"1"}\n'
        top.joinpath(sealed_name).write_bytes(sealed)
        top.joinpath("sealed_salt.hex").write_text(salt.hex())
        manifest = {"exp_id": exp_id, "title": "fake", "hypotheses": ["H"], "arms": ["a"], "primary_endpoint": "e",
                    "decision_rule": "r", "failure_criteria": "f", "task_spec": {"sealed_file_sha256": sha(sealed)},
                    "models": [{"id": "m"}], "seeds": [0], "budget": {"cap": 1}, "schema": "cz.manifest.v1"}
        raw = json.dumps(manifest, indent=2).encode()
        leaves = {k: leaf(field_salt(msalt, k), v) for k, v in manifest.items()}
        exp = {"sealed_file": sealed_name, "sealed_file_sha256": sha(sealed),
               "sealed_salt_commitment": sha(b"cz-salt-commit-v1|" + salt),
               "manifest_salt_commitment": sha(b"cz-manifest-salt-commit-v1|" + msalt),
               "manifest_digest": sha(canonical_json(manifest)), "commitment_root": root_of(leaves),
               "manifest_file_sha256": sha(raw)}
        payload = {"exp_id": exp_id, "commitment_root": exp["commitment_root"], "manifest_digest": exp["manifest_digest"],
                   "manifest_file_sha256": exp["manifest_file_sha256"], "manifest_salt_commitment": exp["manifest_salt_commitment"],
                   "sealed_file_sha256": exp["sealed_file_sha256"], "sealed_salt_commitment": exp["sealed_salt_commitment"],
                   "fields": sorted(manifest), "utc": "2000-01-01T00:00:00Z"}
        ev = {"schema": "cz.event.v1", "seq": 0, "run_id": f"freeze-{exp_id}", "kind": "freeze", "actor": "owner",
              "payload": payload, "prev_hash": GENESIS}
        ev["hash"] = event_hash(ev)
        exp["freeze_ledger_root"] = ev["hash"]
        d.joinpath("freeze.jsonl").write_text(json.dumps(ev, sort_keys=True) + "\n", encoding="utf-8")
        d.joinpath("manifest_salt.hex").write_text(msalt.hex())
        hide = {"task_spec", "models"} if reveal_mode == "redacted" else set()
        rev = {"root": exp["commitment_root"],
               "revealed": {k: v for k, v in manifest.items() if k not in hide},
               "field_salts": {k: field_salt(msalt, k).hex() for k in manifest if k not in hide},
               "other_leaves": {k: leaves[k] for k in hide}}
        d.joinpath("manifest_reveal.json").write_text(json.dumps(rev), encoding="utf-8")
        if reveal_mode == "full":
            d.joinpath("manifest.json").write_bytes(raw)
        return exp

    failures = []
    with tempfile.TemporaryDirectory(prefix="cz-verify-selftest-") as tmp:
        tmp = Path(tmp)
        # 1. Two experiments sharing one sealed set, full manifests.
        shared = tmp / "EXP-CZ-900-901"
        shared.mkdir()
        set_salt = os.urandom(32)
        expected = {e: build(shared, e, True, "sealed-fake.jsonl", "full", set_salt) for e in ("EXP-CZ-900", "EXP-CZ-901")}
        code, text = run(shared, expected)
        if code != 0 or text.count("PASS") != 16:
            failures.append("shared full reveal should pass 16 checks:\n" + text)

        # 2. A single flat experiment with a selective (redacted) manifest reveal.
        flat = tmp / "EXP-CZ-902"
        flat.mkdir()
        exp902 = {"EXP-CZ-902": build(flat, "EXP-CZ-902", False, "sealed-fake.jsonl", "redacted", os.urandom(32))}
        code, text = run(flat, exp902)
        if code != 0 or "SKIP manifest file hash" not in text or text.count("PASS") != 5:
            failures.append("redacted reveal should pass 5 checks and skip the manifest hash:\n" + text)

        # 3. Tampering: each change must make the run fail.
        tampers = {
            "sealed file": lambda: shared.joinpath("sealed-fake.jsonl").write_bytes(b"changed\n"),
            "sealed salt": lambda: shared.joinpath("sealed_salt.hex").write_text(os.urandom(32).hex()),
            "manifest salt": lambda: shared.joinpath("EXP-CZ-900", "manifest_salt.hex").write_text(os.urandom(32).hex()),
            "manifest field": lambda: shared.joinpath("EXP-CZ-900", "manifest.json").write_text(
                shared.joinpath("EXP-CZ-900", "manifest.json").read_text().replace('"fake"', '"other"')),
            "freeze ledger": lambda: shared.joinpath("EXP-CZ-901", "freeze.jsonl").write_text(
                shared.joinpath("EXP-CZ-901", "freeze.jsonl").read_text().replace("2000-01-01", "2000-01-02")),
            "missing freeze ledger": lambda: shared.joinpath("EXP-CZ-901", "freeze.jsonl").unlink(),
        }
        for name, change in tampers.items():
            backup = {p: p.read_bytes() for p in shared.rglob("*") if p.is_file()}
            change()
            code, text = run(shared, expected)
            if code == 0:
                failures.append(f"tampered {name} was not detected")
            for p, b in backup.items():
                p.write_bytes(b)
        code, text = run(shared, expected)
        if code != 0:
            failures.append("restored reveal should pass again:\n" + text)
    for f in failures:
        print("SELF-TEST FAIL " + f)
    print("self-test: " + ("PASS" if not failures else f"{len(failures)} failure(s)"))
    return 0 if not failures else 1


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "reveal/EXP-CZ-001"
    sys.exit(self_test() if arg == "--self-test" else verify(arg))
