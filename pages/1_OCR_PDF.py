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
    upload_text = f"**{uploaded_file.name} is sucessfully Uploaded.**"
    upload_process = st.progress(0, text=upload_text)
    save_text = f"**{uploaded_file.name} is sucessfully Saved.**"
    save_process = st.progress(0, text=save_text)
    ocr_text = f"**{uploaded_file.name} is sucessfully OCR.**"
    ocr_process = st.progress(0, text=ocr_text)
    delete_text = f"**{uploaded_file.name} will be deleted in 30 seconds.**"
    delete_process = st.progress(0, text=delete_text)

    for percent_complete in range(100):
        time.sleep(0.001)
        upload_process.progress(percent_complete + 1, text=upload_text)

    # Save uploaded file to './input_pdf_file' folder.
    save_folder = './input_pdf_file'
    output_folder = './output_pdf_file'
    save_path = Path(save_folder, uploaded_file.name)

    with st.spinner('Wait for uploading pdf...'):
        with open(save_path, mode='wb') as w:
            w.write(uploaded_file.getvalue())
        while True:
            input_folder = os.listdir(save_folder)
            if uploaded_file.name in input_folder:
                break
        for percent_complete in range(100):
            time.sleep(0.001)
            save_process.progress(percent_complete + 1, text=save_text)

    with st.spinner('Wait for ocr process...'):
        pdf_ocr(input_directory=save_folder, output_directory=output_folder, pdf_file=uploaded_file.name)
        while True:
            output_folder_list = os.listdir('./output_pdf_file')
            if uploaded_file.name in output_folder_list:
                break
        for percent_complete in range(100):
            time.sleep(0.001)
            ocr_process.progress(percent_complete + 1, text=ocr_text)

    with open(f"./output_pdf_file/{uploaded_file.name}", "rb") as pdf_file:
        PDFbyte = pdf_file.read()


    st.download_button(label="Download is ready...",
                       data=PDFbyte,
                       file_name=uploaded_file.name,
                       mime='application/octet-stream')

    for percent_complete in range(100):
        time.sleep(0.5)
        delete_process.progress(percent_complete + 1, text=delete_text)

    os.system(f"rm './input_pdf_file/{uploaded_file.name}'")
    os.system(f"rm './output_pdf_file/{uploaded_file.name}'")


