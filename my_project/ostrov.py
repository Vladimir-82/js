def get_the_vowels(word):
    word = [w for w in word if w in 'aeiou']
    res = []
    counter = 0
    for i in range(len(word) - 1):
        if word[i] < word[i + 1]:
            counter += 1
        else:
            res.append(counter)
            counter = 0
    return max(res)

string = "agrtertyfikfmroyrntbvsukldkfa"
print(get_the_vowels(string))