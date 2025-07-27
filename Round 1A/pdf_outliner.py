import fitz  # PyMuPDF
import json
import os

def extract_outline(pdf_path):
    doc = fitz.open(pdf_path)
    outline = doc.get_toc()

    if not outline:
        print("No outline found in the PDF.")
        return

    def build_structure(toc):
        tree = []
        stack = []

        for level, title, page in toc:
            node = {
                "title": title,
                "page": page,
                "children": []
            }

            while len(stack) >= level:
                stack.pop()

            if stack:
                stack[-1]["children"].append(node)
            else:
                tree.append(node)

            stack.append(node)

        return tree

    structured = build_structure(outline)

    # Save to output JSON file
    with open("structured_outline.json", "w", encoding="utf-8") as f:
        json.dump(structured, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    extract_outline("input/sample.pdf")
