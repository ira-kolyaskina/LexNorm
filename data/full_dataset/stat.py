def dataset_stats(inputs, outputs):
    total_words = 0
    changed_words = 0
    unchanged_words = 0
    sentences_with_changes = 0
    sentences_without_changes = 0

    for inp_sentence, out_sentence in zip(inputs, outputs):
        sentence_changed = False  # Флаг, изменялось ли предложение

        for inp, outp in zip(inp_sentence, out_sentence):
            total_words += 1
            if inp != outp:
                changed_words += 1
                sentence_changed = True
            else:
                unchanged_words += 1

        if sentence_changed:
            sentences_with_changes += 1
        else:
            sentences_without_changes += 1

    return {
        "Всего слов": total_words,
        "Измененные слова": changed_words,
        "Неизмененные слова": unchanged_words,
        "Предложения с изменениями": sentences_with_changes,
        "Предложения без изменений": sentences_without_changes
    }


with open("/home/irina/git/LexNorm/data/full_dataset/ALL.txt") as f:
	sentences = f.read().split("\n\n")[:-1]
	sentences = [s.split('\n') for s in sentences]

inputs = [[w.split('\t')[0] for w in s] for s in sentences]
outputs = [[w.split('\t')[1] for w in s] for s in sentences]

stats = dataset_stats(inputs, outputs)
print(stats)

