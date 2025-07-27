# Challenge 1A: PDF Outline Extraction – Adobe India Hackathon 2025

## Overview

This repository contains the solution for **Round 1A – Connecting the Dots Challenge** of the **Adobe India Hackathon 2025**.

Your mission is to process PDF documents and extract a structured outline consisting of:
- Title
- Headings (H1, H2, H3)
- Corresponding page numbers

The solution must be containerized, run on AMD64 CPU architecture, and must **not require internet access** during execution. It should handle up to 50-page PDFs and complete processing in under 10 seconds per document.

---

## Official Requirements

| Requirement                     | Description                                       |
|--------------------------------|---------------------------------------------------|
| Max PDF Length                 | 50 pages                                          |
| Extracted Info                 | Title, H1, H2, H3 headings (with page numbers)    |
| Output Format                  | Valid structured JSON                             |
| Processing Time                | ≤ 10 seconds                                      |
| Network                        | No internet access allowed                     |
| Runtime                        | CPU only (AMD64), 8 CPUs, 16 GB RAM              |
| Model Size (if any used)       | ≤ 200MB                                           |
| Platform                       | Must work on AMD64                                |

---

## Input Format

Your solution should automatically process all `.pdf` files placed inside the `/app/input` directory.

---

## Output Format

Each input PDF should generate a corresponding `.json` file in `/app/output` with the following structure:

```json
{
  "title": "Understanding AI",
  "outline": [
    { "level": "H1", "text": "Introduction", "page": 1 },
    { "level": "H2", "text": "What is AI?", "page": 2 },
    { "level": "H3", "text": "History of AI", "page": 3 }
  ]
}
```

---

## Project Structure

```
Challenge_1a/
├── input/                        # Input PDFs (mounted at runtime)
├── output/                       # Output JSONs (generated)
├── src/
│   └── main.py                   # PDF → JSON processing script
├── sample_dataset/
│   ├── pdfs/                     # Sample PDFs
│   ├── outputs/                  # Sample outputs (JSON)
│   └── schema/
│       └── output_schema.json    # JSON schema definition
├── Dockerfile                    # Docker image definition
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

---

## Build Command

```bash
docker build --platform linux/amd64 -t pdf-outline-solution:<your_identifier> .
```

## Run Command

```bash
docker run --rm \
  -v $(pwd)/input:/app/input:ro \
  -v $(pwd)/output:/app/output \
  --network none \
  pdf-outline-solution:<your_identifier>
```

---

## Implementation Overview

This solution is built with the following principles:
- **Heuristic-based heading detection** using font size and position.
- **PyMuPDF** (`fitz`) for lightweight and accurate PDF parsing.
- Fully containerized via Docker, supporting AMD64 architecture.
- Offline-only design with zero external API calls.

---

## How It Works

1. **PDF Scanning**: All `.pdf` files in `/app/input` are processed.
2. **Text Extraction**: For each page, text blocks are analyzed.
3. **Heading Detection**:
   - Based on font size, weight, position.
   - Assigned as H1, H2, H3 accordingly.
4. **Title Inference**: The most prominent text (largest font on first page) is taken as the title.
5. **Output Generation**: A structured `.json` file is written per input PDF.

---

## Validation Checklist

- [x] Processes all `.pdf` files from `/app/input`
- [x] Outputs JSON files with correct filename mapping
- [x] Each JSON file matches schema in `output_schema.json`
- [x] Output includes title + heading hierarchy with page numbers
- [x] Finishes under 10s for 50-page PDFs
- [x] Entire solution works offline on CPU

---

## Sample Execution (Local)

```bash
# Step 1: Build the Docker image
docker build --platform linux/amd64 -t pdf-outline-solution .

# Step 2: Run the processor on sample data
docker run --rm \
  -v $(pwd)/sample_dataset/pdfs:/app/input:ro \
  -v $(pwd)/sample_dataset/outputs:/app/output \
  --network none \
  pdf-outline-solution
```

---

## Notes

- This solution works on any Linux/macOS system with Docker installed.
- It avoids hardcoding document rules and is generalizable to unseen PDFs.
- Multilingual support is not included in this baseline but can be added for bonus scoring.

---

## Acknowledgements

- Libraries used: `PyMuPDF`, `os`, `json`, `re`
- Dataset: Sample PDFs and outputs are used for testing only.

---
