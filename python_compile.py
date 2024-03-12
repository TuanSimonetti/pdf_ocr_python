import os

os.system("pip install pyinstaller")

print("\n--------------- Run Python Compile -----------------------\n")

file = input(str("What file do you want generate a executable file (exemple: main.py)?\nFilename: "))

os.system(f"pyinstaller {file}")

file = os.listdir("./")
for a in file:
    if ".spec" in a:
        os.system(f"rm {a}")
    if a == "build":
        os.system(f"rm -r {a}")
