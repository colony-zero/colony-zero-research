"""Check a Colony Zero reveal against its published commitments. Python 3 standard library only.

Usage:
  python3 verify_reveal.py reveal/EXP-CZ-001
  python3 verify_reveal.py reveal/EXP-CZ-009-011
  python3 verify_reveal.py reveal/EXP-CZ-017
  python3 verify_reveal.py reveal/EXP-CZ-003a
  python3 verify_reveal.py reveal/EXP-CZ-002 exp-cz-002-reveal.tar.gz
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
import tarfile
import tempfile
from pathlib import Path


EXP002_COMMITMENT_SHA256 = {
    "commitments/EXP-CZ-002/COMMIT-PREGEN.txt": "9acfd3b120e7f2164a6a6481d3a7c6c5f21c73359431f04974c175a0dc46b4e9",
    "commitments/EXP-CZ-002/COMMIT-PRERUN.txt": "e0d7d41eaa09b254a200676d791aed76e530631ad7112c5409e68e08cbaa9f42",
    "commitments/EXP-CZ-002/POSTRUN.txt": "ffe20dc052eab11c6508416afc09252af8c1e8786cd1e74f6b2b1bca8341c537",
    "commitments/EXP-CZ-002/BEACON.txt": "1ebbe32c30b9af66bc117a7c58fa02c60cfd62e7f3c0e6be159ade0021f958b1",
    "commitments/EXP-CZ-002/AMEND-A1.txt": "b57802fd041012ef30fd0cbc5fd22f44c5dbb61655af000777c2a8e7eccee2ba",
    "commitments/EXP-CZ-002/AMEND-A2.txt": "2af4a2f0093cc0c941a7862087a316912c727af6745480d706a5cb7dace9d3ec",
    "commitments/EXP-CZ-002/AMEND-A3.txt": "a4c64f2ee96a9d0f0172c42bc70a02d8193d2a85942a6251e691fee9b90501c0",
    "commitments/EXP-CZ-002/AMEND-A4.txt": "990513c0868890211da9cfa1ce95feff8a3f1e8ecfa3a54d8f5942464221d5f5",
    "commitments/EXP-CZ-002/AMEND-A5.txt": "a85f534de2763a2bbe3a61a90cfb80adc78ebbefef12d8ac811c13e175df4e70",
    "commitments/EXP-CZ-002/AMEND-A6.txt": "675c00a348dd99f19a65d4310ec66de3cf6347ba6ea1f276ca2d6a8c2e27601a",
}
EXP002_REVIEWED_INPUT_SHA256 = {
    "REPORT.md": "6129d64f6e8bbdc1814cb0b29a72d2e7c62bd566e01e284b4b9928e85f2bb1b9",
    "scorer.json": "51822f7062589059742c62666e401a128bead962974c5c44fbcc8a852c0494ff",
    "SCORING_ENVELOPE.json": "c82774f63e5f5cbd6037f718f894efb6cfe50511038e08814cf84bbf1ff438a2",
    "amend-a5-receipt.json": "62f2d8be977430a87c8584bb1fe9b7db25340db88a4823b2a5a88f2bb626dc9a",
    "amend-a6-receipt.json": "bc6331dd80f232823039b41d7e722cc046a6b99c2f007fbe397b2356efa60370",
}
EXP002_SCORER_PROJECTION = {
    "H2.1": {
        "status": "SUPPORTED", "gain": 0.07583333333333334,
        "p": 1.8567069153217267e-14,
    },
    "H2.2": {"status": "SUPPORTED"},
    "H2.2.decomposable": {
        "status": "SUPPORTED", "gain": 0.2841666666666667,
        "p": 8.788262488952081e-83, "p_holm": 3.5153049955808323e-82,
    },
    "H2.2.sequential": {
        "status": "SUPPORTED", "gain": 0.26916666666666667,
        "p": 1.7283750754063332e-81, "p_holm": 5.185125226219e-81,
    },
    "H2.3": {
        "status": "NOT_SUPPORTED", "gain": 0.0, "p": 1.0, "p_holm": 1.0,
    },
    "H2.4": {
        "status": "SUPPORTED", "gain": 0.13666666666666666,
        "p": 1.2636640000538576e-95, "p_holm": 6.318320000269288e-95,
    },
    "H2.5": {
        "status": "SUPPORTED", "gain": 0.1,
        "p": 7.072059810490878e-16, "p_holm": 1.4144119620981756e-15,
    },
}
EXP002_4X_COVERAGE = {
    "T3": 0.81625,
    "U_tool": 0.7404166666666666,
}

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


def commitment_value(path, key):
    for line in path.read_text(encoding="utf-8").splitlines():
        name, _, value = line.partition(" ")
        if name == key and value:
            return value
    raise ValueError(f"{key} is missing from {path.name}")


def release_bytes(path):
    """Read the flat EXP-CZ-002 release directory or tarball without extracting it."""
    path = Path(path)
    files = {}
    if path.is_dir():
        for item in path.iterdir():
            if item.is_symlink() or not item.is_file() or item.name in files:
                raise ValueError("release directory is not a flat set of regular files")
            files[item.name] = item.read_bytes()
    else:
        if path.is_symlink() or not path.is_file():
            raise ValueError("release asset is not a regular file")
        with tarfile.open(path, mode="r:gz") as package:
            for member in package.getmembers():
                name = member.name.removeprefix("./")
                if name in {"", "."} and member.isdir():
                    continue
                if (not member.isfile() or not name or "/" in name or name in files
                        or member.issym() or member.islnk()):
                    raise ValueError("release archive is not a flat set of regular files")
                stream = package.extractfile(member)
                if stream is None:
                    raise ValueError("release member cannot be read")
                files[name] = stream.read()
    if len(files) != 46:
        raise ValueError(f"release asset has {len(files)} files instead of 46")
    return files


def exp002_postrun_hashes(raw):
    """Parse the exact private POSTRUN digest list published with the reveal."""
    if not raw.endswith(b"\n"):
        raise ValueError("POSTRUN record is not LF-terminated")
    text = raw.decode("utf-8")
    if text.splitlines() != sorted(text.splitlines()):
        raise ValueError("POSTRUN record is not sorted")
    values = {}
    for line in text.splitlines():
        fields = line.split()
        if len(fields) != 4 or fields[:2] != ["EXP-CZ-002", "postrun"]:
            raise ValueError("POSTRUN record grammar is invalid")
        relative = Path(fields[2])
        if (relative.is_absolute() or ".." in relative.parts or len(relative.parts) != 3
                or relative.parts[0] != "set5" or len(fields[3]) != 64
                or any(character not in "0123456789abcdef" for character in fields[3])):
            raise ValueError("POSTRUN record path or digest is invalid")
        name = relative.name
        is_result = relative.suffix == ".json" and name not in {
            "timing-vram.json", "live-identity.json", "command.json"}
        is_ledger = relative.suffix == ".jsonl" and not name.endswith(".timing.jsonl")
        if not (is_result or is_ledger) or name in values:
            raise ValueError("POSTRUN record contains an unexpected or duplicate release file")
        values[name] = fields[3]
    if len(values) != 44:
        raise ValueError(f"POSTRUN record has {len(values)} release files instead of 44")
    return values


def exp002_spec():
    return {
        "repository_root": Path(__file__).parent.parent,
        "commitment_sha256": EXP002_COMMITMENT_SHA256,
        "sealed_task_count": 2400,
        "sealed_task_split": "sealed",
        "candidate_task_count": 3000,
        "final_per_cell": 120,
        "reviewed_input_sha256": EXP002_REVIEWED_INPUT_SHA256,
        "scorer_projection": EXP002_SCORER_PROJECTION,
        "coverage_4x": EXP002_4X_COVERAGE,
    }


EXP002_REVEAL_NAMES = {
    "AUDIT_GATE_RECEIPT.json",
    "FREEZE_RECORD-PREGEN.json",
    "FREEZE_RECORD-PRERUN.json",
    "GENERATION_SUMMARY.json",
    "KIT_MANIFEST.json",
    "POSTRUN_RECORD.txt",
    "SEALED_MANIFEST.json",
    "release-manifest.json",
    "sealed-s5-scored.jsonl",
    "sealed_salt.hex",
}


def exp002_reveal_inventory(d):
    try:
        entries = list(d.iterdir())
        valid = (
            len(entries) == len(EXP002_REVEAL_NAMES)
            and {entry.name for entry in entries} == EXP002_REVEAL_NAMES
            and all(entry.is_file() and not entry.is_symlink() for entry in entries)
        )
    except OSError as exc:
        return False, f"reveal inventory cannot be read ({type(exc).__name__}: {exc})"
    if valid:
        return True, "reveal inventory is exactly the ten expected regular non-symlink files"
    return False, "reveal inventory is not exactly the ten expected regular non-symlink files"


def exp002_task_identity_map(salt, count):
    """Recompute Forge v0.0.2 task identities without exposing task content."""
    families = ("arith_chain", "graph_reach", "json_extract", "list_transform")
    identities = {}
    for index in range(count):
        family = families[index % len(families)]
        difficulty = 1 + (index // len(families)) % 5
        tag = hmac.new(salt, f"sealed:{family}:{index}".encode(), hashlib.sha256).digest()
        seed = int.from_bytes(tag[:8], "big")
        text = f"cz.forge.v0.0.2|sealed|{family}|{difficulty}|{seed}".encode()
        identities[sha(text)[:16]] = (index, family, difficulty)
    return identities


def check_exp002(d, spec, release_asset):
    """Check the EXP-CZ-002 reveal, anchored records, and release asset offline."""
    reveal_inventory_ok, inventory_text = exp002_reveal_inventory(d)
    if not reveal_inventory_ok:
        return [("FAIL", inventory_text)]

    out = [("PASS", inventory_text)]

    def check(name, fn):
        try:
            ok = bool(fn())
        except (OSError, ValueError, KeyError, TypeError, UnicodeDecodeError,
                json.JSONDecodeError, tarfile.TarError) as exc:
            ok, name = False, f"{name} ({type(exc).__name__}: {exc})"
        out.append(("PASS" if ok else "FAIL", name))

    metadata = json.loads((d / "release-manifest.json").read_text(encoding="utf-8"))
    sealed_set = metadata["sealed_set"]
    root = Path(spec["repository_root"])
    commitment_paths = {
        name: root / name for name in spec["commitment_sha256"]
    }
    pregen_commitment = commitment_paths["commitments/EXP-CZ-002/COMMIT-PREGEN.txt"]
    prerun_commitment = commitment_paths["commitments/EXP-CZ-002/COMMIT-PRERUN.txt"]
    postrun_commitment = commitment_paths["commitments/EXP-CZ-002/POSTRUN.txt"]
    beacon_commitment = commitment_paths["commitments/EXP-CZ-002/BEACON.txt"]
    a5_commitment = commitment_paths["commitments/EXP-CZ-002/AMEND-A5.txt"]
    a6_commitment = commitment_paths["commitments/EXP-CZ-002/AMEND-A6.txt"]
    pregen_record = d / "FREEZE_RECORD-PREGEN.json"
    prerun_record = d / "FREEZE_RECORD-PRERUN.json"
    postrun_record = d / "POSTRUN_RECORD.txt"
    scored_path = d / "sealed-s5-scored.jsonl"
    salt_path = d / "sealed_salt.hex"
    kit = d / "KIT_MANIFEST.json"
    sealed_manifest = d / "SEALED_MANIFEST.json"
    generation_summary = d / "GENERATION_SUMMARY.json"
    audit_receipt = d / "AUDIT_GATE_RECEIPT.json"
    try:
        released = release_bytes(release_asset)
        release_error = None
    except (OSError, ValueError, tarfile.TarError) as exc:
        released, release_error = {}, str(exc)

    expected_manifest_fields = {
        "schema", "experiment", "sealed_set", "private_freeze_record_sha256",
        "sealed_task_file_sha256", "sealed_manifest_sha256", "sealed_task_count",
        "sealed_task_split", "commitment_files", "commitment_sha256",
        "generation_summary_sha256", "audit_gate_receipt_sha256",
        "postrun_record_sha256", "release_files", "reviewed_input_sha256",
    }
    check("release manifest has the exact public schema", lambda: (
        set(metadata) == expected_manifest_fields
        and set(sealed_set) == {"file", "sha256", "salt_file", "salt_commitment"}
        and metadata["schema"] == "cz.exp002.reveal.v1"
        and metadata["experiment"] == "EXP-CZ-002"
        and metadata["sealed_task_count"] == spec["sealed_task_count"]
        and metadata["sealed_task_split"] == spec["sealed_task_split"]
    ))
    check("scored set and salt use fixed local regular files", lambda: (
        sealed_set["file"] == "sealed-s5-scored.jsonl"
        and sealed_set["salt_file"] == "sealed_salt.hex"
        and scored_path.is_file() and not scored_path.is_symlink()
        and salt_path.is_file() and not salt_path.is_symlink()
    ))
    salt_text = salt_path.read_text(encoding="utf-8") if salt_path.is_file() and not salt_path.is_symlink() else ""
    check("sealed salt is exactly 64 lowercase hexadecimal characters with no newline", lambda: (
        len(salt_text) == 64 and all(character in "0123456789abcdef" for character in salt_text)
    ))
    check("scored sealed set matches its release-manifest hash", lambda: (
        sha(scored_path.read_bytes()) == sealed_set["sha256"]
        and sealed_set["sha256"] == metadata["sealed_task_file_sha256"]
    ))
    check("sealed salt matches its release-manifest commitment", lambda: sha(
        b"cz-salt-commit-v1|" + bytes.fromhex(salt_text)
    ) == sealed_set["salt_commitment"])

    check("all ten public commitment files match their anchored hashes", lambda: (
        all(path.is_file() and not path.is_symlink()
            and sha(path.read_bytes()) == spec["commitment_sha256"][name]
            for name, path in commitment_paths.items())
        and metadata["commitment_files"] == list(spec["commitment_sha256"])
        and metadata["commitment_sha256"] == spec["commitment_sha256"]
    ))
    check("release manifest pins the exact reviewed report, scorer, envelope, and amendment receipts", lambda: (
        metadata["reviewed_input_sha256"] == spec["reviewed_input_sha256"]
    ))
    pregen_json = json.loads(pregen_record.read_text(encoding="utf-8"))
    prerun_json = json.loads(prerun_record.read_text(encoding="utf-8"))
    check("PREGEN and PRERUN records match their anchored public digests", lambda: (
        sha(pregen_record.read_bytes()) == commitment_value(pregen_commitment, "private_freeze_record_sha256")
        and sha(prerun_record.read_bytes()) == commitment_value(prerun_commitment, "private_freeze_record_sha256")
    ))
    check("PRERUN chains to the anchored PREGEN commitment and record", lambda: (
        commitment_value(prerun_commitment, "commit_pregen_sha256") == sha(pregen_commitment.read_bytes())
        and metadata["private_freeze_record_sha256"] == sha(prerun_record.read_bytes())
    ))

    def records_have_only_allowed_changes():
        if pregen_json.get("phase") != "PREGEN" or prerun_json.get("phase") != "PRERUN":
            return False
        allowed = {"phase", "sealed_task_file_sha256", "sealed_manifest_sha256"}
        return (set(pregen_json) == set(prerun_json)
                and all(pregen_json[name] == prerun_json[name]
                        for name in pregen_json if name not in allowed))

    check("PREGEN and PRERUN differ only at the three authorized binding fields", records_have_only_allowed_changes)
    check("KIT_MANIFEST matches the canonical hash recorded before the run", lambda: (
        sha(canonical_json(json.loads(kit.read_bytes()))) == pregen_json["canonical_kit_manifest_sha256"]
    ))
    check("SEALED_MANIFEST matches the PRERUN record and release manifest", lambda: (
        sha(sealed_manifest.read_bytes()) == prerun_json["sealed_manifest_sha256"]
        and metadata["sealed_manifest_sha256"] == prerun_json["sealed_manifest_sha256"]
        and json.loads(sealed_manifest.read_bytes()) == {
            "exp_id": "EXP-CZ-002",
            "schema": "cz.manifest.v1",
            "task_spec": {"sealed_file_sha256": sealed_set["sha256"], "split": "sealed"},
        }
    ))
    check("PRERUN record binds the released scored set", lambda: (
        prerun_json["sealed_task_file_sha256"] == sealed_set["sha256"]
        and prerun_json["sealed_task_file_sha256"] == metadata["sealed_task_file_sha256"]
    ))
    check("PRERUN record binds the released task count and split", lambda: (
        prerun_json["sealed_task_count"] == metadata["sealed_task_count"] == spec["sealed_task_count"]
        and prerun_json["sealed_task_split"] == metadata["sealed_task_split"] == spec["sealed_task_split"]
    ))

    summary_raw = generation_summary.read_bytes()
    receipt_raw = audit_receipt.read_bytes()
    summary_json = json.loads(summary_raw)
    receipt_json = json.loads(receipt_raw)
    check("attempt-005 audit receipt binds the canonical generation summary", lambda: (
        summary_raw == canonical_json(summary_json) + b"\n"
        and receipt_raw == canonical_json(receipt_json) + b"\n"
        and metadata["generation_summary_sha256"] == sha(summary_raw)
        and metadata["audit_gate_receipt_sha256"] == sha(receipt_raw)
        and receipt_json == {
            "schema": "cz.exp002.audit-gate-receipt.v1",
            "attempt": "005",
            "gate_id": "exp002-sealed5-audit-attempt-005",
            "approved": True,
            "generation_summary_sha256": sha(summary_raw),
        }
    ))
    families = ("arith_chain", "graph_reach", "json_extract", "list_transform")
    cells = {f"{family}/{difficulty}": spec["final_per_cell"]
             for family in families for difficulty in range(1, 6)}
    check("generation summary describes the committed balanced scored set", lambda: (
        summary_json["schema"] == "cz.exp002.sealed5-summary.v1"
        and summary_json["attempt"] == "005"
        and summary_json["status"] == "PASS"
        and summary_json["sealed_task_file_sha256"] == sealed_set["sha256"]
        and summary_json["n_candidates"] == spec["candidate_task_count"]
        and summary_json["n_final"] == spec["sealed_task_count"]
        and summary_json["split_counts"] == {"sealed": spec["sealed_task_count"]}
        and summary_json["family_counts"] == {
            family: spec["sealed_task_count"] // len(families) for family in families}
        and summary_json["final_per_cell"] == cells
    ))

    def scored_identities_reproduce():
        raw = scored_path.read_bytes()
        lines = raw.splitlines(keepends=True)
        if len(lines) != spec["sealed_task_count"] or not raw.endswith(b"\n"):
            return False
        identities = exp002_task_identity_map(bytes.fromhex(salt_text), spec["candidate_task_count"])
        previous = -1
        observed = {cell: 0 for cell in cells}
        seen = set()
        for line in lines:
            row = json.loads(line)
            if line != canonical_json(row) + b"\n" or set(row) != {
                    "difficulty", "family", "params", "prompt", "reference", "split", "task_id"}:
                return False
            identity = identities.get(row["task_id"])
            if (identity is None or row["task_id"] in seen or row["split"] != "sealed"
                    or identity[1:] != (row["family"], row["difficulty"]) or identity[0] <= previous):
                return False
            seen.add(row["task_id"])
            previous = identity[0]
            observed[f"{row['family']}/{row['difficulty']}"] += 1
        return observed == cells

    check("scored task identities reproduce from the salt under Forge v0.0.2", scored_identities_reproduce)
    postrun_raw = postrun_record.read_bytes()
    check("published POSTRUN record matches its anchored digest", lambda: (
        sha(postrun_raw) == commitment_value(postrun_commitment, "private_postrun_record_sha256")
        and metadata["postrun_record_sha256"] == sha(postrun_raw)
    ))
    check("release asset is the exact 46-file manifest inventory", lambda: (
        release_error is None
        and set(released) == set(metadata["release_files"])
        and metadata["release_files"] == {name: sha(raw) for name, raw in sorted(released.items())}
    ))
    check("POSTRUN digest list matches all 44 released result and ledger files", lambda: (
        (postrun_hashes := exp002_postrun_hashes(postrun_raw))
        and set(released) == set(postrun_hashes) | {"scorer.json", "SCORING_ENVELOPE.json"}
        and all(sha(released[name]) == digest for name, digest in postrun_hashes.items())
    ))

    def scoring_bindings_match():
        scorer_raw = released["scorer.json"]
        envelope_raw = released["SCORING_ENVELOPE.json"]
        scorer = json.loads(scorer_raw)
        envelope = json.loads(envelope_raw)
        fields = {
            "amendment_a5_receipt_sha256", "freeze_record_sha256",
            "private_beacon_record_sha256", "private_postrun_record_sha256", "schema",
            "scorer_binary_sha256", "scorer_json_sha256",
            "scorer_replacement_descriptor_sha256", "sealed_task_file_sha256",
        }
        digests = fields - {"schema"}
        if (set(envelope) != fields or envelope_raw != canonical_json(envelope) + b"\n"
                or envelope.get("schema") != "cz.exp002.scoring-envelope-a5.v1"
                or any(not isinstance(envelope.get(field), str) or len(envelope[field]) != 64
                       or any(character not in "0123456789abcdef" for character in envelope[field])
                       for field in digests)
                or not isinstance(scorer, dict)
                or scorer.get("schema") != "cz.exp002.union-budget-score.v1"):
            return False
        a5_new = commitment_value(a5_commitment, "new_scorer_sha256")
        a6_new = commitment_value(a6_commitment, "new_scorer_sha256")
        a5_old = commitment_value(a5_commitment, "old_scorer_sha256")
        a6_old = commitment_value(a6_commitment, "old_scorer_sha256")
        a5_descriptor = commitment_value(a5_commitment, "scorer_replacement_descriptor_sha256")
        a6_descriptor = commitment_value(a6_commitment, "scorer_replacement_descriptor_sha256")
        return (
            sha(scorer_raw) == spec["reviewed_input_sha256"]["scorer.json"]
            and sha(envelope_raw) == spec["reviewed_input_sha256"]["SCORING_ENVELOPE.json"]
            and a5_new == a6_new == envelope["scorer_binary_sha256"]
            and a5_old == a6_old
            and a5_descriptor == a6_descriptor == envelope["scorer_replacement_descriptor_sha256"]
            and envelope["amendment_a5_receipt_sha256"]
            == spec["reviewed_input_sha256"]["amend-a5-receipt.json"]
            and envelope["scorer_json_sha256"] == sha(scorer_raw)
            and envelope["freeze_record_sha256"] == sha(prerun_record.read_bytes())
            and envelope["private_postrun_record_sha256"] == sha(postrun_raw)
            and envelope["private_beacon_record_sha256"] == commitment_value(
                beacon_commitment, "private_beacon_record_sha256")
            and envelope["sealed_task_file_sha256"] == sealed_set["sha256"]
        )

    check("scorer and envelope match PRERUN, POSTRUN, BEACON, A5, and A6", scoring_bindings_match)

    def scorer_projection_matches():
        scorer = json.loads(released["scorer.json"])
        endpoints = scorer["endpoints"]
        for endpoint_id, expected in spec["scorer_projection"].items():
            row = endpoints[endpoint_id]
            if row["status"] != expected["status"]:
                return False
            if endpoint_id == "H2.2":
                continue
            values = row["endpoint"] if endpoint_id == "H2.1" else row
            if values["gain"] != expected["gain"] or values["p"] != expected["p"]:
                return False
            if "p_holm" in expected and values["holm"]["p_holm"] != expected["p_holm"]:
                return False
        metrics = scorer["reported_metrics"]
        return all(metrics[arm]["4x"]["coverage"] == coverage
                   for arm, coverage in spec["coverage_4x"].items())

    check("scorer matches the fixed public H2 results and T3/U_tool 4x coverage", scorer_projection_matches)
    return out


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


def verify(folder, expected=None, release_asset=None):
    top = Path(folder)
    is_exp002 = top.name == "EXP-CZ-002"
    if not is_exp002 and top.joinpath("release-manifest.json").exists():
        inventory_ok, inventory_text = exp002_reveal_inventory(top)
        if not inventory_ok:
            print("EXP-CZ-002")
            print(f"  FAIL {inventory_text}")
            return 1
        try:
            is_exp002 = json.loads(top.joinpath("release-manifest.json").read_text()).get("experiment") == "EXP-CZ-002"
        except (OSError, ValueError, AttributeError):
            pass
    if is_exp002:
        print("EXP-CZ-002")
        if release_asset is None:
            print("  FAIL release asset path is required for EXP-CZ-002")
            return 1
        checks = check_exp002(top, expected or exp002_spec(), release_asset)
        for status, text in checks:
            print(f"  {status} {text}")
        return 0 if all(status != "FAIL" for status, _ in checks) else 1

    expected = expected or EXPECTED
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

    def run(folder, expected, release_asset=None):
        if release_asset is None and isinstance(expected, dict):
            release_asset = expected.get("release_asset")
        with contextlib.redirect_stdout(io.StringIO()) as buf:
            code = verify(folder, expected, release_asset)
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

    def build_exp002_fixture(top):
        salt = bytes.fromhex("00" * 32)
        salt_text = salt.hex()
        task_split = "sealed"
        families = ("arith_chain", "graph_reach", "json_extract", "list_transform")
        identities = exp002_task_identity_map(salt, 20)
        by_index = sorted((index, task_id, family, difficulty)
                          for task_id, (index, family, difficulty) in identities.items())
        rows = [{
            "difficulty": difficulty,
            "family": family,
            "params": {"fixture": index},
            "prompt": f"fixture prompt {index}",
            "reference": "fixture",
            "split": "sealed",
            "task_id": task_id,
        } for index, task_id, family, difficulty in by_index]
        sealed = b"".join(canonical_json(row) + b"\n" for row in rows)
        kit_json = {"kit": "fixture", "version": 1}
        sealed_manifest_json = {
            "exp_id": "EXP-CZ-002",
            "schema": "cz.manifest.v1",
            "task_spec": {"sealed_file_sha256": sha(sealed), "split": "sealed"},
        }
        kit_raw = json.dumps(kit_json, indent=2).encode("utf-8")
        sealed_manifest_raw = json.dumps(sealed_manifest_json, indent=2).encode("utf-8")
        frozen = {
            "phase": "PREGEN",
            "sealed_task_file_sha256": "0" * 64,
            "sealed_manifest_sha256": "0" * 64,
            "sealed_task_count": 20,
            "sealed_task_split": task_split,
            "canonical_kit_manifest_sha256": sha(canonical_json(kit_json)),
            "executor_sha256": "3" * 64,
            "worker_binary_sha256": "4" * 64,
            "probe_binary_sha256": "5" * 64,
            "text_probe_binary_sha256": "6" * 64,
            "union_and_budget_cut_scorer_sha256": "7" * 64,
        }
        pregen_raw = canonical_json(frozen)
        prerun_json = {
            **frozen,
            "phase": "PRERUN",
            "sealed_manifest_sha256": sha(sealed_manifest_raw),
            "sealed_task_file_sha256": sha(sealed),
        }
        prerun_raw = canonical_json(prerun_json)
        pregen_commitment = f"private_freeze_record_sha256 {sha(pregen_raw)}\n".encode("utf-8")
        prerun_commitment = (
            f"private_freeze_record_sha256 {sha(prerun_raw)}\n"
            f"commit_pregen_sha256 {sha(pregen_commitment)}\n"
        ).encode("utf-8")
        release = top.parent / "fixture-release"
        release.mkdir()
        postrun_lines = []
        for number in range(1, 23):
            result_name = f"tuple-{number:02d}-result.json"
            ledger_name = f"tuple-{number:02d}-ledger.jsonl"
            result_raw = json.dumps({"fixture": result_name}, sort_keys=True).encode() + b"\n"
            ledger_raw = json.dumps({"fixture": ledger_name}, sort_keys=True).encode() + b"\n"
            release.joinpath(result_name).write_bytes(result_raw)
            release.joinpath(ledger_name).write_bytes(ledger_raw)
            postrun_lines.extend((
                f"EXP-CZ-002 postrun set5/tuple-{number:02d}/{result_name} {sha(result_raw)}",
                f"EXP-CZ-002 postrun set5/tuple-{number:02d}/{ledger_name} {sha(ledger_raw)}",
            ))
        postrun_raw = ("\n".join(sorted(postrun_lines)) + "\n").encode()
        postrun_commitment = f"private_postrun_record_sha256 {sha(postrun_raw)}\n".encode()
        beacon_private_sha = "b" * 64
        beacon_commitment = f"private_beacon_record_sha256 {beacon_private_sha}\n".encode()
        old_scorer = "4" * 64
        replacement_scorer = "2" * 64
        descriptor = "3" * 64
        amendments = {
            f"AMEND-A{number}.txt": f"amendment_id A{number}\nfixture_sha256 {'0' * 64}\n".encode()
            for number in range(1, 5)
        }
        amendments["AMEND-A5.txt"] = (
            f"amendment_id A5\nold_scorer_sha256 {old_scorer}\n"
            f"new_scorer_sha256 {replacement_scorer}\n"
            f"scorer_replacement_descriptor_sha256 {descriptor}\n"
        ).encode()
        amendments["AMEND-A6.txt"] = (
            f"amendment_id A6\nold_scorer_sha256 {old_scorer}\n"
            f"new_scorer_sha256 {replacement_scorer}\n"
            f"scorer_replacement_descriptor_sha256 {descriptor}\n"
        ).encode()
        scorer_fixture = {
            "schema": "cz.exp002.union-budget-score.v1",
            "endpoints": {
                "H2.1": {
                    "endpoint": {"gain": 0.07583333333333334, "p": 1.8567069153217267e-14},
                    "status": "SUPPORTED",
                },
                "H2.2": {"status": "SUPPORTED"},
                "H2.2.decomposable": {
                    "gain": 0.2841666666666667,
                    "holm": {"p_holm": 3.5153049955808323e-82},
                    "p": 8.788262488952081e-83,
                    "status": "SUPPORTED",
                },
                "H2.2.sequential": {
                    "gain": 0.26916666666666667,
                    "holm": {"p_holm": 5.185125226219e-81},
                    "p": 1.7283750754063332e-81,
                    "status": "SUPPORTED",
                },
                "H2.3": {
                    "gain": 0.0,
                    "holm": {"p_holm": 1.0},
                    "p": 1.0,
                    "status": "NOT_SUPPORTED",
                },
                "H2.4": {
                    "gain": 0.13666666666666666,
                    "holm": {"p_holm": 6.318320000269288e-95},
                    "p": 1.2636640000538576e-95,
                    "status": "SUPPORTED",
                },
                "H2.5": {
                    "gain": 0.1,
                    "holm": {"p_holm": 1.4144119620981756e-15},
                    "p": 7.072059810490878e-16,
                    "status": "SUPPORTED",
                },
            },
            "reported_metrics": {
                "T3": {"4x": {"coverage": 0.81625}},
                "U_tool": {"4x": {"coverage": 0.7404166666666666}},
            },
        }
        scorer_raw = canonical_json(scorer_fixture) + b"\n"
        envelope = {
            "amendment_a5_receipt_sha256": "1" * 64,
            "freeze_record_sha256": sha(prerun_raw),
            "private_beacon_record_sha256": beacon_private_sha,
            "private_postrun_record_sha256": sha(postrun_raw),
            "schema": "cz.exp002.scoring-envelope-a5.v1",
            "scorer_binary_sha256": replacement_scorer,
            "scorer_json_sha256": sha(scorer_raw),
            "scorer_replacement_descriptor_sha256": descriptor,
            "sealed_task_file_sha256": sha(sealed),
        }
        envelope_raw = canonical_json(envelope) + b"\n"
        release.joinpath("scorer.json").write_bytes(scorer_raw)
        release.joinpath("SCORING_ENVELOPE.json").write_bytes(envelope_raw)
        reviewed_input_sha256 = {
            "REPORT.md": "9" * 64,
            "scorer.json": sha(scorer_raw),
            "SCORING_ENVELOPE.json": sha(envelope_raw),
            "amend-a5-receipt.json": "1" * 64,
            "amend-a6-receipt.json": "5" * 64,
        }
        commitment_raw = {
            "commitments/EXP-CZ-002/COMMIT-PREGEN.txt": pregen_commitment,
            "commitments/EXP-CZ-002/COMMIT-PRERUN.txt": prerun_commitment,
            "commitments/EXP-CZ-002/POSTRUN.txt": postrun_commitment,
            "commitments/EXP-CZ-002/BEACON.txt": beacon_commitment,
            **{f"commitments/EXP-CZ-002/{name}": raw for name, raw in amendments.items()},
        }
        commitment_sha256 = {name: sha(raw) for name, raw in commitment_raw.items()}
        metadata = {
            "schema": "cz.exp002.reveal.v1",
            "experiment": "EXP-CZ-002",
            "sealed_set": {
                "file": "sealed-s5-scored.jsonl",
                "sha256": sha(sealed),
                "salt_file": "sealed_salt.hex",
                "salt_commitment": sha(b"cz-salt-commit-v1|" + salt),
            },
            "private_freeze_record_sha256": sha(prerun_raw),
            "sealed_task_file_sha256": sha(sealed),
            "sealed_manifest_sha256": sha(sealed_manifest_raw),
            "sealed_task_count": 20,
            "sealed_task_split": task_split,
            "commitment_files": list(commitment_sha256),
            "commitment_sha256": commitment_sha256,
            "postrun_record_sha256": sha(postrun_raw),
            "release_files": {
                path.name: sha(path.read_bytes()) for path in sorted(release.iterdir())
            },
            "reviewed_input_sha256": reviewed_input_sha256,
        }
        generation = {
            "schema": "cz.exp002.sealed5-summary.v1",
            "attempt": "005",
            "status": "PASS",
            "sealed_task_file_sha256": sha(sealed),
            "n_candidates": 20,
            "n_final": 20,
            "split_counts": {"sealed": 20},
            "family_counts": {family: 5 for family in families},
            "final_per_cell": {f"{family}/{difficulty}": 1 for family in families for difficulty in range(1, 6)},
        }
        generation_raw = canonical_json(generation) + b"\n"
        receipt = {
            "schema": "cz.exp002.audit-gate-receipt.v1",
            "attempt": "005",
            "gate_id": "exp002-sealed5-audit-attempt-005",
            "approved": True,
            "generation_summary_sha256": sha(generation_raw),
        }
        receipt_raw = canonical_json(receipt) + b"\n"
        metadata["generation_summary_sha256"] = sha(generation_raw)
        metadata["audit_gate_receipt_sha256"] = sha(receipt_raw)
        top.joinpath("sealed-s5-scored.jsonl").write_bytes(sealed)
        top.joinpath("sealed_salt.hex").write_text(salt_text, encoding="utf-8")
        top.joinpath("release-manifest.json").write_text(json.dumps(metadata), encoding="utf-8")
        top.joinpath("FREEZE_RECORD-PREGEN.json").write_bytes(pregen_raw)
        top.joinpath("FREEZE_RECORD-PRERUN.json").write_bytes(prerun_raw)
        top.joinpath("KIT_MANIFEST.json").write_bytes(kit_raw)
        top.joinpath("SEALED_MANIFEST.json").write_bytes(sealed_manifest_raw)
        top.joinpath("GENERATION_SUMMARY.json").write_bytes(generation_raw)
        top.joinpath("AUDIT_GATE_RECEIPT.json").write_bytes(receipt_raw)
        top.joinpath("POSTRUN_RECORD.txt").write_bytes(postrun_raw)
        fixture_root = top.parent / "fixture-public"
        fixture_root.joinpath("commitments", "EXP-CZ-002").mkdir(parents=True)
        for name, raw in commitment_raw.items():
            fixture_root.joinpath(name).write_bytes(raw)
        return {
            "repository_root": fixture_root,
            "commitment_sha256": commitment_sha256,
            "release_asset": release,
            "sealed_task_count": 20,
            "sealed_task_split": task_split,
            "candidate_task_count": 20,
            "final_per_cell": 1,
            "reviewed_input_sha256": reviewed_input_sha256,
            "scorer_projection": EXP002_SCORER_PROJECTION,
            "coverage_4x": EXP002_4X_COVERAGE,
        }

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

        # 4. EXP-CZ-002 binds its reveal, ten public records, and release asset.
        exp002 = tmp / "EXP-CZ-002"
        exp002.mkdir()
        exp002_expected = build_exp002_fixture(exp002)
        code, text = run(exp002, exp002_expected)
        if code != 0 or text.count("PASS") != 23:
            failures.append("EXP-CZ-002 fixture should pass 23 checks:\n" + text)

        extra = exp002 / "unexpected.txt"
        extra.write_text("unexpected\n", encoding="utf-8")
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("extra EXP-CZ-002 reveal file was not rejected")
        extra.unlink()

        kit_path = exp002 / "KIT_MANIFEST.json"
        kit_raw = kit_path.read_bytes()
        external_kit = tmp / "external-KIT_MANIFEST.json"
        external_kit.write_bytes(kit_raw)
        kit_path.unlink()
        kit_path.symlink_to(external_kit)
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("symlinked EXP-CZ-002 KIT_MANIFEST.json was not rejected")
        kit_path.unlink()
        kit_path.write_bytes(kit_raw)

        release_fixture = exp002_expected["release_asset"]
        release_tar = tmp / "fixture-release.tar.gz"
        with tarfile.open(release_tar, mode="w:gz") as package:
            package.add(release_fixture, arcname=".")
        tar_expected = {**exp002_expected, "release_asset": release_tar}
        code, text = run(exp002, tar_expected)
        if code != 0 or text.count("PASS") != 23:
            failures.append("EXP-CZ-002 tarball fixture should pass 23 checks:\n" + text)

        for name in ("tuple-01-result.json", "scorer.json", "SCORING_ENVELOPE.json"):
            target = release_fixture / name
            original = target.read_bytes()
            target.write_bytes(original + b"changed\n")
            code, text = run(exp002, exp002_expected)
            if code == 0:
                failures.append(f"tampered EXP-CZ-002 release member {name} was not detected")
            target.write_bytes(original)

        # Rewriting the scorer, envelope, and release manifest together must not
        # replace the reviewed scoring bytes or the fixed public result values.
        scorer_path = release_fixture / "scorer.json"
        envelope_path = release_fixture / "SCORING_ENVELOPE.json"
        metadata_path = exp002 / "release-manifest.json"
        scorer_original = scorer_path.read_bytes()
        envelope_original = envelope_path.read_bytes()
        metadata_original = metadata_path.read_bytes()
        scorer_json = json.loads(scorer_original)
        scorer_json["endpoints"]["H2.1"]["endpoint"]["gain"] = 0.2
        scorer_path.write_bytes(canonical_json(scorer_json) + b"\n")
        envelope_json = json.loads(envelope_original)
        envelope_json["scorer_json_sha256"] = sha(scorer_path.read_bytes())
        envelope_path.write_bytes(canonical_json(envelope_json) + b"\n")
        metadata = json.loads(metadata_original)
        metadata["release_files"]["scorer.json"] = sha(scorer_path.read_bytes())
        metadata["release_files"]["SCORING_ENVELOPE.json"] = sha(envelope_path.read_bytes())
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("coordinated EXP-CZ-002 scorer, envelope, and manifest rewrite was not detected")
        scorer_path.write_bytes(scorer_original)
        envelope_path.write_bytes(envelope_original)
        metadata_path.write_bytes(metadata_original)

        a5_path = (exp002_expected["repository_root"] / "commitments" /
                   "EXP-CZ-002" / "AMEND-A5.txt")
        a5_original = a5_path.read_bytes()
        a5_path.write_bytes(a5_original + b"changed\n")
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("tampered EXP-CZ-002 A5 commitment was not detected")
        a5_path.write_bytes(a5_original)

        # The scored-set locator is part of the public contract. It cannot point
        # outside the reveal, traverse, or resolve through a symlink.
        local_scored = exp002 / "sealed-s5-scored.jsonl"
        external_scored = tmp / "external-scored.jsonl"
        external_scored.write_bytes(local_scored.read_bytes())
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["sealed_set"]["file"] = str(external_scored)
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        local_bytes = local_scored.read_bytes()
        local_scored.unlink()
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("absolute external EXP-CZ-002 scored-set locator was not rejected")
        local_scored.write_bytes(local_bytes)
        metadata["sealed_set"]["file"] = "../external-scored.jsonl"
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("traversing EXP-CZ-002 scored-set locator was not rejected")
        metadata["sealed_set"]["file"] = "sealed-s5-scored.jsonl"
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        local_scored.unlink()
        local_scored.symlink_to(external_scored)
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("symlinked EXP-CZ-002 scored set was not rejected")
        local_scored.unlink()
        local_scored.write_bytes(local_bytes)

        # Rewriting both commitment files and the manifest's current hashes must
        # not replace the hashes that were anchored before publication.
        fixture_root = exp002_expected["repository_root"]
        pregen_path = fixture_root / "commitments" / "EXP-CZ-002" / "COMMIT-PREGEN.txt"
        prerun_path = fixture_root / "commitments" / "EXP-CZ-002" / "COMMIT-PRERUN.txt"
        pregen_original = pregen_path.read_bytes()
        prerun_original = prerun_path.read_bytes()
        metadata_original = metadata_path.read_bytes()
        pregen_path.write_bytes(pregen_original + b"extra ignored\n")
        prerun_lines = prerun_path.read_text(encoding="utf-8").splitlines()
        prerun_lines[1] = f"commit_pregen_sha256 {sha(pregen_path.read_bytes())}"
        prerun_path.write_text("\n".join(prerun_lines) + "\n", encoding="utf-8")
        metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
        metadata["commitment_sha256"] = {
            "commitments/EXP-CZ-002/COMMIT-PREGEN.txt": sha(pregen_path.read_bytes()),
            "commitments/EXP-CZ-002/COMMIT-PRERUN.txt": sha(prerun_path.read_bytes()),
        }
        metadata_path.write_text(json.dumps(metadata), encoding="utf-8")
        code, text = run(exp002, exp002_expected)
        if code == 0:
            failures.append("rewritten EXP-CZ-002 PREGEN/PRERUN commitments were not rejected")

        # Restore the fixture before the independent sealed-byte tamper.
        pregen_path.write_bytes(pregen_original)
        prerun_path.write_bytes(prerun_original)
        metadata_path.write_bytes(metadata_original)
        exp002.joinpath("sealed-s5-scored.jsonl").write_text("changed\n", encoding="utf-8")
        code, text = run(exp002, exp002_expected)
        if code == 0 or "scored sealed set matches" not in text:
            failures.append("tampered EXP-CZ-002 scored set was not detected:\n" + text)
    for f in failures:
        print("SELF-TEST FAIL " + f)
    print("self-test: " + ("PASS" if not failures else f"{len(failures)} failure(s)"))
    return 0 if not failures else 1


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else "reveal/EXP-CZ-001"
    release = sys.argv[2] if len(sys.argv) > 2 else None
    sys.exit(self_test() if arg == "--self-test" else verify(arg, release_asset=release))
