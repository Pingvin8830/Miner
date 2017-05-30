#!/usr/bin/python3

from random import randrange

class Field (object):
  '''Игровое поле'''
  def __init__ (self, rows = 10, columns = 10, mines = 10):
    self.rows       = rows
    self.columns    = columns
    self.mines      = mines
    self.list_cells = {}

    for y in range (rows):
      for x in range (columns):
        self.list_cells [(x, y)] = Cell (x, y)

  def set_mines (self):
    count = 0
    while count < self.mines:
      cell = self.list_cells [(randrange (self.columns), randrange (self.rows))]
      if not cell.is_mine:
        cell.is_mine = True
        for y in range (3):
          for x in range (3):
            try:
              cell_update = self.list_cells [(cell.x - 1 + x, cell.y - 1 + y)]
              if not cell_update.is_mine: cell_update.count += 1
            except:
              continue
        cell.count   = 9
        count       += 1

  def __str__ (self):
    string = '  '
    delim = ' +'
    for x in range (self.columns):
      delim += '---+'
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
  def __init__ (self, x, y):
    self.x       = x
    self.y       = y
    self.count   = 0
    self.is_mine = False
    self.is_open = False

  def __str__ (self):
    return '(%d, %d)' % (self.x, self.y)

if __name__ == '__main__':
  print ('Это модуль с классами')
