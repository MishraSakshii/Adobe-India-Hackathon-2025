
# Persona-Driven Intelligent Document Analyzer

##  Challenge Overview

This project is a submission for **Round 1B of the Adobe India Hackathon 2025**, themed **"Connect What Matters — For the User Who Matters"**.

### Objective:
Build an offline, CPU-based intelligent document analyzer that:
- Accepts a **persona definition** and **job-to-be-done**
- Processes a **collection of PDFs** (3–10)
- Extracts and ranks the most relevant sections based on the persona’s objective
- Outputs the results in the required structured JSON format

---

##  Directory Structure

```
Round1B/
│
├── analyzer.py                # Main Python script
├── persona.json              # Persona definition and job-to-be-done
├── input/                    # Folder containing input PDFs (3–10 documents)
├── output.json               # Final output JSON with ranked sections
├── requirements.txt          # Python dependencies
├── approach_explanation.md  # 300–500 word write-up on the methodology
└── README.md                 # This file
```

---

##  How It Works

1. **Load Persona**:
   Loads `persona.json`, containing:
   ```json
   {
     "persona": "Product Manager",
     "job_to_be_done": "Identify key insights about market trends, product requirements, and competitor analysis"
   }
   ```

2. **Keyword Extraction**:
   The `job_to_be_done` string is split into keywords used to identify relevant PDF sections.

3. **Text Extraction**:
   The `PyMuPDF` library reads all `.pdf` files from the `input/` directory and extracts their content.

4. **Scoring & Ranking**:
   Text is split into paragraphs. Each paragraph is scored based on how many keywords it contains.
   The top 5 sections per document are retained based on score.

5. **Output Generation**:
   Creates a structured `output.json` file listing top sections per document.

---

##  Output Format

```json
[
  {
    "filename": "file1.pdf",
    "top_sections": [
      {
        "score": 15,
        "content": "The relevant section content..."
      }
    ]
  }
]
```

---

##  Setup Instructions

### Step 1: Clone Repository & Navigate

```
cd Round1B
```

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3: Add PDF Documents

Place your documents inside the `input/` directory.

### Step 4: Define Your Persona

Edit the `persona.json` file as needed.

### Step 5: Run the Analyzer

```bash
python analyzer.py
```

---

##  Constraints Met

-  Offline Execution (No Internet Access)
-  CPU-only
-  Executes within 60 seconds
-  Total Model/Script Size ≤ 1GB
-  Proper JSON Output

---

##  Requirements File (`requirements.txt`)

```
PyMuPDF
```

---

##  approach_explanation.md (Summary)

This script processes PDFs by extracting full text using `PyMuPDF`, then scores and ranks blocks of text using keywords derived from the persona’s job-to-be-done. It returns the top-scoring sections per file, allowing domain-specific document prioritization. No ML model was used to adhere to the offline, CPU-only, and ≤1GB constraints.

---

##  Authors

- Team INVICTA  
- Submitted for Adobe India Hackathon 2025
