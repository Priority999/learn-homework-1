"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main(first_word, second_word):
    if first_word == second_word and isinstance(first_word, str) and isinstance(second_word, str):
        return '1'
    elif first_word != second_word and second_word.lower() == 'learn':
        return '3'
    elif first_word != second_word and len(str(first_word)) > len(str(second_word)):
        return '2'
    else:
        return '0'

# Переданные в функцию 1 и 1 не являются строками - возвращаем 0
print(main(1, 1))
# Переданные в функцию строки "Saturn" и "Saturn" являются одинаковыми - возвращаем 1
print(main('Saturn', 'Saturn'))
# Переданные в функцию строки "Jupiter" и "Mars" разные, при этом первая строка длиннее второй - возвращаем 2
print(main('Jupiter', 'Mars'))
# Переданные в функцию строки "Python" и "Learn" разные, во второй строке содержится слово "learn" - возвращаем 3
print(main('Python', 'Learn'))
    
# if __name__ == "__main__":
#     main()
