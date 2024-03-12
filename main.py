import os
import ocrmypdf


def pdf_ocr():
    file = os.listdir(".input_pdf_file")
    for a in file:
        ocrmypdf.ocr(f'./input_pdf_file/{a}', f'./output_pdf_file/{a}', deskew=True, force_ocr=True)


if __name__ == '__main__':
    pdf_ocr()