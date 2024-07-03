def bestSum(target, numbers):
    table = [None]*(target+1)
    table[0] = []

    for i in range(target+1):
        if table[i] != None:
            for num in numbers:
                if i+num < target+1:
                    temp = table[i].copy()
                    temp.append(num)
                    if table[i+num] == None or len(table[i+num]) > len(temp):
                        table[i+num] = temp
    return table[-1]


print(bestSum(7, [5, 3, 4, 7]))
print(bestSum(8, [2, 3, 5]))
print(bestSum(8, [1, 4, 5]))
print(bestSum(100, [1, 2, 5, 25]))
