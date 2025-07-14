def main():
    heigt = int(input("Height: "))
    piramid(heigt)

def piramid(n):
    for i in range(n):
        print("#" * (i+1))

if __name__ == "__main__":
    main()