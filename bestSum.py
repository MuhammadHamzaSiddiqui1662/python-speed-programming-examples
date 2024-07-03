def bestSum(targetSum, numbers, memo):
    if targetSum in memo:
        return memo[targetSum]
    if targetSum < 0:
        return None
    if targetSum == 0:
        return []

    bestPattern = None
    for num in numbers:
        remainder = targetSum-num
        pattern = bestSum(remainder, numbers, memo)
        if pattern is not None:
            pattern = pattern.copy()
            pattern.append(num)
            if bestPattern == None or len(pattern) < len(bestPattern):
                bestPattern = pattern
    memo[targetSum] = bestPattern
    return bestPattern


print(bestSum(7, [5, 3, 4, 7], {}))
print(bestSum(8, [2, 3, 5], {}))
print(bestSum(8, [1, 4, 5], {}))
print(bestSum(100, [1, 2, 5, 25], {}))
