#!/usr/bin/python3

def control_count (count, control, minimum = 0, maximum = 10, integer = True):
  '''Функция контроля правильности числовых данных'''

  if integer: count = int   (count)
  else:       count = float (count)

  # Контроль на положительное число
  if   control == 'positive': return count > 0
  elif control == 'in':       return count in range ()
  else:                       return False

if __name__ == '__main__':
  print ('Это модуль с функциями')
