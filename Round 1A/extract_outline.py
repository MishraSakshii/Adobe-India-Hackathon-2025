import fitz  # PyMuPDF
import os
import json

def extract_headings(pdf_path):
    doc = fitz.open(pdf_path)
    title = os.path.basename(pdf_path).replace(".pdf", "")
    outline = []

    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict")["blocks"]

        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    size = span["size"]

                    # Simple heuristic (you can refine later)
                    if size > 20:
                        level = "H1"
                    elif 15 < size <= 20:
                        level = "H2"
                    elif 12 < size <= 15:
                        level = "H3"
                    else:
                        continue

                    outline.append({
                        "level": level,
                        "text": text,
                        "page": page_num + 1
                    })

    return {
        "title": title,
        "outline": outline
    }

def main(input_dir, output_dir):
    for filename in os.listdir(input_dir):
        if filename.endswith(".pdf"):
            input_path = os.path.join(input_dir, filename)
            result = extract_headings(input_path)

            output_path = os.path.join(output_dir, filename.replace(".pdf", ".json"))
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2)

if __name__ == "__main__":
    input_dir = "/app/input"
    output_dir = "/app/output"
    os.makedirs(output_dir, exist_ok=True)
    main(input_dir, output_dir)
