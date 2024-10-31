def prime_range(x, y):
    prime_list = []
    for i in range(x, y+1):
        flag = 0
        if i <= 1:
            flag = 1
        for j in range(2, i//2+1):
            if i % j == 0:
                flag = 1
        if flag != 1:
            prime_list.append(i)
    return prime_list

try:
    start = int(input("Enter the start of the range: "))
    stop = int(input("Enter the stop of the range: "))
    print(prime_range(start, stop))
except ValueError:
    print("Please enter a valid number.")
