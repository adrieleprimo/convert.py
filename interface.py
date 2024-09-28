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

