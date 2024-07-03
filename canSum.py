def canSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum == 0:
        return True
    if targetSum < 0:
        return False
    for number in numbers:
        remainderNum = targetSum-number
        if canSum(remainderNum, numbers, memo) == True:
            memo[targetSum] = True
            return True
    memo[targetSum] = False
    return False


print(canSum(7, [2, 3], {}), 1)
print(canSum(7, [5, 3, 4, 7], {}), 2)
print(canSum(7, [2, 4], {}), 3)
print(canSum(8, [3, 3, 5], {}), 4)
print(canSum(300, [7, 14], {}), 5)
