#!/usr/bin/python3

from sys import path

path.append ('/data/git/Miner')

from classes import Game

game = Game (rows = 5, columns = 7, mines = 6)
while (not game.is_win) and (not game.is_lost):
  game.open_cell ()

print (game)
