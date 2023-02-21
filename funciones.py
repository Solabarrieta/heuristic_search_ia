def pushSuccessors(successors, structure):
    for s in successors:
        structure.push(s)
    return structure


def isStateVisited(visited, state):
    return state in visited


def updateSuccessors(successors, parent):
    successorsUpdated = []
    for s in successors:
        successorsUpdated.append(
            (s[0], parent[1] + [s[1]], parent[2] + s[2]))

    return successorsUpdated


def pushPQueue(successors, pqueue, heuristics=None):
    for s in successors:
        if heuristics:
            distance = heuristics[s[0]]
            pqueue.push(s, s[2] + distance)
        else:
            pqueue.push(s, s[2])

    return pqueue


def getSuccessorsDistance(successors, heuristic, problem):
    successorsDistance = {}

    for s in successors:
        successorsDistance[s[0]] = heuristic(s[0], problem)

    return successorsDistance


def filterVisitedSuccessors(successors, visited):
    filtered = []
    for s in successors:
        if s not in visited:
            filtered.append(s)
    return filtered
