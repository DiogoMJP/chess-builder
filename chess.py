from abc import ABC, abstractmethod


class Board():
    def __init__(self, name, width, height):
        self.name = name
        self.size = (width, height)


class MovementRule(ABC):
    @abstractmethod
    def get_movs(self, board, pos):
        pass

    @abstractmethod
    def move(self, board, pos):
        pass


class AbsoluteMovement(MovementRule):
    def __init__(self, mov_list):
        

class Piece():
    def __init__(self, name, image):
        self.name = name
        self.image = image
        self.mov_rules = []
        self.is_piece = False
        self.board = None
        self.pos = None

    def set_piece(self, board, x, y):
        self.board = board
        self.pos = (x, y)
        self.is_piece = True

    def add_movements(self, mov_list, rule_type):
        if rule_type == "ABS":
            self.mov_rules += [lambda pos: [(pos[0] + mov[0], pos[1] + mov[1]) for mov in mov_list]]
        elif rule_type == "REL":
            self.mov_rules += [lambda pos: [mov for mov in mov_list]]

    def get_valid_movements(self):
        mov_list = [mov for mov in movs for movs in [mov_rules(self.pos) for mov_rules in self.mov_rules]]
        print(mov_list)
