n = int(input("n: "))

if n<0:
    print("Invalid")
elif n == 0 or n == 1:
    print("Fact = 1")
else:
    i = 2
    Fact = 1
    while i < n:
        Fact = Fact * i
        i = i + 1
        print(Fact)