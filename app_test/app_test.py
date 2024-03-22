from streamlit.testing.v1 import AppTest


def test_home_page():
    at = AppTest.from_file("../Home.py").run()
    assert not at.exception


def test_ocr_pdf_page_1():
    at = AppTest.from_file("../pages/1_OCR_PDF.py").run()
    assert not at.exception


#def test_pdf_ocr_function():
    #    pdf_file = "hello_world.pdf"
    #os.system("mkdir ../input_pdf_file")
    #os.system("mkdir ../output_pdf_file")
    #os.system(f"cp ../app_test/{pdf_file} ../input_pdf_file/")
    #input_directory = "../input_pdf_file"
    #output_directory = "../output_pdf_file"
    #pdf_ocr(input_directory=input_directory, output_directory=output_directory, pdf_file=pdf_file)
    #output_test = os.listdir(output_directory)
    #os.system("rm -r ../input_pdf_file")
    #os.system("rm -r ../output_pdf_file")
    #assert output_test[0].endswith('.pdf') == True

