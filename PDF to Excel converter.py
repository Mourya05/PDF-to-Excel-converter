import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_path, excel_path):
    # Open the PDF file
    with pdfplumber.open(pdf_path) as pdf:
        first_page = pdf.pages[0]
        table = first_page.extract_table()

        if table:
            df = pd.DataFrame(table[1:], columns=table[0])
            

            df.to_excel(excel_path, index=False)
            print(f"Excel file saved at {excel_path}")
        else:
            print("No table found on the first page.")


pdf_path = 'input.pdf'
excel_path = 'output.xlsx'
pdf_to_excel(pdf_path, excel_path)
