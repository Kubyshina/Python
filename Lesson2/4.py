# Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки
# нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове

userInput = input("Введите строку из нескольких слов, разделённых пробелами:\n")
wordsList = userInput.split(" ")

for i in range(len(wordsList)):
    print(f"{i+1} {wordsList[i][0:10]}")
