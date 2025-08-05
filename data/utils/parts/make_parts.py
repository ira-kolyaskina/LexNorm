
with open('/home/irina/git/LexNorm/data/raw_RUS_DATA.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

sentences = []
current_sentence = []

for line in lines:
    line = line.strip()
    if line:
        current_sentence.append(line)
    else:
        if current_sentence:
            sentences.append(current_sentence)
            current_sentence = []

if current_sentence:
    sentences.append(current_sentence)


def write_to_file(start_index, end_index, sentences):
    filename = f'/home/irina/git/LexNorm/data/parts/{start_index + 1}-{end_index}.txt'
    with open(filename, 'w', encoding='utf-8') as f:
        for sentence in sentences[start_index:end_index]:
            for word in sentence:
                f.write(word + '\t\n')
            f.write('\n')

block_size = 200
for i in range(0, len(sentences), block_size):
    write_to_file(i, min(i + block_size, len(sentences)), sentences)
