import os
from tkinter import Tk, filedialog, Button, Label, StringVar
from tkinter.messagebox import showinfo
from converter import convertPdfToExcel

def chooseFile():
    pdfPath = filedialog.askopenfilename(
        title = 'Select a PDF file',
        filetypes = (('PDF File', '*.pdf'),)
    )
    if pdfPath:
        labelFile['text'] = f'Selected File: {os.path.basename(pdfPath)}'
        selectedPdfPath.set(pdfPath)

def converter():
    pdfPath = selectedPdfPath.get()
    if not pdfPath:
        showinfo('Error','Please, select a PDF file first.')
        return
    
    excelFile = filedialog.asksaveasfilename(
        defaultextension = '.xlsx',
        filetypes = (('Excel File', '*.xlsx'),),
        title = 'Save as'
    )

    if excelFile:
        convertPdfToExcel(pdfPath, excelFile)
        showinfo('Success', f'Conversion Complete! File saved as {excelFile}')
    
