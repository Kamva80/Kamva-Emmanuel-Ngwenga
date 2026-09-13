import pdfplumber

def extract_local_pdf(pdf_path):
    # Open the PDF file locally on your machine
    with pdfplumber.open(pdf_path) as pdf:
        # Extract all text from the very first page
        first_page = pdf.pages[0]
        text_content = first_page.extract_text()

    return text_content

