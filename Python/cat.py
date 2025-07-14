def main():
    number = get_number()
    love(number)

def get_number():
    while True:
        n = int(input("what's n? "))
        if n > 0:
            return n
   
def love(n):    
    for _ in range(n):
        print('I love my family')

main()