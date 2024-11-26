from abc import ABC, abstractmethod

class Piece(ABC):
    def __init__(self, color, position):
        """
        Inicializuje šachovou figurku.
        
        :param color: Barva figurky ('white' nebo 'black').
        :param position: Aktuální pozice na šachovnici jako tuple (row, col).
        """
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        """
        Vrací všechny možné pohyby figurky.
        Musí být implementováno v podtřídách.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        
        # Pokud je bílý pěšák, pohybuje se nahoru (zvyšuje se číslo řádku)
        if self.color == "white":
            # Pohyb o jedno políčko vpřed
            if self.is_position_on_board((row + 1, col)):
                moves.append((row + 1, col))
        # Pokud je černý pěšák, pohybuje se dolů (snižuje se číslo řádku)
        elif self.color == "black":
            # Pohyb o jedno políčko zpět
            if self.is_position_on_board((row - 1, col)):
                moves.append((row - 1, col))

        return moves

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        """
        Vrací všechny možné tahy jezdce.
        
        :return: Seznam možných pozic [(row, col), ...].
        """
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]
        # Filtruje tahy, které jsou mimo šachovnici
        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]  # čtyři směry diagonál

        for dr, dc in directions:
            r, c = row, col
            # Pohyb diagonálně, dokud není šachovnice
            while True:
                r += dr
                c += dc
                if self.is_position_on_board((r, c)):
                    moves.append((r, c))
                else:
                    break
        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # vertikální a horizontální směry

        for dr, dc in directions:
            r, c = row, col
            # Pohyb ve směru daného směru (přidání k řádkům a sloupcům)
            while True:
                r += dr
                c += dc
                if self.is_position_on_board((r, c)):
                    moves.append((r, c))
                else:
                    break
        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # všechny směry

        for dr, dc in directions:
            r, c = row, col
            # Pohyb ve směru daného směru (přidání k řádkům a sloupcům)
            while True:
                r += dr
                c += dc
                if self.is_position_on_board((r, c)):
                    moves.append((r, c))
                else:
                    break
        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]  # všechny směry

        for dr, dc in directions:
            r, c = row + dr, col + dc
            if self.is_position_on_board((r, c)):
                moves.append((r, c))
        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    # Testování
    piece1 = Knight("black", (1, 2))
    piece2 = Pawn("white", (2, 2))
    piece3 = Bishop("black", (4, 4))
    piece4 = Rook("white", (1, 1))
    piece5 = Queen("black", (4, 4))
    piece6 = King("white", (5, 5))

    pieces = [piece1, piece2, piece3, piece4, piece5, piece6]

    for piece in pieces:
        print(piece)
        print("Possible moves:", piece.possible_moves())
        print()

