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

def bdfs(maze, alg):
    # If the alg is not BFS or DFS, raise exception.
    if (alg != 'BFS') and (alg != 'DFS'):
        raise Exception('Incorrect alg! Need BFS or DFS!')
    
    # Initialize Maze
    for vertex in maze.adjList:
        vertex.prev = None
        vertex.dist = float('-inf')
        vertex.visited = False

    if alg == 'BFS':
        # BFS uses a queue
        visit = Queue()
    else:
        # DFS uses a stack
        visit = Stack()

    # Set start vertex distance and visited
    maze.start.dist = 0
    maze.start.visited = True
    # Push into visit
    visit.push(maze.start)
    # Keep visting untile visit is empty
    while not visit.isEmpty():
        # Remove the front/top of visit
        vertex = visit.pop()
        # Exit if reached the end
        if vertex.isEqual(maze.exit):
            break
        # Iterate through all the neighbors
        for neighbor in vertex.neigh:
            # If neighbor is not seen before
            if not neighbor.visited:
                # Add to visited and change its field
                neighbor.dist = vertex.dist + 1
                neighbor.prev = vertex
                neighbor.visited = True
                visit.push(neighbor)
    # Backtrace to find the shortest path
    path = []
    vertex = maze.exit
    while vertex:
        path.insert(0, vertex.rank)
        vertex = vertex.prev
    return path

"""
Main function.
"""
if __name__ == "__main__":
    testMazes(False)