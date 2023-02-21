# search.py

"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import funciones
import util


class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    stack = util.Stack()
    visited = []
    path = []

    start = [problem.getStartState(), [], 0]
    stack.push(start)

    while True:

        if stack.isEmpty():
            break

        state = stack.pop()
        isGoal = problem.isGoalState(state[0])

        if isGoal:
            path = state[1]
            break

        isVisited = funciones.isStateVisited(visited, state[0])

        if not isVisited:

            visited.append(state[0])
            path.append(state[1])
            successors = problem.getSuccessors(state[0])
            successors = funciones.filterVisitedSuccessors(successors, visited)
            successors = funciones.updateSuccessors(successors, state)
            stack = funciones.pushSuccessors(successors, stack)

    return path


def breadthFirstSearch(problem):
    queue = util.Queue()
    visited = []

    start = [problem.getStartState(), [], 0]
    queue.push(start)
    path = []

    while True:

        if queue.isEmpty():
            break

        state = queue.pop()
        isGoal = problem.isGoalState(state[0])

        if isGoal:

            path = state[1]
            break

        isVisited = funciones.isStateVisited(visited, state[0])

        if not isVisited:

            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            successors = funciones.filterVisitedSuccessors(successors, visited)
            successors = funciones.updateSuccessors(successors, state)
            queue = funciones.pushSuccessors(successors, queue)

    return path


def uniformCostSearch(problem):
    pqueue = util.PriorityQueue()
    visited = []
    path = []

    start = [problem.getStartState(), [], 0]
    pqueue.push(start, start[2])

    while True:

        if pqueue.isEmpty():
            break

        state = pqueue.pop()
        isGoal = problem.isGoalState(state[0])

        if isGoal:
            path = state[1]
            break

        isVisited = funciones.isStateVisited(visited, state[0])

        if not isVisited:

            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            successors = funciones.filterVisitedSuccessors(successors, visited)
            successors = funciones.updateSuccessors(successors, state)
            pqueue = funciones.pushPQueue(successors, pqueue)

    return path


def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    pqueue = util.PriorityQueue()
    visited = []
    path = []

    start = [problem.getStartState(), [], 0]
    pqueue.push(start, start[2])

    while True:

        if pqueue.isEmpty():
            break

        state = pqueue.pop()
        isGoal = problem.isGoalState(state[0])

        if isGoal:
            path = state[1]
            break

        isVisited = funciones.isStateVisited(visited, state[0])

        if not isVisited:

            visited.append(state[0])
            successors = problem.getSuccessors(state[0])
            successors = funciones.filterVisitedSuccessors(successors, visited)
            successors = funciones.updateSuccessors(
                successors, state)
            successorsHeuristics = funciones.getSuccessorsDistance(
                successors, heuristic, problem)
            pqueue = funciones.pushPQueue(
                successors, pqueue, successorsHeuristics)

    return path


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
