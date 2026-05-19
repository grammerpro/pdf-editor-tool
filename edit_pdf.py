#!/usr/bin/env python3
"""Simple PDF editor with merge, watermark, and signature capabilities."""

import sys
import argparse
from pathlib import Path

def merge_pdfs(input_paths, output_path):
    """Placeholder for merging PDFs – prints what would happen."""
    print(f"[PLACEHOLDER] Merging PDFs: {input_paths} → {output_path}")

def add_watermark(input_path, output_path, text):
    """Placeholder for adding a text watermark."""
    print(f"[PLACEHOLDER] Adding watermark '{text}' to {input_path} → {output_path}")

def add_signature(input_path, signature_path, output_path):
    """Placeholder for overlaying a signature image."""
    sig_name = Path(signature_path).name
    print(f"[PLACEHOLDER] Adding signature image '{sig_name}' to {input_path} → {output_path}")

def main():
    parser = argparse.ArgumentParser(description="Simple PDF editor")
    sub = parser.add_subparsers(dest="command", required=True)

    # merge command
    merge_p = sub.add_parser("merge", help="Merge multiple PDFs into one")
    merge_p.add_argument("inputs", nargs="+", help="Input PDF files")
    merge_p.add_argument("-o", "--output", required=True, help="Output merged PDF")
    merge_p.set_defaults(func=lambda ns: merge_pdfs(ns.inputs, ns.output))

    # watermark command
    wat_p = sub.add_parser("watermark", help="Add a text watermark")
    wat_p.add_argument("input", help="Input PDF file")
    wat_p.add_argument("-o", "--output", required=True, help="Output PDF file")
    wat_p.add_argument("--watermark", required=True, help="Watermark text")
    wat_p.set_defaults(func=lambda ns: add_watermark(ns.input, ns.output, ns.watermark))

    # sign command
    sign_p = sub.add_parser("sign", help="Overlay a signature image")
    sign_p.add_argument("input", help="Input PDF file")
    sign_p.add_argument("--signature", required=True, help="Signature image file")
    sign_p.add_argument("-o", "--output", required=True, help="Output signed PDF")
    sign_p.set_defaults(func=lambda ns: add_signature(ns.input, ns.signature, ns.output))

    # Parse and run
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()