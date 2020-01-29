def product(maliste):
    total = 1
    for num in maliste:
        total = total * num
    return total


print(product([4, 5, 5]))  # 100
