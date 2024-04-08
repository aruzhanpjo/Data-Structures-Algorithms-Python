def BFS(startV):
    queue = []
    discovered = set()
    queue.append(startV)
    discovered.add(startV)
    while queue != []:
        cur = queue.pop(0)
        print(cur)
        for neighbor in queue[cur]:
            if neighbor not in discovered:
                queue.append(neighbor)
                discovered.add(neighbor)
                
