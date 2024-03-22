import os
import ocrmypdf


def pdf_ocr(input_directory, output_directory, pdf_file):
    while True:
        file = os.listdir(input_directory)
        if pdf_file in file:
            break
    ocrmypdf.ocr(f'{input_directory}/{pdf_file}', f'{output_directory}/{pdf_file}', deskew=True, force_ocr=True, invalidate_digital_signatures=True)
