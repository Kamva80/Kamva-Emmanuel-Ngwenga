import re

def parse_invoice(text):
    data = {
        "supplier": None,
        "invoice_number": None,
        "invoice_date": None,
        "due_date": None,
        "subtotal": None,
        "total": None,
        "tax": None
    }

    supplier_match = re.search(r"From:\s*\n\s*(.+)",  text)
    if supplier_match:
        data["supplier"] = supplier_match.group(1).strip()

    invoice_number_match = re.search(r"Invoice Number\s+([A-Z0-9-]+)", text)
    if invoice_number_match:
        data["invoice_number"] = invoice_number_match.group(1)

    invoice_date_match = re.search(r"Invoice Date\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})", text)   
    if invoice_date_match:
        data["invoice_date"] = invoice_date_match.group(1)

    due_date_match = re.search(r"Due Date\s+([A-Za-z]+\s+\d{1,2},\s+\d{4})", text)
    if due_date_match:
        data["due_date"] = due_date_match.group(1)

    subtotal_match = re.search(r"Sub Total\s+\$?([\d.,]+)", text)
    if subtotal_match:
        data["subtotal"] = subtotal_match.group(1)

    total_match = re.search(r"^Total\s+\$?([\d.,]+)", text, re.MULTILINE)
    if total_match:
        data["total"] = total_match.group(1)

    tax_match = re.search(r"Tax\s+\$?([\d.,]+)", text)
    if tax_match:
        data["tax"] = tax_match.group(1)

    return data

     