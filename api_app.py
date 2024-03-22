from fastapi import FastAPI, UploadFile
from starlette.responses import RedirectResponse
from src.service.ocr_service import api_pdf_ocr

app = FastAPI()


@app.get("/api/health/")
def health():
    return {"Status": "ok"}


@app.get("/api/swagger/")
def swagger():
    return RedirectResponse(url="/docs/")


@app.post("/api/pdf_ocr/")
def pdf_ocr(file: UploadFile):
    response = api_pdf_ocr(output_directory='./output_pdf_file', pdf_file=file.filename)
    return {"pdf_file": response.filename}
