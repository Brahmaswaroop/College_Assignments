def fact1(num):
    if num <= 1:
        return 1
    else:
        return num * fact1(num-1)

def fact2(num):
    fact = 1
    for i in range(num, 0, -1):
        fact = fact * i
    return fact

try:
    while True:
        x = int(input("Enter the number: "))
        print(f"The factorial of {x} in recursive case = {fact1(x)}")
        print(f"The factorial of {x} in iterative case = {fact2(x)}")
except ValueError:
    print("Please type a number next time ^_^")
