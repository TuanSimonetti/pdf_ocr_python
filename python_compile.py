import os

os.system("pip install pyinstaller")

print("\n--------------- Run Python Compile -----------------------\n")

file = input(str("What file do you want generate a executable file (exemple: main.py)?\nFilename: "))

os.system(f"pyinstaller {file}")
