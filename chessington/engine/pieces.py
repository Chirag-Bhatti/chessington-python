from __future__ import annotations
from abc import ABC, abstractmethod
from chessington.engine.data import Player, Square
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from chessington.engine.board import Board

class Piece(ABC):
    """
    An abstract base class from which all pieces inherit.
    """

    def __init__(self, player: Player):
        self.player = player

    @abstractmethod
    def get_available_moves(self, board: Board) -> List[Square]:
        """
        Get all squares that the piece is allowed to move to.
        """
        pass

    def move_to(self, board, new_square):
        """
        Move this piece to the given square on the board.
        """
        current_square = board.find_piece(self)
        board.move_piece(current_square, new_square)


class Pawn(Piece):
    """
    A class representing a chess pawn.
    """
    def get_available_moves(self, board) -> List[Square]:
        avaliable_moves = []
        current_location = board.find_piece(self)
        player_colour = self.player
        start_row = 1 if player_colour == Player.WHITE else 6
        end_row = 7 if player_colour == Player.WHITE else 0
        direction = 1 if player_colour == Player.WHITE else -1

        one_spaces_up = Square.at(current_location.row + (1 * direction), current_location.col)
        two_spaces_up = Square.at(current_location.row + (2 * direction), current_location.col)

        # End of board
        if current_location.row == end_row:
            return []

        # Starting movement
        if current_location.row == start_row:
            if not (board.get_piece(two_spaces_up) or board.get_piece(one_spaces_up)):
              avaliable_moves.append(two_spaces_up)
            
        # General movement
        if not board.get_piece(one_spaces_up):
            avaliable_moves.append(one_spaces_up)

        return avaliable_moves

class Knight(Piece):
    """
    A class representing a chess knight.
    """

    def get_available_moves(self, board):
        return []


class Bishop(Piece):
    """
    A class representing a chess bishop.
    """

    def get_available_moves(self, board):
        return []


class Rook(Piece):
    """
    A class representing a chess rook.
    """

    def get_available_moves(self, board):
        return []


class Queen(Piece):
    """
    A class representing a chess queen.
    """

    def get_available_moves(self, board):
        return []


class King(Piece):
    """
    A class representing a chess king.
    """

    def get_available_moves(self, board):
        return []