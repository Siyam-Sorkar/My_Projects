in_count = 0

while in_count != 999:
    enter = input("> ")
    if enter == "0":
        in_count *= 0
    in_count += 1
    print(in_count)
