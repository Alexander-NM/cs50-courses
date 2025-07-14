with open("name.txt", "r") as file:
    for line in sorted(file, reverse = True):
        print("hello,", line.rstrip())
