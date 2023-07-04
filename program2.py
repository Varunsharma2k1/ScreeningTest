def program2(a):
    series = []
    for i in range(1, a + 1):
        if i % 2 != 0:
            series.append(i)
    return series


a = int(input("Enter the value of a: "))

series = program2(a)
print(*series)
