import pandas as pd

def export_to_excel(invoice, filename="invoice_data.xlsx"):

    df = pd.DataFrame([invoice])

    df.to_excel(filename, index=False)

    print(f"Excel file saved as {filename}")