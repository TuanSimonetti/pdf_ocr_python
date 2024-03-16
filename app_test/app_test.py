import os
from streamlit.testing.v1 import AppTest
from src.ocr_service import pdf_ocr

def test_home_page():
    at = AppTest.from_file("../Home.py").run()
    assert not at.exception


def test_ocr_pdf_page_1():
    at = AppTest.from_file("../pages/1_OCR_PDF.py").run()
    assert not at.exception


def test_pdf_ocr_function():
    os.system("mkdir ../input_pdf_file")
    os.system("mkdir ../output_pdf_file")
    os.system("cp ../app_test/test.pdf ../input_pdf_file/")
    pdf_file = "test.pdf"
    input_directory = "../input_pdf_file"
    output_directory = "../output_pdf_file"
    pdf_ocr(input_directory=input_directory, output_directory=output_directory, pdf_file=pdf_file)
    output_test = os.listdir(output_directory)
    os.system("rm -r ../input_pdf_file")
    os.system("rm -r ../output_pdf_file")
    assert output_test[0].endswith('.pdf') == True

