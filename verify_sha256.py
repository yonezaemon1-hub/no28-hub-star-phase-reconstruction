from pathlib import Path
import hashlib
import sys

root = Path(__file__).resolve().parent
errors = []
for line in (root / 'SHA256SUMS').read_text(encoding='utf-8').splitlines():
    if not line.strip():
        continue
    expected, name = line.split('  ', 1)
    path = root / name
    got = hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None
    ok = got == expected
    print(('PASS' if ok else 'FAIL') + ' ' + name)
    if not ok:
        errors.append(name)
print('RESULT=' + ('PASS' if not errors else 'FAIL'))
sys.exit(1 if errors else 0)
