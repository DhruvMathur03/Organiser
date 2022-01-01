from pathlib import Path


req_path = Path("/Users/dhruvmathur/Documents")
main_path = Path("/Users/dhruvmathur")
folders = ["Racket", "Python", "stuff", "PDF"]

for file in main_path.iterdir():
    if file.is_file() and file.stem != ".DS_Store":
        a = 0
        ext = file.suffix
        stem = file.stem
        new_file = f'{file.stem}{ext}'

        if ext == ".rkt":
            a = 0
        elif ext == ".py":
            a = 1
        elif ext == ".pdf":
            a = 3
        else:
            a = 2

        new_path = req_path.joinpath(folders[a])
        new_file_path = new_path.joinpath(new_file)
        file.replace(new_file_path)

        




