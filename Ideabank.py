
import sys

if sys.argv[1:]:
    if sys.argv[1] == "--list":
        with open("ideabank.md", "r") as f:
            print("Your ideabank:")
            i = 1
            for line in f:
                print(str(i) + ". ", line, end = "")
                i += 1
    else:
        print("Unknown arguments!")
else:
    idea = input("What is your new idea: ")
    with open("ideabank.md", "a+") as f:
        f.write(idea + "\n")
        print("\nYour ideabank:")
        f.seek(0)
        i = 1
        for line in f:
            print(str(i) + ". ", line, end = "")
            i += 1
