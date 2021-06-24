"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
"""

with open("1.txt", "r", encoding="utf-8") as file:
    file_content = file.readlines()
    str_num = len(file_content)
    print(f"В файле {str_num} строк")
    for i in range(0, str_num):
        print(f"В {i + 1} строке {len(file_content[i].split())} слов")
