import os

os.system("pip install pyinstaller")

print("\n--------------- Run Python Compile -----------------------\n")

file = input(str("What file do you want generate a executable file (exemple: ocr_service.py)?\nFilename: "))

one_file = input(str("""Do you wanna create a single executable file?
If you wanna a single file, the process while run is more slowly. If you wanna share, you'll need to compact.
If you wanna a directory file, the processing is more fast. If you wanna share the file, it is not necessary to compact.
Sigle file is 'y' / directory file is 'n' 
[y/n]"""))

if one_file == "y":
    os.system(f"pyinstaller {file} --onefile")
elif one_file == "n":
    os.system(f"pyinstaller {file}")
else:
    print("You informed an incorrect answer. You need to say 'y' or 'n'.")

file = os.listdir("./")
for a in file:
    if ".spec" in a:
        os.system(f"rm {a}")
    if a == "build":
        os.system(f"rm -r {a}")
