# Adobe India Hackathon 2025 – Round 1A Submission

##  Challenge Name: Connecting the Dots – PDF Outline Extractor

## Problem Statement
Given a PDF file, extract its hierarchical outline (Table of Contents) in a structured format (JSON). The goal is to process uploaded PDFs and extract any embedded bookmarks or outline entries to support document navigation.

##  Approach
We built a Dockerized Python application that:
- Reads an input PDF file (e.g., `sample.pdf`)
- Uses PyMuPDF (`fitz`) to extract the outline/bookmark structure
- Cleans and structures the data into a JSON format
- Writes the final output to a file named `outline.json`

If no outline is found, the program gracefully exits with a message indicating the same.

##  How to Run

### 1. Build the Docker Image
```bash
docker build -t adobe-pdf-outliner .
```

### 2. Run the Container
```bash
docker run --rm -v "${PWD}:/app" adobe-pdf-outliner > outline.json
```

>  Ensure your `sample.pdf` is placed inside the mounted folder (`/app` in the container). The extracted outline will be saved to `outline.json`.

##  Sample Output (`outline.json`)
```json
[
  {
    "title": "Chapter 1",
    "page": 1,
    "children": [
      {
        "title": "Section 1.1",
        "page": 2,
        "children": []
      }
    ]
  },
  {
    "title": "Chapter 2",
    "page": 5,
    "children": []
  }
]
```

> In case of no bookmarks in the PDF, the tool outputs: `No outline found in the PDF.`

##  Dependencies
All dependencies are listed in `requirements.txt` and installed via Docker during build.

```txt
PyMuPDF
```

##  Tech Stack
- Python 3
- PyMuPDF (fitz)
- Docker

##  Notes
- Tested with various PDFs — if the document lacks bookmarks, the outline will be empty.
- Docker ensures portability across environments.
- You can also run the script locally using `python extract_outline.py` for testing purposes.

##  Contributor
- **Team:** INVICTA
- **Hackathon:** Adobe India Hackathon 2025
- **Challenge:** Round 1A – Connecting the Dots
