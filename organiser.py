from pathlib import Path

req_path = Path("/Users/dhruvmathur/Documents")
user_path = Path("/Users/dhruvmathur/")
folders = ["Racket", "Python", "stuff", "Roms", "apps", "CS-Assignments", "MATH", "Screenshots"]

def paths(inp):

    if inp == "Downloads":
        req_user_path = user_path.joinpath("Downloads")
        return req_user_path
    elif inp == "Documents":
        req_user_path = user_path.joinpath("Documents")
        return req_user_path
    elif inp == "Desktop":
        req_user_path = user_path.joinpath("Desktop")
        return req_user_path
    

def user_input():
    options = ["Downloads", "Documents", "Desktop"]
    for i in range(len(options)):
        print(str(i+1) + ":" + options[i])
    inp = int(input("Enter Number : "))
    if inp in range(len(options) + 1):
        inp = options[inp - 1]
        return inp
    else:
        print("Invalid")
        SystemExit
    

def replacer(index, filename):
    new_path = req_path.joinpath(folders[index])

    if index == 6:
        if "136" in filename:
            new_path = new_path.joinpath("136")
        else:
            new_path = new_path.joinpath("138")

    new_file_path = new_path.joinpath(filename)
    file.replace(new_file_path)

a = user_input()
main_path = paths(a)

for file in main_path.iterdir():

    a = 0
    ext = file.suffix
    stem = file.stem
    new_file = f'{file.stem}{ext}'

    if file.is_file() and file.stem != ".DS_Store":
        
        if "Cs" in stem:
            a = 5
        elif "Screenshot" in stem:
            a = 7
        elif ext == ".rkt":
            a = 0
        elif ext == ".py":
            a = 1
        elif ext == ".gba" or ext == ".nds":
            a = 3
        elif "Lecture" in stem:
            a = 6
        else:
            a = 2

    elif ext == ".app":
        a = 5
    replacer(a, new_file)

        





