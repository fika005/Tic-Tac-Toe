import copy

### An abstract class that other states will inherit from.
class State:

    def __init__(self):
        pass

    def isGoal(self):
        pass

    def successors(self):
        pass

    def __repr__(self):
        pass


## helper function to handle changing left to right.
def flip(side):
    if side == 'left':
        return 'right'
    else:
        return 'left'


## A State for the Fox and Chickens problem. We have four instance variables, representing the four objects.
##  (fox, chicken, grain, boat). Values for them are {'left','right'}"""

class FoxAndChickensState(State):
    def __init__(self, f='left', c='left', g='left', b='left', parent=None):
        self.fox = f
        self.chicken = c
        self.grain = g
        self.boat = b
        self.parent = parent

    def isGoal(self):
        return self.fox == 'right' and self.chicken == 'right' and self.grain == 'right' and self.boat == 'right'

    ## check to make sure that we have not left the fox with the chicken, or the chicken with the grain
    def isValidState(self):
        if self.fox == self.chicken and self.fox != self.boat:
            return False
        if self.chicken == self.grain and self.grain != self.boat:
            return False
        return True

    def __repr__(self):
        return "fox: %s chicken: %s grain: %s boat: %s" % (self.fox, self.chicken, self.grain, self.boat)

### generate all valid successor states, and return them in a list.
    def successors(self):
        successorStates = []
        if self.fox == self.boat:
            s = FoxAndChickensState(flip(self.fox), self.chicken, self.grain, flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        if self.chicken == self.boat:
            s = FoxAndChickensState(self.fox, flip(self.chicken), self.grain, flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        if self.grain == self.boat:
            s = FoxAndChickensState(self.fox, self.chicken, flip(self.grain), flip(self.boat), self)
            if s.isValidState():
                successorStates.append(s)
        s = FoxAndChickensState(self.fox, self.chicken, self.grain, flip(self.boat), self)
        if s.isValidState():
            successorStates.append(s)
        return successorStates


#############
## TicTacToeState

### Helper functions to determine whether we are at a leaf node.

def rowWin(board):
    for row in board:
        if len(set(row)) == 1 and row[0] != ' ':
            return row[0]
    return False


def colWin(board):
    for i in range(3):
        col = [item[i] for item in board]
        if len(set(col)) == 1 and col[0] != ' ' :
            return col[0]
    return False


def diagonalWin(board):
    if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[1][1] != ' ':
        return board[1][1]
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[1][1] != ' ':
        return board[1][1]
    else:
        return False


def boardFull(board):
    if any(x == ' ' for x in board[0]) or any(x == ' ' for x in board[1]) or any(x == ' ' for x in board[2]):
        return False
    else:
        return True

### State representing a Tic-Tac-Toe board. ' ' is used for unfilled squares.

class TicTacToeState(State):
    def __init__(self, board=None):
        self.score = 0
        if board:
            self.board = board
        else:
            self.board = [[' ', ' ', ' '],
                          [' ', ' ', ' '],
                          [' ', ' ', ' ']]

    def isGoal(self):
        ### we have a win
        if rowWin(self.board) or colWin(self.board) or diagonalWin(self.board):
            return True
        elif boardFull(self.board):
            return True
        else:
            return False

    ## move is either 'x' or 'o'
    def successors(self, move):
        successorStates = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == ' ':
                    newBoard = copy.deepcopy(self.board)
                    newBoard[i][j] = move
                    successorStates.append(TicTacToeState(newBoard))

        return successorStates

    ### player is either x or o
    def scoreSelf(self, player):
        winner = rowWin(self.board)
        if not winner:
            winner = colWin(self.board)
        if not winner:
            winner = diagonalWin(self.board)
        if winner:
            if winner == player:
                self.score = 1
            else:
                self.score = -1
        else :
            self.score = 0

    def __repr__(self):
        return " %s\n %s\n %s\n" % (self.board[0], self.board[1], self.board[2])
