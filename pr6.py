text = input("Введите строку, оканчивающуюся точкой: ")

words = text.strip('.').split()

word_count = len(words)

print("Количество слов в строке:", word_count)
