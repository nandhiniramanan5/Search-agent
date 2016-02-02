dict_graph = {}
# Read the data.txt file
with open('data.txt', 'r') as f:
    for l in f:
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = int(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = int(p_cost)


# Breadth First Search Method
def BreadthFirstSearch(graph, src, dst):
    q = [(src, [src], 0)]
    visited = {src}
    while q:
        (node, path, cost) = q.pop(0)
        for temp in graph[node].keys():
            if temp != dst:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                newpath = path + [temp]
                newcost = cost + graph[node][temp]
                return newpath,newcost


# Depth First Search Method
def DepthFirstSearch(graph, src, dst):
    stack = [(src, [src], 0)]
    visited = {src}
    while stack:
        (node, path, cost) = stack.pop()
        for temp in graph[node].keys():
            if temp != dst:
                if temp not in visited:
                    visited.add(temp)
                    stack.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                newpath = path + [temp]
                newcost = cost + graph[node][temp]
                return newpath,newcost
                


# Iterative Deepening Search Method
def IterativeDeepening(graph, src, dst):
    level = 0
    count = 0
    stack = [(src, [src], 0)]
    visited = {src}
    while True:
        level += 1
        while stack:
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in graph[node].keys():
                    if temp != dst:
                        if temp not in visited:
                            visited.add(temp)
                            count += 1
                            stack.append((temp, path + [temp], cost + graph[node][temp]))
                    else:
                        newpath = path + [temp]
                        newcost = cost + graph[node][temp]
                        return newpath,newcost
                        
            else:
                q = stack
                visited_bfs = {src}
                while q:
                    (node, path, cost) = q.pop(0)
                    for temp in graph[node].keys():
                        if temp != dst:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                        else:
                            newpath = path + [temp]
                            newcost = cost + graph[node][temp]
                            return newpath,newcost
                            
                break


n = 1
print dict_graph
print "-----------------------------------------------"
while n == 1:
    src = raw_input("Enter the source: ")
    dst = raw_input("Enter the Destination: ")
    while src not in dict_graph or dst not in dict_graph:
        print "No such city name"
        src = raw_input("Enter the correct source (case_sensitive): ")
        dst = raw_input("Enter the correct destination(case_sensitive):  ")
    x = input("enter the type of search you want to do\n1.BFS 2.DFS 3.ID:: ")
    if x == 1:
        print "for BFS"
        print (BreadthFirstSearch(dict_graph, src, dst))

    elif x == 2:
        print "for DFS"
        print (DepthFirstSearch(dict_graph, src, dst))

    elif x == 3:
        print "for ID"
        print (IterativeDeepening(dict_graph, src, dst))

    n = input("enter 1 if you wish to continue:\n")
