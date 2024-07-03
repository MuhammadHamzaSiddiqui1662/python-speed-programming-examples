def canConstruct(target, wordbank, memo):
    if target in memo:
        return memo[target]
    if target == '':
        return True

    for word in wordbank:
        if target.find(word) == 0:
            word = target[len(word):]
            if canConstruct(word, wordbank, memo):
                memo[target] = True
                return True

    memo[target] = False
    return False


print(canConstruct('abcdef', ['ab', 'abc', 'def', 'abcd'], {}))
print(canConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar'], {}))
print(canConstruct('enterapotentpot', [
      'a', 'p', 'ent', 'enter', 'ot', 'o', 't'], {}))
print(canConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
], {}))
