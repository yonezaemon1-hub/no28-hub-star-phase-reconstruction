# No.28 — Restricted Hub-Star Phase Reconstruction (archival research record)

**Author:** Ryutaro Yonezu / Yonezu Research Lab  
**Publication version:** Archival v1.0, prepared 2026-10-17  
**Manuscript:** `No28_Restricted_HubStar_Research_Record_20261017.pdf`  
**Type:** Unrefereed, explicitly INCONCLUSIVE research record. **Not a validated novel paper.**

## Public status statement

- **CONDITIONAL PASS, model restricted:** An exact ternary-reset second-jet encoding of a target binary leaf edge and a normalized fixed-horizon two-graph Gaussian observation lower bound, *within the assumed binary hub-star Kuramoto model*.
- **NOT FULLY PROVED:** A raw-hub-phase sample-complexity upper estimate exists only as an analytic proof outline; its full constants and analytic prerequisites are not independently certified.
- **Novelty:** INCONCLUSIVE; conceptual overlap with established oscillator-network inference, partial observation and spectral differentiation is substantial. No first-discovery, novelty or priority claims.
- **Review:** Internal algebraic checks and re-runs only. No independent external human or second-model audit of the final evidence bundle. Not peer reviewed.
- **Scope:** No hardware validation, no general all-m two-binary-probe solution, no generic weighted/frequency-unknown/noisy-reset recovery claim.

### Disposition override (2026-10-17)

The immutable original audit (`No28_FINAL_AUDIT_DECISION_20261016.zip`) said **publication HOLD pending owner authorization/external review**. On 2026-10-17 the author **authorized dissemination specifically as an INCONCLUSIVE archival record with these limitations**. The original HOLD decision is preserved unchanged; author authorization changes the **posting decision**, not the validation, mathematics, or novelty judgement.

## Files

- `No28_Restricted_HubStar_Research_Record_20261017.pdf` — standalone 4-page English research record.
- `No28_Restricted_HubStar_Research_Record_20261017.tex` — TeX manuscript source.
- `No28_FINAL_AUDIT_DECISION_20261016.zip` — **byte-for-byte unchanged** 2026-10-16 audit closure with 5 evidence ZIPs, code, audit, symbolic checker, prior simulator outputs and internal SHA256 manifests.
- `PUBLICATION_METADATA.md` — suggested archive metadata including reference list.
- `SHA256SUMS` — hashes of all above files and verification code (excluding manifest itself).
- `verify_sha256.py` — no-dependency manifest checker for Python 3.12 on Windows 10 or other OS.

**PDF integrity note (2026-10-18):** The GitHub PDF has a different byte hash from the original PDF contained in the 2026-10-17 archival preparation ZIP, but the four extracted-text pages and all four rasterized pages compare exactly at 1.5× rendering. The repository `SHA256SUMS` records the **GitHub-published PDF bytes**, not the original preparation-ZIP PDF bytes; the TeX source and original closure-audit ZIP remain byte-identical to their archived copies. This distinction affects file provenance, not the stated research status.

## Reproducibility

Run `python verify_sha256.py` within this directory. To run the algebra checker, unpack the evidence ZIP and run its `independent_equation_check.py` (requires SymPy). Previous numerical results in nested ZIPs may need SciPy; the check of original evidence integrity does not.

**Contact:** yonezaemon1+research@gmail.com  
**Rights:** All rights reserved. No open-source or redistribution license granted beyond rights otherwise provided by law.

**Important:** Creation of this publication package does not itself establish upload to GitHub, Zenodo, or any issued DOI. A published location must be independently verified.
