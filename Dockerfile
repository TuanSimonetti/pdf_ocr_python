FROM python:3.10-slim

RUN pip install --upgrade pip
RUN mkdir -p /app/
RUN mkdir /app/input_pdf_file/
RUN mkdir /app/output_pdf_file/
WORKDIR /app

COPY . /app/

RUN apt-get update \
    && apt-get -y install tesseract-ocr \
    && apt-get -y install ghostscript

RUN python3 -m pip install -r /app/requirements.txt

RUN pip3 install -r requirements.txt

EXPOSE 8502

HEALTHCHECK CMD curl --fail http://localhost:8502/_stcore/health

RUN chmod +x ./docker-entrypoint.sh

ENTRYPOINT ["./docker-entrypoint.sh"]