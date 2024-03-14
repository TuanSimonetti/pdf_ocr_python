import time

import streamlit as st
from pathlib import Path
import os
from src.ocr_service import pdf_ocr

st.set_page_config(
    page_title="OCR PDF"
)

st.title("OCR PDF")

uploaded_file = st.file_uploader("Choose a PDF file", type="pdf", accept_multiple_files=False)

if st.button('Submit'):
    st.markdown("**The file is sucessfully Uploaded.**")

    # Save uploaded file to 'F:/tmp' folder.
    save_folder = './input_pdf_file'
    save_path = Path(save_folder, uploaded_file.name)
    with st.spinner('Wait for uploading pdf...'):
        with open(save_path, mode='wb') as w:
            w.write(uploaded_file.getvalue())
        while True:
            input_folder = os.listdir(save_folder)
            if uploaded_file.name in input_folder:
                break
        st.success(f'File {uploaded_file.name} is successfully saved!')
    with st.spinner('Wait for ocr process...'):
        pdf_ocr(pdf_file=uploaded_file.name)
        while True:
            output_folder = os.listdir('./output_pdf_file/')
            if uploaded_file.name in output_folder:
                break
        st.success(f'File {uploaded_file.name} is successfully ocr processed!')

    with open(f"./output_pdf_file/{uploaded_file.name}", "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.write("arquivo sera arquivado em 30 segundos")

    st.download_button(label="Download is ready...",
                       data=PDFbyte,
                       file_name=uploaded_file.name,
                       mime='application/octet-stream')

    time.sleep(30)
    os.system(f"rm './input_pdf_file/{uploaded_file.name}'")
    os.system(f"rm './output_pdf_file/{uploaded_file.name}'")


