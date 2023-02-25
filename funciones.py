
class Functions():
    def __init__(self):
        pass

    def pushSuccessors(self, successors, structure):
        for s in successors:
            structure.push(s)
        return structure

    def isStateVisited(self, visited, state):
        return state in visited

    def updateSuccessors(self, successors, parent):
        successorsUpdated = []
        for s in successors:
            successorsUpdated.append(
                (s[0], parent[1] + [s[1]], parent[2] + s[2]))

        return successorsUpdated

    def filterVisitedSuccessors(self, successors, visited):
        filtered = []
        for s in successors:
            if s not in visited:
                filtered.append(s)
        return filtered


class SearchFunctions(Functions):
    def __init__(self, problem):
        self.problem = problem
        super().__init__()

    def pushPQueue(self, successors, pqueue, heuristics=None):
        for s in successors:
            if heuristics:
                distance = heuristics[s[0]]
                pqueue.push(s, s[2] + distance)
            else:
                pqueue.push(s, s[2])

        return pqueue

    def getSuccessorsDistance(self, successors, heuristic):
        successorsDistance = {}
        for s in successors:
            successorsDistance[s[0]] = heuristic(s[0], self.problem)

        return successorsDistance


class CornersFunctions(Functions):

    def __init__(self, problem):
        self.problem = problem
        super().__init__()

    def pushPQueue(self, successors, pqueue, heuristics=None):
        for s in successors:
            if heuristics:
                distance = heuristics[s[0][0]]
                pqueue.push(s, s[2] + distance)
            else:
                pqueue.push(s, s[2])

        return pqueue

    def getSuccessorsDistance(self, successors, heuristic):
        successorsDistance = {}
        for s in successors:
            position, _ = s[0]
            successorsDistance[position] = heuristic(s[0], self.problem)
        return successorsDistance
