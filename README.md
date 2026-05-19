# PDF Editor with Signature Support

A lightweight, open‑source PDF editor that can:

- **Merge** multiple PDFs into one.
- Add a **text watermark** to any page.
- Overlay a **signature image** onto the last page of a PDF.

No Adobe Acrobat or DocuSign required – just Python and a few free libraries.

## Requirements

- Python 3.8+
- `pypdf` – PDF reading/writing
- `pillow` – Image handling (for signature overlay)

Install the dependencies with:

```bash
pip install pypdf pillow
```

## Usage

```bash
# Merge PDFs
python edit_pdf.py merge input1.pdf input2.pdf -o merged.pdf

# Add a watermark
python edit_pdf.py watermark input.pdf -o watermarked.pdf --watermark "CONFIDENTIAL"

# Add a signature image (e.g., signature.png) to the last page
python edit_pdf.py sign input.pdf --signature signature.png -o signed.pdf
```

## License

MIT – feel free to use, modify, and distribute.