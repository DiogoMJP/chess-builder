from abc import ABC, abstractmethod


Vector = tuple[int, int]


class Game():
    def __init__(self) -> None:
        pass


class Board():
    def __init__(self, name: str, size: Vector) -> None:
        self.name = name
        self.size = size


class Script(ABC):
    @abstractmethod
    def get_value(self, game: Game) -> None:
        pass


class MovementRule(ABC):
    @abstractmethod
    def __init__(self, mov_list: list[Vector], mov_rule: str) -> None:
        pass

    @abstractmethod
    def can_move(self, board: Board, mov: Vector) -> bool:
        pass

    @abstractmethod
    def get_movs(self, board: Board, mov: Vector) -> list[Vector]:
        pass

    @abstractmethod
    def move(self, board: Board, pos: Vector, target: Vector) -> None:
        pass


class AbsoluteMovement(MovementRule):
    def __init__(self, mov_list: list[Vector], mov_rule: str) -> None:
        self.mov_list = mov_list
        self.mov_rule = lambda board, mov: exec(mov_rule)

    def can_move(self, board: Board, mov: Vector) -> bool:
        return self.mov_rule(board, mov)

    def get_movs(self, board: Board, mov: Vector) -> list[Vector]:
        movs = []
        for mov in self.mov_list:
            if self.can_move(board, mov):
                movs += [mov]

        return movs


class RelativeMovement(MovementRule):
    def __init__(self, mov_list: list[Vector], mov_rule: str) -> None:
        self.mov_list = mov_list
        self.mov_rule = lambda board, mov: exec(mov_rule)

    def can_move(self, board: Board, mov: Vector) -> bool:
        return self.mov_rule(board, mov)

    def get_movs(self, board: Board, pos: Vector) -> list[Vector]:
        movs = []
        for mov in self.mov_list:
            if self.can_move(board, mov):
                movs += [(pos[0] + mov[0], pos[1] + mov[1])]

        return movs


class Piece():
    def __init__(self, name: str, image: str) -> None:
        self.name = name
        self.image = image
        self.mov_rules = []
        self.is_piece = False
        self.board = None
        self.pos = None

    def set_piece(self, board: Board, pos: Vector) -> None:
        self.board = board
        self.pos = pos
        self.is_piece = True

    def add_movements(self, mov_list: list[Vector], rule_type: str) -> None:
        if rule_type == "ABS":
            self.mov_rules += [lambda pos: [(pos[0] + mov[0], pos[1] + mov[1]) for mov in mov_list]]
        elif rule_type == "REL":
            self.mov_rules += [lambda pos: [mov for mov in mov_list]]

    def get_valid_movements(self) -> None:
        pass