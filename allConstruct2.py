def newComb(comb, word):
    temp = comb.copy()
    temp.append(word)
    return temp


def allConstruct(target, wordbank):
    table = [None]*(len(target)+1)
    for i in range(len(table)):
        table[i] = []
    table[0].append([])

    for i in range(len(table)):
        # if len(table[i]) > 0:
        for word in wordbank:
            if target[i:i+len(word)] == word:
                # temp = combination.copy()
                # temp.append(word)

                # if table[i+len(word)] == []:
                #     table[i+len(word)] = []

                for comb in table[i]:
                    table[i+len(word)].append(newComb(comb, word))
                # table[i+len(word)].map()
    return table[-1]


print(allConstruct('purple', ['purp', 'p', 'ur', 'le', 'purpl']))
print(allConstruct('abcdef', ['ab', 'abc',
      'cd', 'def', 'abcd', 'ef', 'c']))
print(allConstruct('skateboard', [
      'bo', 'rd', 'ate', 't', 'ska', 'sk', 'boar']))
print(allConstruct('eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef', [
    'e',
    'ee',
    'eee',
    'eeee',
    'eeeee',
    'eeeeee'
]))
