"""

Домашнее задание №1

Исключения: KeyboardInterrupt

* Перепишите функцию hello_user() из задания while1, чтобы она 
  перехватывала KeyboardInterrupt, писала пользователю "Пока!" 
  и завершала работу при помощи оператора break
    
"""

def hello_user():
    try:
      how_r_u = input('Как дела? ').lower()
      while how_r_u != "хорошо":
          how_r_u = input('Как дела? ').lower()
          if how_r_u == 'хорошо':
            break
    except KeyboardInterrupt:
        print('\nПока!')
hello_user()
    
# if __name__ == "__main__":
#     hello_user()
