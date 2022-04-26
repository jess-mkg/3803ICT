import cProfile
from logging import NullHandler
from collections import deque
import time

class PathFinder: 
    def __init__(self, board, chain):
        self.board = board
        self.chain = chain

