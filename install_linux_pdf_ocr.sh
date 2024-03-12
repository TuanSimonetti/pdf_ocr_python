cd ./Desktop
mkdir pdf_ocr_python
cd pdf_ocr_python
mkdir input_pdf_file
mkdir output_pdf_file

cd ./Desktop/pdf_ocr_python/main.py

echo import os >> main.py
echo import ocrmypdf >> main.py
echo def pdf_ocr(): >> main.py
echo    file = os.listdir(".input_pdf_file") >> main.py
echo    for a in file: >> main.py
echo        ocrmypdf.ocr(f'./input_pdf_file/{a}', f'./output_pdf_file/{a}', deskew=True, force_ocr=True) >> main.py
echo if __name__ == '__main__': >> main.py
echo    pdf_ocr() >> main.py

echo python3 main.py >> execution.bat


sudo apt-get update
sudo apt-get install python3.10.12
pip install --upgrade pip
Python3 -m venv .\myenv

sudo apt install tesseract-ocr
sudo apt install libtesseract-dev
sudo apt install tesseract-lang

sudo apt-get install ghostscript

git clone --recursive https://github.com/kornelski/pngquant.git
cd pngquant
cargo build --release

pip install ocrmypdf
