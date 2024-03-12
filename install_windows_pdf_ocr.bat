Dir ./Desktop
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

echo python main.py >> execution.bat

@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%username%\chocolatey\bin"

echo choco install python --version=3.9.7 >> install_components.bat
echo choco upgrade python --version=3.9.7 >> install_components.bat
echo python3 -m venv .\myenv >> install_components.bat
echo python -m pip install --upgrade pip >> install_components.bat
echo choco install --pre tesseract >> install_components.bat
echo choco install tesseract-lang >> install_components.bat
echo choco install ghostscript >> install_components.bat
echo choco install pngquant >> install_components.bat
echo pip install ocrmypdf >> install_components.bat
echo python --version >> install_components.bat