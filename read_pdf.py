import pypdf
with open('S06 - Fundamentos de CI-CD - Conceptos y Herramientas.pdf', 'rb') as f:
    reader = pypdf.PdfReader(f)
    text = '\n'.join(page.extract_text() for page in reader.pages)
    with open('pdf_text.txt', 'w', encoding='utf-8') as out:
        out.write(text)
