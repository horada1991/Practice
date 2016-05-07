
import sys

def PrintIdeaBank():
    print("Your ideabank:")
    f.seek(0)
    i = 1
    for line in f:
        print(str(i) + ". ", line, end = "")
        i += 1


if sys.argv[1:]:
    if sys.argv[1] == "--delete":
        with open("ideabank.md", "r+") as f:
            lines = f.readlines()
            f.seek(0)
            i = 1
            for line in lines:
                try:
                    if i != int(sys.argv[2]):
                        f.write(line)
                    i += 1
                except ValueError:
                    print("Not a valid value for the --delete command!")
                    exit()
            f.truncate()
            PrintIdeaBank()
    elif sys.argv[1] == "--list":
        with open("ideabank.md", "r") as f:
            PrintIdeaBank()
    else:
        print("Unknown arguments!")
else:
    idea = input("What is your new idea: ")
    with open("ideabank.md", "a+") as f:
        f.write(idea + "\n")
        print("")
        PrintIdeaBank()
