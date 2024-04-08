def BFS(graph,startV):
    queue = []
    discovered = set()
    queue.append(startV)
    discovered.add(startV)
    while queue != []:
        cur = queue.pop(0)
        print(cur)
        
        for neighbor in graph[cur]:
            if neighbor not in discovered:
                queue.append(neighbor)
                discovered.add(neighbor)
                
Graph = { 1: [2,3,4,5],
         2: [1, 6],
         3: [1,6],
         4: [1, 7],
         5: [1, 7],
         6: [2,3, 8],
         7: [4, 5, 8]}

BFS(Graph, 1)


