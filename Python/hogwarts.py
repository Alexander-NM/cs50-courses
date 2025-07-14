students = [
    {"name": "Alex", "home": "MSC", "surname": "MV"},  
    {"name": "Lev" , "home": "MSC", "surname": "MV"},  
    {"name": "Oleg", "home": "KRD", "surname": None},  
]

for student in students:
    print(student["name"], student["home"], student["surname"], sep= ", ")
