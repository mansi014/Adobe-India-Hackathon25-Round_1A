import os
import fitz  # PyMuPDF
import json
from pathlib import Path

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = []
    title = doc.metadata.get("title", Path(pdf_path).stem)

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    size = span["size"]
                    font = span["font"]
                    text = span["text"].strip()

                    if not text:
                        continue

                    level = None
                    if size > 20:
                        level = "H1"
                    elif 15 < size <= 20:
                        level = "H2"
                    elif 12 < size <= 15:
                        level = "H3"

                    if level:
                        outline.append({
                            "level": level,
                            "text": text,
                            "page": page_num + 1
                        })

    return {"title": title, "outline": outline}

def main():
    input_dir = Path("/app/input")
    output_dir = Path("/app/output")
    output_dir.mkdir(parents=True, exist_ok=True)

    for pdf_file in input_dir.glob("*.pdf"):
        result = extract_outline(str(pdf_file))
        output_file = output_dir / f"{pdf_file.stem}.json"
        with open(output_file, "w") as f:
            json.dump(result, f, indent=2)

if __name__ == "__main__":
    main()
