
idea = input("What is your new idea: ")
with open("ideabank.md", "a+") as f:
    f.write(idea + "\n")
    print("\nYour ideabank:")
    f.seek(0)
    i = 1
    for line in f:
        print(str(i) + ". ", line, end = "")
        i += 1
