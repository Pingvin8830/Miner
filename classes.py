#!/usr/bin/python3

from random import randrange

class Field (object):
  '''Игровое поле'''
  def __init__ (self, rows = 10, columns = 10, mines = 10):
    '''Инициализация поля'''
    self.rows       = rows           # Количество строк
    self.columns    = columns        # Количество столбцов
    self.mines      = mines          # Количество мин
    self.closes     = rows * columns # Количество закрытых ячеек
    self.list_cells = {}             # Ячейки

    # Составление списка ячеек
    for y in range (rows):
      for x in range (columns):
        self.list_cells [(x, y)] = Cell ()

  def clear (self):
    '''Очистка поля'''

    # Сброс количества закрытых ячеек
    self.closes = self.rows * self.columns

    # Сброс самих ячеек
    for y in range (self.rows):
      for x in range (self.columns):
        self.list_cells [(x, y)].__init__ ()


  def set_mines (self):
    '''Расстановка мин'''
    count = 0 # Количество расставленных мин

    # "Перебор мин"
    while count < self.mines:

      # Выбор случайной ячейки
      mines_x = randrange (self.columns)
      mines_y = randrange (self.rows)
      cell    = self.list_cells [(mines_x, mines_y)]

      # Контроль "незанятости"
      if not cell.is_mine:
        cell.is_mine = True

        # Обновление чисел вокруг мины
        for y in range (3):
          for x in range (3):
            try:
              cell_update = self.list_cells [(mines_x - 1 + x, mines_y - 1 + y)]
              if not cell_update.is_mine: cell_update.count += 1
            except:
              continue
        cell.count = 9
        count     += 1

  def __str__ (self):
    string = '  '
    delim  = ' +'
    for x in range (self.columns):
      delim  += '---+'
      string += ' %d  ' % x
    string += '\n' + delim + '\n'
    for y in range (self.rows):
      string += '%d|' % y
      for x in range (self.columns):
        cell = self.list_cells [(x, y)]
        if cell.is_open: string += ' %d |' % cell.count
        else:            string += '   |'
      string += '\n' + delim + '\n'

    return string

class Cell (object):
  '''Ячейка поля'''
  def __init__ (self):
    '''Инициализация ячейки'''
    self.count   = 0      # Число в ячейке
    self.is_mine = False  # Признак мины
    self.is_open = False  # Признак "открытости"

  def __str__ (self):
    return '%d' % self.count

if __name__ == '__main__':
  print ('Это модуль с классами')
