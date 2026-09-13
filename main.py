from extractor import extract_local_pdf
from parser import parse_invoice
from exporter import export_to_excel
import os

pdf_folder = "sample_documents"

files = os.listdir(pdf_folder)

print(files)

pdf_path = "sample_documents/invoice_001.pdf"

text = extract_local_pdf(pdf_path)

print("RAW TEXT")
print(text)

invoice = parse_invoice(text)

print("\n-----Extracted invoice-----")
print(f"Supplier: {invoice['supplier']}")
print(f"Invoice number: {invoice['invoice_number']}")
print(f"Invoice date: {invoice['invoice_date']}")
print(f"Due date: {invoice['due_date']}")
print(f"Subtotal: {invoice['subtotal']}")
print(f"Tax: {invoice['tax']}") 
print(f"Total: {invoice['total']}")  

export_to_excel(invoice)