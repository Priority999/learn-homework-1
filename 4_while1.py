"""

Домашнее задание №1

Цикл while: hello_user

* Напишите функцию hello_user(), которая с помощью функции input() спрашивает 
  пользователя “Как дела?”, пока он не ответит “Хорошо”
   
"""

def hello_user():
    how_r_u = input('Как дела? ').lower()
    while how_r_u != "хорошо":
        how_r_u = input('Как дела? ').lower()
        if how_r_u == 'хорошо':
          break

hello_user()
    
#if __name__ == "__main__":
 #   hello_user()
