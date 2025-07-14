import re

name = input("What's your name? ").strip()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = f"{matches.group(2).strip()} {matches.group(1).strip()}"
print(f"hello, {name}")
