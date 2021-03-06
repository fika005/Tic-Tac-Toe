import copy
import random

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
            self.move_orders = []


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
        else:
            self.score = 0

    def __repr__(self):
        return " %s\n %s\n %s\n" % (self.board[0], self.board[1], self.board[2])

    def __lt__(self, other):
        return self.score < other.score

    def __hash__(self):
        return hash(str(self.board))


class EightPuzzleState(State):
    def __init__(self, puzzle_list=None, level=0):
        if puzzle_list:
            self.state = puzzle_list
        else:
            # self.state = [i for i in range(1, 9)] + ['B']
            # random.shuffle(self.state)
            self.state = [1, 'B', 2, 4, 5, 3, 7, 8, 6]
        self.level = level

    def isGoal(self):
        for i, j in zip(range(1, 9), self.state):
            if i != j:
                return False
        return True

    def swap(self, ind1, ind2):
        lst = self.state.copy()
        temp = lst[ind1]
        lst[ind1] = lst[ind2]
        lst[ind2] = temp
        return lst

    def move_blank(self, move):
        blank_index = self.state.index('B')
        if move == 'right':
            if blank_index % 3 == 2:
                return None
            return self.swap(blank_index, blank_index + 1)
        if move == 'left':
            if blank_index % 3 == 0:
                return None
            return self.swap(blank_index, blank_index - 1)
        if move == 'up':
            if blank_index // 3 == 0:
                return None
            return self.swap(blank_index, blank_index - 3)
        if move == 'down':
            if blank_index // 3 == 2:
                return None
            return self.swap(blank_index, blank_index + 3)

    def cost(self):
        cost = 0
        for i, j in zip(range(1, 9), self.state):
            if j == 'B':
                j = 9
            cost += abs(i - j)
        return cost

    def successors(self):
        successor_states = []
        for move in ['left', 'right', 'up', 'down']:
            new_state_list = self.move_blank(move)
            if new_state_list:
                successor_states.append(EightPuzzleState(new_state_list, self.level + 1))
        return successor_states

    def __repr__(self):
        return str(self.state)

    def __lt__(self, other):
        return self.cost() + self.level < other.cost() + other.level

    def __hash__(self):
        return hash(str(self.state))


