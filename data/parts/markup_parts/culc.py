with open("/home/irina/git/LexNorm/data/parts/markup_parts/3.txt", 'r') as f:
    sentences = f.read().split("\n\n")[:-1]

sentences = [s.split('\n') for s in sentences]
print(len(sentences))
inputs = [[w.split('\t')[0] for w in s] for s in sentences]
a = 0
for i in inputs:
    a += len(i)

print(a)
