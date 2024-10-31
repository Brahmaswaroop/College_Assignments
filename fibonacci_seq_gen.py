def fib_num_gen(n):
    fib_list = [None]
    for i in range(0, n):
        if fib_list[0] is None:
            fib_list[0] = 0
        elif len(fib_list) == 1:
            fib_list.append(1)
        else:
            fib_list.append(fib_list[i-1] + fib_list[i-2])
    return fib_list

try:
    x = int(input("Enter the number of terms to print: "))
    y = fib_num_gen(x)
    print((str(y).strip("[]")))
except ValueError:
    print("Please enter a correct response.")
