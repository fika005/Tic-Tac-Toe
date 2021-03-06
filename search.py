from state import EightPuzzleState, TicTacToeState
from heapq import heappush


def BFS(initialState):
    searchQueue = [initialState]
    closed_set = set()
    num_states_generated = 0
    while len(searchQueue) > 0:
        currentNode = searchQueue.pop(0)
        if currentNode in closed_set:
            continue
        closed_set.add(currentNode)
        if currentNode.isGoal():
            return currentNode, num_states_generated
        else:
            successorStates = currentNode.successors()
            successorStates = [x for x in successorStates if x not in closed_set]
            num_states_generated += len(successorStates)
            searchQueue.extend(successorStates)
    return None, num_states_generated


def DFS(initialState):
    searchQueue = [initialState]
    closed_set = set()
    num_states_generated = 0
    while len(searchQueue) > 0:
        currentNode = searchQueue.pop()
        closed_set.add(currentNode)
        if currentNode.isGoal():
            return currentNode, num_states_generated
        else:
            successorStates = currentNode.successors()
            successorStates = [x for x in successorStates if x not in closed_set]
            num_states_generated += len(successorStates)
            searchQueue.extend(successorStates)
    return None, num_states_generated


def DLS(initialState, limit_depth=10):
    searchQueue = [initialState]
    closed_set = set()
    num_states_generated = 0
    depth = 0
    while len(searchQueue) > 0:
        currentNode = searchQueue.pop()
        if currentNode in closed_set:
            continue
        if currentNode is None:
            depth -= 1
            continue
        else:
            depth += 1
        closed_set.add(currentNode)
        if currentNode.isGoal():
            return currentNode, num_states_generated
        else:
            successorStates = currentNode.successors()
            searchQueue.append(None)
            if depth < limit_depth:
                successorStates = [x for x in successorStates if x not in closed_set]
                num_states_generated += len(successorStates)
                searchQueue.extend(successorStates)
    return None, num_states_generated


def IDS(initialState, max_depth=100):
    num_states_generated = 0
    for i in range(max_depth):
        result, num_states = DLS(initialState, i)
        num_states_generated += num_states
        if result is not None:
            return result, num_states_generated
    return None, num_states_generated


def A_star(initialState):
    searchQueue = []
    heappush(searchQueue, initialState)
    num_states_generated = 0
    closed_set = set()
    while len(searchQueue) > 0:
        currentNode = searchQueue[0]
        del searchQueue[0]
        closed_set.add(currentNode)
        if currentNode.isGoal():
            return currentNode, num_states_generated
        else:
            successorStates = currentNode.successors()
            for successorState in successorStates:
                if successorState not in closed_set:
                    num_states_generated += 1
                    heappush(searchQueue, successorState)
    return None, num_states_generated


def flipPlayer(player) :
    if player == 'x':
        return 'o'
    else :
        return 'x'


##  player will be x or o.
def minimax(initialState, player):
    if initialState.isGoal():
        initialState.scoreSelf(player)
        return initialState.score
    else:
        best_score = 100
        for state in initialState.successors(player):
            score = minimax(state, flipPlayer(player))
            if score < best_score:
                best_score = score
        return -best_score


def find_best_move(state, player):
    best_score = 100
    best_state = None
    for state in state.successors(player):
        score = minimax(state, flipPlayer(player))
        if score < best_score:
            best_score = score
            best_state = state
    return best_state


if __name__ == '__main__':
    eight_puzzle = EightPuzzleState()
    print(eight_puzzle)
    for algo in [BFS, DLS, IDS, A_star]:
        print(f"Algo: {str(algo)}, number of generated states:{algo(eight_puzzle)[1]}")

    tic_tac_toe_state = TicTacToeState()
    player = 'x'
    while not tic_tac_toe_state.isGoal():
        i, j = input(f"Your move player {player}: ").split()
        if tic_tac_toe_state.board[int(i)][int(j)] == ' ':
            tic_tac_toe_state.board[int(i)][int(j)] = player
        else:
            continue
        print(tic_tac_toe_state)
        if tic_tac_toe_state.isGoal():
            print(f"{player} won!")
            break
        tic_tac_toe_state = find_best_move(tic_tac_toe_state, 'o')
        print(tic_tac_toe_state)
        if tic_tac_toe_state.isGoal():
            print(f"{flipPlayer(player)} won!")
            break

