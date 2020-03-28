# Name:         Peyton Fitzgerald
# Date:         03/qw/2020
# Description   Contains a Board class, Piece Class (and several piece type child classes), and a XiangqiGame class.
#               These classes work together to replicate the gameplay of Chinese chess.


class Board:
    """
    Board CLass - Creates and initializes pieces for a Xiangqi gameboard. Each of these pieces are created using
    composition with the Piece class and its respective child classes
    """
    def __init__(self):
        self._game_board = [['[ ]'] * 10 for n in range(11)]
        # Column headers
        y = 0
        col_header = '~ABCDEFGHI'
        while y < 10:
            self._game_board[0][y] = col_header[y]
            y += 1

        # row numbers
        x = 1
        while x < 11:
            self._game_board[x][0] = str(x)
            x += 1

        # red piece position initialization
        self._red_general = General(1, 5, 'red')
        self._red_advisor_one = Advisor(1, 4, 'red')
        self._red_advisor_two = Advisor(1, 6, 'red')
        self._red_elephant_one = Elephant(1, 3, 'red')
        self._red_elephant_two = Elephant(1, 7, 'red')
        self._red_horse_one = Horse(1, 2, 'red')
        self._red_horse_two = Horse(1, 8, 'red')
        self._red_chariot_one = Chariot(1, 1, 'red')
        self._red_chariot_two = Chariot(1, 9, 'red')
        self._red_cannon_one = Cannon(3, 2, 'red')
        self._red_cannon_two = Cannon(3, 8, 'red')
        self._red_soldier_one = Soldier(4, 1, 'red')
        self._red_soldier_two = Soldier(4, 3, 'red')
        self._red_soldier_three = Soldier(4, 5, 'red')
        self._red_soldier_four = Soldier(4, 7, 'red')
        self._red_soldier_five = Soldier(4, 9, 'red')

        # Assigning Red Pieces to Board
        self._game_board[1][5] = self._red_general
        self._game_board[1][4] = self._red_advisor_one
        self._game_board[1][6] = self._red_advisor_two
        self._game_board[1][3] = self._red_elephant_one
        self._game_board[1][7] = self._red_elephant_two
        self._game_board[1][2] = self._red_horse_one
        self._game_board[1][8] = self._red_horse_two
        self._game_board[1][1] = self._red_chariot_one
        self._game_board[1][9] = self._red_chariot_two
        self._game_board[3][2] = self._red_cannon_one
        self._game_board[3][8] = self._red_cannon_two
        self._game_board[4][1] = self._red_soldier_one
        self._game_board[4][3] = self._red_soldier_two
        self._game_board[4][5] = self._red_soldier_three
        self._game_board[4][7] = self._red_soldier_four
        self._game_board[4][9] = self._red_soldier_five

        # black piece position initialization
        self._black_general = General(10, 5, 'black')
        self._black_advisor_one = Advisor(10, 4, 'black')
        self._black_advisor_two = Advisor(10, 6, 'black')
        self._black_elephant_one = Elephant(10, 3, 'black')
        self._black_elephant_two = Elephant(10, 7, 'black')
        self._black_horse_one = Horse(10, 2, 'black')
        self._black_horse_two = Horse(10, 8, 'black')
        self._black_chariot_one = Chariot(10, 1, 'black')
        self._black_chariot_two = Chariot(10, 9, 'black')
        self._black_cannon_one = Cannon(8, 2, 'black')
        self._black_cannon_two = Cannon(8, 8, 'black')
        self._black_soldier_one = Soldier(7, 1, 'black')
        self._black_soldier_two = Soldier(7, 3, 'black')
        self._black_soldier_three = Soldier(7, 5, 'black')
        self._black_soldier_four = Soldier(7, 7, 'black')
        self._black_soldier_five = Soldier(7, 9, 'black')

        # Assigning Black Pieces to Board
        self._game_board[10][5] = self._black_general
        self._game_board[10][4] = self._black_advisor_one
        self._game_board[10][6] = self._black_advisor_two
        self._game_board[10][3] = self._black_elephant_one
        self._game_board[10][7] = self._black_elephant_two
        self._game_board[10][2] = self._black_horse_one
        self._game_board[10][8] = self._black_horse_two
        self._game_board[10][1] = self._black_chariot_one
        self._game_board[10][9] = self._black_chariot_two
        self._game_board[8][2] = self._black_cannon_one
        self._game_board[8][8] = self._black_cannon_two
        self._game_board[7][1] = self._black_soldier_one
        self._game_board[7][3] = self._black_soldier_two
        self._game_board[7][5] = self._black_soldier_three
        self._game_board[7][7] = self._black_soldier_four
        self._game_board[7][9] = self._black_soldier_five

        # Storing a list of active pieces for the board
        self._active_pieces = [self._red_general, self._black_general, self._red_advisor_one, self._red_advisor_two,
                               self._red_elephant_one, self._red_elephant_two, self._red_horse_one, self._red_horse_two,
                               self._red_chariot_two, self._red_cannon_one, self._red_cannon_two, self._red_soldier_one,
                               self._red_soldier_two, self._red_soldier_three, self._red_soldier_four,
                               self._red_soldier_five, self._black_advisor_one, self._black_advisor_two,
                               self._black_elephant_one, self._black_elephant_two, self._black_horse_one,
                               self._black_horse_two, self._black_chariot_one, self._black_chariot_two,
                               self._black_cannon_one, self._black_cannon_two, self._black_soldier_one,
                               self._black_soldier_two, self._black_soldier_three, self._black_soldier_four,
                               self._black_soldier_five, self._red_chariot_one, ]

    def get_board(self):
        """
        Getter for the board.
        :return: The board
        """
        return self._game_board

    def remove_captured_piece(self, piece):
        """
        Removes a piece from the list of active pieces.
        :param piece: Piece to be removed.
        """
        self._active_pieces.remove(piece)

    def get_active_pieces(self):
        """
        Gets the list of active pieces on the board.
        :return: The list of active pieces.
        """
        return self._active_pieces

    def get_red_general(self):
        """
        Gets the red general's class instance.
        :return: Red General Instance
        """
        return self._red_general

    def get_black_general(self):
        """
        Get's the black general's class instance
        :return: Gets the black general's class instance
        """
        return self._black_general

    def update_board(self, begin_row, begin_column, end_row, end_column):
        """
        Updates the board to correspond with the movement of a piece (including captures)
        :param begin_row: beginning row of the moving piece
        :param begin_column: beginning column of the moving piece
        :param end_row: target row for movement
        :param end_column: target column for movement
        """

        piece = self._game_board[begin_row][begin_column]

        # if a piece is being captured, remove it from the list of active pieces
        if self._game_board[end_row][end_column] != '[ ]':
            self.remove_captured_piece(self._game_board[end_row][end_column])

        self._game_board[begin_row][begin_column] = '[ ]'
        self._game_board[end_row][end_column] = piece

        # Update the piece's internal data members to reflect its new position
        piece.set_position_x(end_row)
        piece.set_position_y(end_column)


class Piece:
    """
    Parent class for each of the Piece types.
    """

    def __init__(self, x, y, team):
        """
        Initialization
        :param x:
        :param y:
        :param team:
        """
        self._position_x = x
        self._position_y = y
        self._team = team
        self._board_representation = None

    def get_display(self):
        return self._board_representation

    def get_x_position(self):
        return self._position_x

    def get_y_position(self):
        return self._position_y

    def get_team(self):
        return self._team

    def set_position_x(self, x):
        self._position_x = x

    def set_position_y(self, y):
        self._position_y = y

    def capturing_same_team_piece(self, begin_row, begin_column, end_row, end_column, board):
        # Get the piece that will be moving based on the beginning coordinates
        moving_piece = board[begin_row][begin_column]
        potential_ending_piece = board[end_row][end_column]

        if potential_ending_piece != '[ ]' and moving_piece != '[ ]':
            # Make sure a piece isn't moving to a space occupied by a piece on it's own team
            if potential_ending_piece.get_team() == moving_piece.get_team():
                return True
            else:
                return False
        else:
            return False

    def in_palace(self, row, column, team):
        """
        Determines if a given position on the board is in the palace for a given team
        :param row: row of the target position on the board
        :param column: column of the target position on the board
        :param team: the team whose palace we are examining
        :return: True if position is in the palace, false otherwise
        """
        if column == 4 or column == 5 or column == 6:
            if team == 'red':
                if int(row) == 1 or int(row) == 2 or int(row) == 3:
                    return True
                else:
                    return False
            if team == 'black':
                if int(row) == 8 or int(row) == 9 or int(row) == 10:
                    return True
                else:
                    return False
        else:
            return False


class General(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'G' + str(team[0])

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, false otherwise.
        """
        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False
        # Checking to see if the given position is in the palace for that General
        if not self.in_palace(end_row, end_column, self._team):
            return False
        # Checking to see if a legal leftward or rightward movement is being made
        if end_column - begin_column == 0 and (end_row - begin_row == -1 or end_row - begin_row == 1):
            return True
        # Checking to see if a legal upward or downward movement is being made
        elif end_row - begin_row == 0 and (end_column - begin_column == 1 or end_column - begin_column == -1):
            return True
        else:
            # the movement is illegal, so returning false
            return False


class Advisor(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'A' + str(team[0])

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, False otherwise.
        """
        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False

        # Checking to see if the given position is in the palace for that Advisor
        if not self.in_palace(end_row, end_column, self._team):
            return False

        # Checking to see if a legal, diagonal move is being made
        if (end_column - begin_column == 1 or end_column - begin_column == -1) and (
                end_row - begin_row == -1 or end_row - begin_row == 1):
            return True
        else:
            # the move is illegal so returning False
            return False


class Elephant(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'E' + str(team[0])

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, False otherwise.
        """
        column_move_value = end_column - begin_column
        row_move_value = end_row - begin_row

        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False

        # Ensuring the piece isn't trying to cross the river. If so, return False.
        if self._team == 'red' and end_row > 5:
            return False
        if self._team == 'black' and end_row < 6:
            return False

        # checking each of the 4 legal, diagonal movement directions, including whether the first space in each
        # diagonal direction is occupied by a piece (which would block movement in that direction).
        if (column_move_value == 2 and row_move_value == 2) and game_board[begin_row + 1][begin_column + 1] == '[ ]':
            return True
        elif (column_move_value == -2 and row_move_value == -2) and game_board[begin_row - 1][begin_column - 1] == '[ ]':
            return True
        elif (column_move_value == 2 and row_move_value == -2) and game_board[begin_row - 1][begin_column + 1] == '[ ]':
            return True
        elif (column_move_value == -2 and row_move_value == 2) and game_board[begin_row + 1][begin_column - 1] == '[ ]':
            return True
        else:
            # move is illegal, returning False.
            return False


class Horse(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'H' + str(team[0])

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, False otherwise.
        """
        column_move_value = end_column - begin_column
        row_move_value = end_row - begin_row

        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False

        # Checking each of the 8 potential movements for a Horse piece.
        # down and to the diagonal left or right
        if (column_move_value == 1 and row_move_value == 2) and game_board[begin_row + 1][begin_column] == '[ ]':
            return True
        elif (column_move_value == -1 and row_move_value == 2) and game_board[begin_row + 1][begin_column] == '[ ]':
            return True

        # right and to the diagonal up or down
        elif (column_move_value == 2 and row_move_value == 1) and game_board[begin_row][begin_column + 1] == '[ ]':
            return True
        elif (column_move_value == 2 and row_move_value == -1) and game_board[begin_row][begin_column + 1] == '[ ]':
            return True

        # up and to the diagonal left or right
        elif (column_move_value == 1 and row_move_value == -2) and game_board[begin_row - 1][begin_column] == '[ ]':
            return True
        elif (column_move_value == -1 and row_move_value == -2) and game_board[begin_row - 1][begin_column] == '[ ]':
            return True

        # left and to the diagonal left or right
        elif (column_move_value == -2 and row_move_value == 1) and game_board[begin_row][begin_column - 1] == '[ ]':
            return True
        elif (column_move_value == -2 and row_move_value == -1) and game_board[begin_row][begin_column - 1] == '[ ]':
            return True
        else:
            # move is illegal, returning False.
            return False


class Chariot(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'R' + str(team[0])

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, False otherwise.
        """
        piece_in_way = False
        column_move_value = end_column - begin_column
        row_move_value = end_row - begin_row

        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False

        if column_move_value != 0 and row_move_value != 0:
            return False

        # Getting search values for the column - needed so that each of the rows or columns being passed in
        # an orthogonal movement can be checked for pieces as it cannot jump over pieces when moving from
        # point A to point B.
        if begin_column > end_column:
            start_search_column = end_column
            end_search_column = begin_column
        else:
            start_search_column = begin_column
            end_search_column = end_column

        if begin_row > end_row:
            start_search_row = end_row
            end_search_row = begin_row
        else:
            start_search_row = begin_row
            end_search_row = end_row

        # One of the move values must be 0 as the chariot can only move orthogonally - returning false if this isn't
        # the case as that would mean an illegal movement.
        if column_move_value != 0 and row_move_value != 0:
            return False

        if column_move_value != 0 and row_move_value == 0:
            # look through each column in the orthogonal movement and search for a piece occupying a position
            # between the beginning position and the end position
            for y in range(start_search_column + 1, end_search_column):
                if game_board[begin_row][y] != '[ ]' and y != end_column:
                    # if a piece is in the way, flag piece_in_way to reflect that.
                    piece_in_way = True
        if column_move_value == 0 and row_move_value != 0:
            # look through each row in the orthogonal movement and search for a piece occupying a position
            # between the beginning position and the end position
            for x in range(start_search_row + 1, end_search_row):
                if game_board[x][begin_column] != '[ ]' and x != end_row:
                    # if a piece is in the way, flag piece_in_way to reflect that.
                    piece_in_way = True

        # if no piece is in the way, return True.
        if not piece_in_way:
            return True
        else:
            # Otherwise return False as it's an illegal movement.
            return False


class Cannon(Piece):
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'C' + str(team[0])

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, False otherwise.
        """
        # counter variable used to count the number of pieces between a start and end position on the board
        count = 0
        piece_in_way = False
        column_move_value = end_column - begin_column
        row_move_value = end_row - begin_row

        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False

        # Getting search values for the column - needed so that each of the rows or columns being passed in
        # an orthogonal movement can be checked for pieces as it cannot jump over pieces when moving from
        # point A to point B.
        if begin_column > end_column:
            start_search_column = end_column
            end_search_column = begin_column
        else:
            start_search_column = begin_column
            end_search_column = end_column

        if begin_row > end_row:
            start_search_row = end_row
            end_search_row = begin_row
        else:
            start_search_row = begin_row
            end_search_row = end_row

        # One of the move values must be 0 as the cannon can only move orthogonally - returning false if this isn't
        # the case as that would mean an illegal movement.
        if column_move_value != 0 and row_move_value != 0:
            return False

        # look through each column in the orthogonal movement and search for a piece occupying a position
        # between the beginning position and the end position
        if column_move_value != 0 and row_move_value == 0:
            for y in range(start_search_column + 1, end_search_column):
                if game_board[begin_row][y] != '[ ]' and y != end_column:
                    # if a piece is in the way, flag piece_in_way to reflect that, and add 1 to the counter.
                    count += 1
                    piece_in_way = True
        # look through each row in the orthogonal movement and search for a piece occupying a position
        # between the beginning position and the end position
        if column_move_value == 0 and row_move_value != 0:
            for x in range(start_search_row + 1, end_search_row):
                if game_board[x][begin_column] != '[ ]' and x != end_row:
                    # if a piece is in the way, flag piece_in_way to reflect that, and add 1 to the counter.
                    count += 1
                    piece_in_way = True

        # Check to see if the cannon movement is attempting to capture a piece
        if game_board[end_row][end_column] != '[ ]':
            # if only one piece is in the way, return True.
            if piece_in_way and count <= 1:
                return True
            # Otherwise, if multiple pieces are in the way, or if no piece is in the way, the capture is illegal.
            else:
                return False
        # if normal movement is taking place, the cannon operates like a chariot. If no piece is in the way of the
        # movement the move is legal.
        else:
            if not piece_in_way and game_board[end_row][end_column] == '[ ]':
                return True
            else:
                return False


class Soldier(Piece):
    """
    Child class of the Piece class. Represents the Soldier piece in Xiangqi
    """
    def __init__(self, x, y, team):
        super().__init__(x, y, team)
        self._board_representation = 'S' + str(team[0])
        self._upgraded = False

    def legal_move(self, begin_row, begin_column, end_row, end_column, game_board):
        """
        Moves a piece from one location of the board to another.
        :param begin_row: beginning row for piece to move
        :param begin_column: beginning column for piece to move
        :param end_row:  ending row for piece to move to
        :param end_column: ending column for piece to move to
        :param game_board: current active game board being used
        :return: True if move is legal, False otherwise.
        """
        # Make sure the piece isn't capturing a piece of its own team
        if game_board[end_row][end_column] != '[ ]':
            if self.capturing_same_team_piece(begin_row, begin_column, end_row, end_column, game_board):
                return False

        # Flags a soldier as upgraded if they have crossed the river
        if not self._upgraded and self._team == 'red' and begin_row == 6:
            self._upgraded = True

        if not self._upgraded and self._team == 'black' and begin_row == 5:
            self._upgraded = True

        # move logic for upgraded soldiers
        if self._upgraded and self._team == 'red':
            if (-1 <= end_column - begin_column <= 1) and end_row - begin_row == 0:
                return True
            if end_column - begin_column == 0 and end_row - begin_row == 1:
                return True
            else:
                return False

        elif self._upgraded and self._team == 'black':
            if (-1 <= end_column - begin_column <= 1) and end_row - begin_row == 0:
                return True
            if end_column - begin_column == 0 and end_row - begin_row == -1:
                return True
            else:
                return False

        # move logic for a normal soldier that hasn't crossed the river
        elif not self._upgraded and self._team == 'red':
            if end_column - begin_column == 0 and end_row - begin_row == 1:
                return True
            else:
                return False
        elif not self._upgraded and self._team == 'black':
            if end_column - begin_column == 0 and end_row - begin_row == -1:
                return True
            else:
                return False
        else:
            return False


class XiangqiGame:
    """
    A Xiangqi class. Creates a board using the Board class, which contains a number of Piece objects representing
    various Xiangqi pieces, as well as empty spots on the board. A Xiangqi operates on this board to replicate the
    gameplay of Xiangqi - including moving pieces and determining check, checkmate, and stalemate.
    """
    def __init__(self):
        self._active_game = Board()
        self._game_board = self._active_game.get_board()
        self._active_pieces = self._active_game.get_active_pieces()
        self._player_turn = 'red'
        self._game_state = 'UNFINISHED'

        self._black_in_check = False
        self._red_in_check = False

    def get_black_general(self):
        """
        Getter for the black general
        :return: the black general
        """
        return self._active_game.get_black_general()

    def get_red_general(self):
        """
        Getter for the red general
        :return: the red general
        """
        return self._active_game.get_red_general()

    def get_specific_general(self, team):
        """
        Getter for a specific general
        :param team: The team of the general requested
        :return: The general requested
        """
        if team == 'red':
            return self._active_game.get_red_general()
        if team == 'black':
            return self._active_game.get_black_general()

    def get_game_state(self):
        """
        Getter for the game state.
        :return: the current value of the game state member variable.
        """
        return self._game_state

    def is_in_check(self, team):
        """
        Determines if a team is in check
        :param team: the team that the program is checking for check
        :return: True if the given team is in check, False otherwise.
        """
        if team == 'black' and self._black_in_check:
            return True
        elif team == 'red' and self._red_in_check:
            return True
        else:
            return False

    def __get_real_column(self, alg_column):
        """
        Converts the letter for a column to an integer
        :param alg_column: Letter for a column to be turned into an integer.
        :return: The integer version of a letter for a column
        """

        if alg_column[0].lower() == 'a':
            real_column = 1
        elif alg_column[0].lower() == 'b':
            real_column = 2
        elif alg_column[0].lower() == 'c':
            real_column = 3
        elif alg_column[0].lower() == 'd':
            real_column = 4
        elif alg_column[0].lower() == 'e':
            real_column = 5
        elif alg_column[0].lower() == 'f':
            real_column = 6
        elif alg_column[0].lower() == 'g':
            real_column = 7
        elif alg_column[0].lower() == 'h':
            real_column = 8
        elif alg_column[0].lower() == 'i':
            real_column = 9
        else:
            real_column = 0

        return real_column

    def get_turn(self):
        """
        :return: Current player turn
        """
        return self._player_turn

    def print_board(self):
        """
        Prints the current state of the board.
        """
        print_board = [x[:] for x in self._game_board]

        # iterate through each position on the board, and if a piece object is there, change it from the object
        # to that object's display value.
        for x in range(1, 11):
            for y in range(1, 10):
                if print_board[x][y] != '[ ]':
                    print_board[x][y] = self._game_board[x][y].get_display()

        for row in print_board:
            print("{: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} {: >10} ".format(*row))

    def facing_generals(self, begin_row, begin_column, end_row, end_column, moving_piece, inc_board=None):
        facing = True
        # Check if generals would be facing one another after the move
        if inc_board is None:
            board = [x[:] for x in self._game_board]
        else:
            board = [x[:] for x in inc_board]

        # getting x and y positions for each general
        red_gen_x = self.get_red_general().get_x_position()
        red_gen_y = self.get_red_general().get_y_position()
        black_gen_x = self.get_black_general().get_x_position()
        black_gen_y = self.get_black_general().get_y_position()

        # If one of the generals is the moving piece, use the end row and end column for that movement instead of
        # the x and y position stored within the instantiation itself.
        if moving_piece is self.get_red_general():
            red_gen_x = end_row
            red_gen_y = end_column

        if moving_piece is self.get_black_general():
            black_gen_x = end_row
            black_gen_y = end_column

        # if the generals are in the same column, look at the value of each row between them and ensure that
        # at least one piece is there. If so, change facing to false. Otherwise it remains true.
        if black_gen_y == red_gen_y:
            board[begin_row][begin_column] = '[ ]'
            board[end_row][end_column] = moving_piece
            for x in range(red_gen_x, black_gen_x):
                if board[x][red_gen_y] != '[ ]':
                    if board[x][red_gen_y] is not self.get_black_general():
                        if board[x][red_gen_y] is not self.get_red_general():
                            facing = False
        else:
            facing = False

        if facing:
            return True
        else:
            return False

    def is_team_in_check(self, team, moving_piece, captured_piece=None, arg_board=None, end_row=0, end_column=0):
        """
        Determines if a given team is in check
        :param team: Team that the function is looking at to see if they are in check
        :param moving_piece: Piece that is moving
        :param captured_piece: Piece that is being captured
        :param board: Board that is currently being used
        :param end_row: End row of any movement
        :param end_column: End column of any movement
        :return: True if the given team is in check, false otherwise.
        """
        check_determination = False

        # Getting the row and column of the respective general - if the general is moving, the first if statement
        # gets the new location of the general after the move.
        if moving_piece is self.get_red_general() or moving_piece is self.get_black_general():
            check_gen_x = end_row
            check_gen_y = end_column
        elif team == 'black':
            check_gen_x = self.get_black_general().get_x_position()
            check_gen_y = self.get_black_general().get_y_position()
        elif team == 'red':
            check_gen_x = self.get_red_general().get_x_position()
            check_gen_y = self.get_red_general().get_y_position()

        # cycle through each piece on the board of the relevant team and see if it can legally move to the
        # position of the board occupied by the opposing team's general. If so, check is True.
        for piece in self._active_pieces:
            if arg_board is None:
                board = [x[:] for x in self._game_board]
            else:
                board = [x[:] for x in arg_board]
            if piece.get_team() != team and piece is not captured_piece:
                begin_x = piece.get_x_position()
                begin_y = piece.get_y_position()
                if piece.legal_move(begin_x, begin_y, check_gen_x, check_gen_y, board):
                    check_determination = True
                    break

        if check_determination:
            return True
        else:
            return False

    def move_causes_check(self, begin_x, begin_y, end_x, end_y, moving_piece, potential_piece):
        """
        Determine if a player's move would cause their own general to be put in check.
        If so, return False as the move is not legal.
        :param begin_x: Starting x position
        :param begin_y: Starting y position
        :param end_x:  Ending x position
        :param end_y: Ending y position
        :param moving_piece: piece that is moving
        :param potential_piece: the value of the end move position on the board
        :return: True if the move would put the player's own general in check, False otherwise.
        """
        board = [x[:] for x in self._game_board]
        board[begin_x][begin_y] = '[ ]'
        board[end_x][end_y] = moving_piece

        if self.is_team_in_check(moving_piece.get_team(), moving_piece, potential_piece, board, end_x, end_y):
            return True
        else:
            return False

    def determine_win_condition(self):
        """
        Determines whether, given the state of a game board, checkmate or stalemate has been reached.
        This is the case when a player is in check and has no way of moving out of check or a player has no legal
        movements that wouldn't put them in check. If either is the case, the game_state is updated accordingly.
        """
        checkmate = True

        # If black is in check, use the black team general and its coordinates.
        if self._black_in_check or self.get_turn() == 'black':
            checked_team = 'black'
        # If red is in check, use the red team general and its coordinates.
        elif self._red_in_check or self.get_turn() == 'red':
            checked_team = 'red'

        for piece in self._active_pieces:
            board_copy = [item[:] for item in self._game_board]
            if piece.get_team() == checked_team:
                begin_x = piece.get_x_position()
                begin_y = piece.get_y_position()
                for end_x in range(1, 11):
                    for end_y in range(1, 10):
                        if piece.legal_move(begin_x, begin_y, end_x, end_y, board_copy):
                            potential_piece = board_copy[end_x][end_y]
                            board_copy[begin_x][begin_y] = '[ ]'
                            board_copy[end_x][end_y] = piece
                            if not self.facing_generals(begin_x, begin_y, end_x, end_y, piece, board_copy):
                                if not self.is_team_in_check(checked_team, piece, potential_piece, board_copy, end_x, end_y):
                                    checkmate = False
                                    break

        if checkmate:
            if checked_team == 'black':
                self._game_state = 'RED_WON'
            if checked_team == 'red':
                self._game_state = 'BLACK_WON'

    def make_move(self, start, end):
        """
        Using a start and end location, determines if a Xiangqi move is legal, and if so updates the game's
        internal data members to reflect players in check, the game as won by a specific player, or the game as
        unfinished depending on the move.
        :param start: Starting location of the move in algebraic notation
        :param end: Ending location of the move in algebraic notation
        :return: True if the move is legal, false otherwise.
        """
        # If the someone has won the game, return False as the game is over.
        if self._game_state != "UNFINISHED":
            return False
        # Converting move notation to integers in order to properly index the game board
        if len(start) == 3:
            begin_row = int(start[-2:])
        else:
            begin_row = int(start[1:])
        if len(end) == 3:
            end_row = int(end[-2:])
        else:
            end_row = int(end[1:])

        # Making sure that the row values are correct and inbounds
        # If not, return False. Otherwise continue.
        if end_row < 1 or end_row > 10:
            return False
        if begin_row < 1 or begin_row > 10:
            return False

        # Converting the letters to numbers that are relevant to the board
        begin_column = self.__get_real_column(start[0].lower())
        end_column = self.__get_real_column(end[0].lower())

        # Making sure that the column values are correct and inbounds
        # If not, return False. Otherwise continue.
        if end_column < 1 or end_column > 9:
            return False
        if begin_column < 1 or begin_column > 9:
            return False

        # Get the piece that will be moving based on the beginning coordinates
        moving_piece = self._game_board[begin_row][begin_column]

        # make sure we are actually moving a piece and it's not an empty position
        # If so, return False. Otherwise continue.
        if moving_piece == '[ ]':
            return False

        # Make sure it's the right player's team.
        # If not, return False. Otherwise continue.
        if moving_piece.get_team() != self._player_turn.lower():
            return False

        # Grabbing the value of the position to be moved to.
        potential_piece = self._game_board[end_row][end_column]

        # Making sure the piece isn't moving to a space occupied by a piece of its own team
        # If so, return False. Otherwise continue.
        if potential_piece in self._active_pieces and moving_piece in self._active_pieces:
            if potential_piece.get_team() == moving_piece.get_team():
                return False

        if self.facing_generals(begin_row, begin_column, end_row, end_column, moving_piece):
            return False

        if moving_piece.legal_move(begin_row, begin_column, end_row, end_column, self._game_board):
            # Check to see if when a player is in check, the move would take the player out of check
            # if so, allow the move and return True, otherwise return False.
            if self._black_in_check or self._red_in_check:
                copy_of_board = [item[:] for item in self._game_board]
                copy_of_board[begin_row][begin_column] = '[ ]'
                copy_of_board[end_row][end_column] = moving_piece
                if self.is_team_in_check(moving_piece.get_team(), moving_piece, potential_piece,
                                    copy_of_board, end_row, end_column):
                    return False

            if self.move_causes_check(begin_row, begin_column, end_row, end_column, moving_piece, potential_piece):
                return False

            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # If all of the above conditions have been met and the program hasn't returned False,
            # the move is legal, so the board is updated accordingly.
            self._active_game.update_board(begin_row, begin_column, end_row, end_column)
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            new_board_copy = [item[:] for item in self._game_board]
            # Determine if red is in check after the board has been updated.
            # If so, update the member variable to show that red is in check.
            if self.is_team_in_check('red', moving_piece, potential_piece, new_board_copy, end_row, end_column):
                self._red_in_check = True
            else:
                self._red_in_check = False

            # Determine if black is in check after the board has been updated.
            # If so, update the member variable to show that red is in check.
            if self.is_team_in_check('black', moving_piece, potential_piece, new_board_copy, end_row, end_column):
                self._black_in_check = True
            else:
                self._black_in_check = False

            # Change the turn value to the other player's team in preparation for the next turn
            if self._player_turn == 'red':
                self._player_turn = 'black'
            else:
                self._player_turn = 'red'

            self.determine_win_condition()
            # If all of the above conditions are passed, return True for a successful move.
            return True
        else:
            return False

'''
def test_my_game():
    game = XiangqiGame()
    print("\nBeginning Game \n")
    game.print_board()
    print('\n')
    while game.get_game_state() == "UNFINISHED":
        print('Current turn is: ' + str(game.get_turn()))
        if game.is_team_in_check('black'):
            print('\n')
            game.print_board()
            print('black is in check')
            print('\n')
        if game.is_team_in_check('red'):
            print('red is in check')
            print('\n')
        begin = input("Please enter beginning location: ")
        print('\n')
        end = input('Please enter ending location: ')
        if game.make_move(begin, end):
            print('Legal Move - Updating Board')
        else:
            print('Move is not Legal. Try again')
        game.print_board()
        print('GAME STATE IS: ' + str(game.get_game_state()))
'''
