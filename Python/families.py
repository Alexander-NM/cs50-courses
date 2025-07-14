import csv

name = input("What's your name? ")
town = input("What's your town? ")

with open("families.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "town"])
    writer.writerow({"name": name, "town": town})