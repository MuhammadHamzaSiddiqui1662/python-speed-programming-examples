# import math
# def allConstruct(target, wordbank, memo):
#     if target in memo:
#         return memo[target]
#     if target == '':
#         return [[]]

#     allCombos = []
#     for word in wordbank:
#         if target.find(word) == 0:
#             newTarget = target[len(word):]
#             combos = allConstruct(newTarget, wordbank, memo)
#             for arr in combos:
#                 arr.insert(0, word)
#                 allCombos.append(arr.copy())
#             memo[target] = combos.copy()
#     return allCombos


# print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl'], {}))
# print(allConstruct('abcdef', ['ab', 'abc',
#       'cd', 'def', 'abcd', 'ef', 'c'], {}))
# print(allConstruct('skateboard', [
#       'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
# print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
#     'e',
#     'ee',
#     'eee',
#     'eeee',
#     'eeeee',
#     'eeeeee'
# ], {}))



def a(b):
    b = b+[5]
    return b
c = [1,2,3,4]
c=a(c)
print(len(c))
print(c)
print([1,2]+[3,4])

age = {}
age["hamza"] = 18
age["hadia"] = 30
print(age)

t = ("a","b")

a=[1,2,3,4,5]
x=frozenset(a)
# x.append(7)
print(x[0])
print(a)


