import os
from pathlib import Path
from fastapi import FastAPI, UploadFile
from fastapi.responses import FileResponse
from starlette.responses import RedirectResponse
from src.service.ocr_service import pdf_ocr

app = FastAPI()


@app.get("/api/health/")
def health():
    return {"Status": "ok"}


@app.get("/api/swagger/")
def swagger():
    return RedirectResponse(url="/docs/")


@app.post("/api/pdf_ocr/")
def pdf_ocr(file: UploadFile):
    save_folder = './input_pdf_file'
    output_folder = './output_pdf_file'
    save_path = Path(save_folder, file.filename)
    with open(save_path, mode='wb') as w:
        w.write(UploadFile.getvalue())
    pdf_ocr(input_directory=save_folder,
            output_directory=output_folder,
            pdf_file=file.filename)
    if os.path.exists(f'{output_folder}/{file.filename}'):
        return FileResponse(f'{output_folder}/{file.filename}', media_type="application/pdf")
    return {"error": "File not found!"}
