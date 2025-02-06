def remove_inpt_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as infile, open(output_file, 'w', encoding='utf-8') as outfile:
        skip_next = False  # Флаг для пропуска следующей строки
        for line in infile:
            if skip_next:
                # Пропускаем строку после 'INPT:'
                skip_next = False
                if line.strip():  # Проверяем, не пустая ли строка
                    outfile.write(line)
                continue
            if line.startswith('INPT:'):
                skip_next = True  # Устанавливаем флаг для пропуска следующей строки
            elif line.strip():  # Записываем строку, если она не пустая
                outfile.write(line)

# Укажите пути к файлам
input_file = '/home/irina/git/LexNorm/data/parts/markup_parts/ans_1201-1400.txt'
output_file = '/home/irina/git/LexNorm/data/parts/markup_parts/12.txt'

# Выполнение функции
remove_inpt_lines(input_file, output_file)
