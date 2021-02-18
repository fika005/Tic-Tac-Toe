


def BFS(initialState) :
    searchQueue = [initialState]

    while len(searchQueue) > 0 :
        currentNode = searchQueue.pop(0)
        if currentNode.isGoal() :
            return currentNode
        else :
            successorStates = currentNode.successors()
            searchQueue.extend(successorStates)
    return None

def flipPlayer(player) :
    if player == 'x' :
        return 'o'
    else :
        return 'x'

##  player will be x or o.

def minimax(initialState, player) :
    if initialState.isGoal() :
        initialState.scoreSelf(player)
        return initialState
    else :
        ### you do this part


