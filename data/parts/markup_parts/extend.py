import os

def combine_text_files(folder_path, output_file):
    try:
        files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
        
        text_files = [f for f in files if f.endswith('.txt')]

        if not text_files:
            print("В папке нет текстовых файлов.")
            return

        with open(output_file, 'w', encoding='utf-8') as outfile:
            for file_name in text_files:
                file_path = os.path.join(folder_path, file_name)
                with open(file_path, 'r', encoding='utf-8') as infile:
                    # outfile.write(f"--- Содержимое файла: {file_name} ---\n")
                    outfile.write(infile.read())
                    outfile.write("\n\n")
                    
        print(f"Файлы успешно объединены в {output_file}")
    except Exception as e:
        print(f"Произошла ошибка: {e}")

# Пример использования
folder_path = "/home/irina/git/LexNorm/data/parts/markup_parts/full"
output_file = "/home/irina/git/LexNorm/data/parts/markup_parts/ALL.txt"
combine_text_files(folder_path, output_file)
