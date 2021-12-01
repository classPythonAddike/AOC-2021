import os

# Folders are named like c1, c2, c3 ...

folders = [f.name for f in os.scandir(".") if f.is_dir() and f.name[0] == "c"]
challenge_numbers = sorted([int(f[1:]) for f in folders])

new_c = challenge_numbers[-1] + 1 if len(challenge_numbers) > 0 else 1

choice = input(f"Creating folder for c{new_c}. Proceed? [Y/n]: ").lower()

if choice == "n":
    print("Exiting . . . .")
    exit()

os.mkdir(os.path.join(os.curdir, f"c{new_c}"))


language_list = {
    "Python": "py",
    "Golang": "go",
    "Ruby": "rb"
}

print("Select a language to continue with:")

for num, lang in enumerate(language_list):
    print(f"{num + 1}. {lang}")

print(f"{len(language_list) + 1}. Skip")

language = input(f"Choice (Default is Skip): ")

if language not in language_list:
    print("Skipping . . . .")
    exit()

lang_filetype = language_list[language]

print(f"Creating {language} file in c{new_c}/")

with open(os.path.join(f"c{new_c}", f"p1.{lang_filetype}"), "w") as f:
    pass

with open(os.path.join(f"c{new_c}", f"p2.{lang_filetype}"), "w") as f:
    pass

with open(os.path.join(f"c{new_c}", "input.txt"), "w") as f: pass

print("Done! Good Luck!")
