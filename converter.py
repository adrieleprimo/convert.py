import camelot
import pandas as pd
import tabula   

def extractTabularTables(pdfPath):
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
    
