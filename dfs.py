def dfs(maze):
    for v in maze.adjList:
        v.prev = None
        v.dist = float('inf')
        v.visited = False

    stack = stack()
    stack.push(maze.start)
    maze.start.dist = 0
    maze.start.visited = True

    while not stack.isEmpty():
        vertex = stack.pop()
        if vertex.isEqual(maze.exit):
            break

        for neighbor in vertex.neigh:
            if neighbor.visited == False:
                neighbor.dist = vertex.dist + 1
                neighbor.visited = True
                neighbor.prev = vertex
                stack.push(neighbor)

    path = []
    vertex = maze.exit()
    while vertex:
        path.insert(0, vertex)
        vertex = vertex.prev

    return path
