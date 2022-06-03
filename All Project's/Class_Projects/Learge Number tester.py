a = int(input("input a: "))
b = int(input("input b: "))
c = int(input("input c: "))

if a>b:
    if a>c:
        print(f"A is the largest number, and the number is {a}.")
    else:
        print(f"C is the largest number, and the number is {c}.")

else:
    if b>c:
        print(f"B is the largest number, and the number is {b}.")
    else:
        print(f"C is the largest number, and the number is {c}.")