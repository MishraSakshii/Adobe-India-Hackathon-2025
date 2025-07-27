# Round 1B: Persona-Driven Document Analyzer - Approach Explanation

## Overview

This solution implements an intelligent offline document analyzer designed to extract and rank the most relevant sections from a set of PDF files based on a user-defined persona and job-to-be-done. It uses lightweight, CPU-friendly methods for keyword scoring and text extraction to comply with the challenge constraints: model size < 1GB, CPU-only, and ≤60 seconds for processing 3–5 documents.

---

## Methodology

### 1. Input Handling

* The system expects the following inputs:

  * A folder named `input` containing PDF documents.
  * A `persona.json` file specifying:

    * `persona`: The role (e.g., Product Manager, Researcher).
    * `job_to_be_done`: A textual description of the task the persona needs to accomplish.

### 2. Text Extraction

* Uses `PyMuPDF` (fitz) to extract raw text from each page in each PDF file.
* All text from a PDF is collected and split into candidate sections by paragraph.

### 3. Keyword Scoring

* The `job_to_be_done` string is split into individual keywords.
* Each paragraph is scored based on keyword frequency.
* Top 5 highest-scoring sections per document are retained.

### 4. Output Format

* Output is saved in `output.json` in the following structure:

  ```json
  [
    {
      "filename": "file1.pdf",
      "top_sections": [
        { "score": 5, "content": "..." },
        ...
      ]
    },
    ...
  ]
  ```
* This structure aligns with the expected schema in the challenge instructions.

---

## Constraints Compliance

* **CPU-Only**: No GPU libraries are used.
* **Model Size**: No pretrained or deep learning models are used.
* **Time**: Processing is deterministic and lightweight (under 60 seconds for 3–5 files).
* **Offline**: All functionality works offline; no internet access is needed.

---

## Improvements & Future Scope

* Add deeper semantic matching using a small language model (≤1GB) for ranking.
* Include sub-section breakdown using headings/font sizes from PDFs.
* Normalize scores across documents for better cross-file ranking.

---

## Conclusion

This solution provides a lightweight, efficient, and accurate method for persona-based document analysis, and can be easily extended or adapted to a variety of use cases and personas.
