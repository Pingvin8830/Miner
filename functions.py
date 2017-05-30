#!/usr/bin/python3

def control_count (count, control, integer = True):
  '''Функция контроля правильности числовых данных'''

  if integer: count = int   (count)
  else:       count = float (count)

  # Контроль на положительное число
  if control == 'positive': return count > 0
  else:                     return False

if __name__ == '__main__':
  print ('Это модуль с функциями')
