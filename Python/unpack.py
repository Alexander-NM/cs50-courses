def f(*args, **kwargs):
    print("Positional:", args)

numbers_1 = (1, 44, 55, 44)
numbers_2 = (5, 42, 74, 94)

f(numbers_1, numbers_2)