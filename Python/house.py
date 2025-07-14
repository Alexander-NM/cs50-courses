name = input("What's your name? ")

match name:
    case "Alex" | "Lev":
        print("Makoveev")
    case "Elene":
        print("Ivleva")
    case _:
        print("Who?")    

ff = ""
ff.strip().lower()