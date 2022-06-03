n       = int(input("Enter the number to calculate: "))

if n < 0:
    print("Negative numbers aren't allowed")

elif n == 0: #or n == 1:
    print("Factorial 0 is: 1")
else:
    i = 1
    Fact = i * n
    while i < n:
        Fact = Fact * i
        i += 1
    print(f"Factorial {n} is: {Fact}")
