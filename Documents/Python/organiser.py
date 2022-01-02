from pathlib import Path

inp = input("Enter Path to be organised :")
req_path = Path("/Users/dhruvmathur/Documents")
main_path = Path(inp)
folders = ["Racket", "Python", "stuff", "PDF", "Roms", "apps", "CS-Assignments"]

def replacer(index, filename):
    new_path = req_path.joinpath(folders[index])
    new_file_path = new_path.joinpath(filename)
    file.replace(new_file_path)

for file in main_path.iterdir():

    a = 0
    ext = file.suffix
    stem = file.stem
    new_file = f'{file.stem}{ext}'

    if file.is_file() and file.stem != ".DS_Store":
        
        if "Cs" in stem:
            a = 6
        elif ext == ".rkt":
            a = 0
        elif ext == ".py":
            a = 1
        elif ext == ".pdf":
            a = 3
        elif ext == ".gba" or ext == ".nds":
            a = 4
        else:
            a = 2

    elif ext == ".app":
        a = 5

    replacer(a, new_file)

        





