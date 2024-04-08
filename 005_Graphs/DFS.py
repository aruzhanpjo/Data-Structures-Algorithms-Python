def DFS(graph, startV):
    stack = []
    visited = set()
    stack.append(startV)
    # visited.add(startV)
    
    while stack != []:
        cur = stack.pop()
        
        if cur not in visited:
            print(cur)
            visited.add(cur)
            
            for neighbor in graph[cur]:
                stack.append(neighbor)
                
            
gr2 = { 1 : [4,2],
       2: [1,3,5],
       3:[2,4],
       4: [1, 5,3],
       5: [2,4]
         
}
DFS(gr2, 3)
        