def add_one(digits):
    count = len(digits) - 1
    x = 0
    for num in digits:
        x += num * (10 ** count)
        count -= 1
    x += 1

    res = []
    if x < 10:
        a = x % 10
        res.append(a)
    elif 10 <= x < 10 ** 2:
        a = x % 10
        b = x % (10 ** 2) // 10
        res.append(b)
        res.append(a)
    elif 10 ** 2 <= x < 10 ** 3:
        a = x % 10
        b = x % (10 ** 2) // 10
        c = x % (10 ** 3) // 100
        res.append(c)
        res.append(b)
        res.append(a)
    elif 10 ** 3 <= x < 10 ** 4:
        a = x % 10
        b = x % (10 ** 2) // 10
        c = x % (10 ** 3) // 100
        d = x % (10 ** 4) // 1000
        res.append(d)
        res.append(c)
        res.append(b)
        res.append(a)
    elif x >= 10**4:
        res.append(0)
        res.append(0)
        res.append(0)
        res.append(0)

    return res


digit_list = [9, 9, 9, 9]
print(add_one(digit_list))
