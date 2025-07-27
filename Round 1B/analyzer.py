import os
import json
import fitz  # PyMuPDF
from datetime import datetime

def load_persona(file="persona.json"):
    with open(file, "r") as f:
        return json.load(f)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    return "\n".join([page.get_text() for page in doc])

def score_sections(text, query_keywords):
    sections = text.split('\n\n')
    scored = []
    for section in sections:
        score = sum(section.lower().count(k.lower()) for k in query_keywords)
        if score > 0:
            scored.append((score, section.strip()))
    return sorted(scored, reverse=True)[:5]

def estimate_page_number(content, pdf_path):
    doc = fitz.open(pdf_path)
    for i, page in enumerate(doc):
        if content.strip() in page.get_text():
            return i + 1
    return -1  # If not found

def main():
    persona_data = load_persona()
    keywords = persona_data["job_to_be_done"].lower().split()

    extracted_sections = []
    subsection_analysis = []
    input_documents = []
    rank = 1

    for pdf_file in os.listdir("input"):
        if pdf_file.endswith(".pdf"):
            input_documents.append(pdf_file)
            full_path = os.path.join("input", pdf_file)
            text = extract_text_from_pdf(full_path)
            ranked = score_sections(text, keywords)

            for score, content in ranked:
                page_num = estimate_page_number(content, full_path)
                extracted_sections.append({
                    "document": pdf_file,
                    "page_number": page_num,
                    "section_title": content.split('\n')[0][:100],
                    "importance_rank": rank
                })
                subsection_analysis.append({
                    "document": pdf_file,
                    "refined_text": content[:1000],
                    "page_number": page_num
                })
                rank += 1

    final_output = {
        "metadata": {
            "input_documents": input_documents,
            "persona": persona_data["persona"],
            "job_to_be_done": persona_data["job_to_be_done"],
            "processing_timestamp": datetime.now().isoformat()
        },
        "extracted_sections": extracted_sections,
        "subsection_analysis": subsection_analysis
    }

    with open("output.json", "w") as f:
        json.dump(final_output, f, indent=2)

if __name__ == "__main__":
    main()

