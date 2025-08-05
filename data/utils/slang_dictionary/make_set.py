with open('/home/irina/git/LexNorm/data/slang.txt', 'r', encoding='utf-8') as f1, open('/home/irina/git/LexNorm/data/slang (copy).txt', 'r', encoding='utf-8') as f2:
    words_set = set(word.strip().lower() for word in f1.read().splitlines()) | set(word.strip().lower() for word in f2.read().splitlines())

print(sorted(words_set))
print(len(words_set))

