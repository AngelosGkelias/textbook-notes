#!/usr/bin/env python3
"""Compile native Typst sources using the CLI or this interpreter's binding."""

import argparse
from pathlib import Path
import shutil
import subprocess
import tempfile


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", required=True, type=Path)
    parser.add_argument("source", type=Path)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    root, source, output = (p.resolve() for p in (args.root, args.source, args.output))
    output.parent.mkdir(parents=True, exist_ok=True)

    try:
        with tempfile.TemporaryDirectory(prefix=".typst-build-", dir=output.parent) as staging:
            pdf = Path(staging) / "compiled.pdf"
            cli = shutil.which("typst")
            if cli:
                subprocess.run([cli, "compile", "--root", str(root), str(source), str(pdf)], check=True)
                backend = "Typst CLI"
            else:
                try:
                    import typst
                except ImportError:
                    parser.exit(1, "No Typst CLI or Python typst binding is available.\n")
                pdf.write_bytes(typst.compile(str(source), root=str(root)))
                backend = "Python typst binding"
            if not pdf.read_bytes().startswith(b"%PDF-"):
                raise ValueError("Compiler did not produce a PDF")
            pdf.replace(output)
    except Exception as error:
        parser.exit(1, f"Native Typst build failed: {error}\n")
    print(f"Compiled {source} -> {output} with {backend}")


if __name__ == "__main__":
    main()
