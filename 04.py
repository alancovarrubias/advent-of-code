def valid_password(number):
    password = str(number)
    prev = 0
    for c in password:
        num = int(c)
        if num < prev:
            return False
        prev = num

    adjacent = False
    duplicate = None
    for c in password:
        if adjacent:
            if c == prev:
                adjacent = False
            else:
                return adjacent
        elif c == duplicate:
            pass
        elif c == prev:
            adjacent = True
            duplicate = c
        prev = c
    return adjacent

passwords = list(filter(valid_password, range(347312, 805915)))
print(len(passwords))
