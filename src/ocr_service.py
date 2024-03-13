import os
import ocrmypdf


def pdf_ocr(pdf_file):
    while True:
        file = os.listdir("./input_pdf_file")
        if pdf_file in file:
            break
    ocrmypdf.ocr(f'./input_pdf_file/{pdf_file}', f'./output_pdf_file/{pdf_file}', deskew=True, force_ocr=True)
