with open("text.txt", "r") as file:   #відкриття файлу
    text = file.readlines()

def letter_edit():            #підрахунок кількості літер
    line_number = 0
    for line in text:
        line_number += 1
        letters_count = len(line)
        print(f'There is {letters_count} letters in {line_number} line')  #виведення в консоль

def words_edit():       #розбивання на слова
    line_number = 0
    for line in text:
        line_number += 1
        word_edit = line.split(" ")
        word_count = len(word_edit)
        print(f'There is {word_count} words in {line_number} line')  #виведення в консоль

letter_edit()
words_edit()
