"""Verify all shipped payload hashes, independently of the math verifier."""
import hashlib
from pathlib import Path, PurePosixPath
import sys


def main():
    root = Path(__file__).resolve().parent
    count = 0
    for line in (root / 'SHA256SUMS.txt').read_text(encoding='utf-8').splitlines():
        if not line:
            continue
        expected, name = line.split('  ', 1)
        rel = PurePosixPath(name)
        if rel.is_absolute() or '..' in rel.parts:
            raise ValueError('Unsafe manifest path')
        actual = hashlib.sha256(root.joinpath(*rel.parts).read_bytes()).hexdigest()
        if actual != expected:
            print('FAIL', name)
            return 1
        count += 1
    print(f'PASS SHA256 {count}/{count} payload files')
    return 0


if __name__ == '__main__':
    sys.exit(main())
