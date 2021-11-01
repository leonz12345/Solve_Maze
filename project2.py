"""
Math 560
Project 2
Fall 2021

project2.py

Partner 1:
Partner 2:
Date:
"""

# Import math and other p2 files.
import math
from p2tests import *

"""
BFS/DFS function

INPUTS
maze: A Maze object representing the maze.
alg:  A string that is either 'BFS' or 'DFS'.

OUTPUTS
path: The path from maze.start to maze.exit.
"""

def bfs(maze):
    for vertex in maze.adjList:
        vertex.prev = None
        vertex.dist = float('-inf')
        vertex.visited = False
    maze.start.dist = 0
    maze.start.visited = True
    visit = Queue()
    visit.push(maze.start)
    while not visit.isEmpty():
        print(visit)
        vertex = visit.pop()
        print(vertex)
        if vertex.isEqual(maze.exit):
            break
        for neighbor in vertex.neigh:
            if neighbor and not neighbor.visited:
                neighbor.dist = vertex.dist + 1
                neighbor.prev = vertex
                neighbor.visited = True
                visit.push(neighbor)
    path = []
    vertex = maze.exit
    while vertex:
        path.insert(0, vertex.rank)
        vertex = vertex.prev
    print(path)
    return path


def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    if alg == 'BFS':
        print('Entered')
        return bfs(maze)
    else:
        print('Entered')
        return bfs(maze) # CHANGE LATER

"""
Main function.
"""
# if __name__ == "__main__":
#     testMazes(False)

def main():
    testMazes(False)

if __name__ == "__main__":
    main()