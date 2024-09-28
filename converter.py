import camelot
import pandas as pd
import tabula   

def extractTabulaTables(pdfPath):
    try:
        tables = tabula.read_pdf(pdfPath, pages='all', multiple_tables=True)
        return tables
    except Exception as e:
        print(f'Error when extracting with Tabula: {e}')
        return None
    
def extractCamelotTables(pdfPath):
    try:
        tables = camelot.read_pdf(pdfPath, pages='all')
        return [tables.df for table in tables]
    except Exception as e:
        print(f'Error when extracting with Camelot: {e}')
        return None
    
def savePdfToExcel(tables, fileNameExcel):
    with pd.ExcelWriter(fileNameExcel, engine='openpyxl') as writer:
        for idx, table in enumerate(tables):
            table.to_excel(writer, sheet_name=f'Table_{idx+1}', index=False)
        print(f'Conversion complete! File saved as {fileNameExcel}')

def convertPdfToExcel(pdfPath, fileNameExcel):
    tables = extractTabulaTables(pdfPath)
    if not tables:
        tables = extractCamelotTables(pdfPath)
    
    if tables:
        savePdfToExcel(tables, fileNameExcel)
    else:
        print('No table was found in the PDF')

