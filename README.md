# Adobe India Hackathon 2025

## Welcome to the "Connecting the Dots" Challenge

### Rethink Reading. Rediscover Knowledge.

What if every time you opened a PDF, it didn't just sit there—it spoke to you, connected ideas, and narrated meaning across your entire library?

That's the future we're building — and we want you to help shape it.

In the *Connecting the Dots* challenge, our mission is to reimagine the humble PDF as an intelligent, interactive experience — one that understands structure, surfaces insights, and responds like a trusted research companion.

---

## The Journey Ahead

### Round 1: 
Kick things off by building the brains — extract structured outlines from raw PDFs with blazing speed and pinpoint accuracy. Then, power it up with on-device intelligence that understands sections and links related ideas together.

### Round 2:
It's showtime! Build a beautiful, intuitive reading webapp using Adobe's PDF Embed API. You will be using your Round 1 work to design a futuristic web experience.

---

## Why This Matters

In a world flooded with documents, what wins is not more content — it's **context**. We're not just building tools — we're building the future of how we read, learn, and connect.

No matter your background — ML hacker, UI builder, or insight whisperer — this is your stage.

**Are you in?**  
It's time to read between the lines. Connect the dots. And build a PDF experience that feels like magic. Let's go.

---

## Challenge Solutions

### [Challenge 1A – PDF Outline Extraction](./Challenge_1a/README.md)
Basic PDF processing with Docker containerization and structured outline extraction (Title, H1, H2, H3).  
A lightweight CPU-only solution that enables fast, offline document structure understanding.

---

### [Challenge 1B – Persona-Driven Document Intelligence](./Challenge_1b/README.md)
Advanced content filtering from document collections using Persona and Job-to-be-Done input.  
Returns ranked, relevant document sections using personalized document analysis.

---

## Repository Structure

```
.
├── Challenge_1a/
│   ├── input/                      # Input PDFs (mounted at runtime)
│   ├── output/                     # Output JSONs (generated)
│   ├── src/                        # Outline extraction logic
│   ├── Dockerfile
│   └── README.md

├── Challenge_1b/
│   ├── Collection_1/               # Financial Reports
│   ├── Collection_2/               # Product Manuals
│   ├── Collection_3/               # Educational Content
│   ├── src/                        # Content extraction logic
│   ├── Dockerfile
│   ├── approach_explanation.md
│   └── README.md

├── .gitignore
└── README.md                       # ← You are here
```

---

## Note

Each challenge directory contains detailed documentation and instructions.  
Please refer to their individual `README.md` files for build, run, and implementation details.

---

