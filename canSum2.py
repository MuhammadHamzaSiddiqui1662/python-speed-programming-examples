def canSum(targetSum, numbers):
    table = [False]*(targetSum+1)
    table[0] = True

    for i in range(targetSum+1):
        if(table[i]):
            for num in numbers:
                if(i+num < targetSum+1):
                    table[i+num] = True
    return table[-1]


print(canSum(7, [2, 3]))
print(canSum(7, [5, 3, 4, 7]))
print(canSum(7, [2, 4]))
print(canSum(8, [3, 3, 5]))
print(canSum(300, [7, 14]))
