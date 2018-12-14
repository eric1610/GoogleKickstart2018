from collections import defaultdict, deque
import sys
sys.setrecursionlimit(1200)
def find_cycle(n, visited, visited_temp, weight_graph, adj_list, curr, parent):
    visited_temp[curr] = True
    for i in adj_list[curr]:
        if not visited_temp[i]:
            cycle_index = find_cycle(n, visited, visited_temp, weight_graph, adj_list, i, curr)
            if cycle_index != -1:
                visited[curr] = True
                weight_graph[curr] = 0
                return cycle_index
        elif parent != i:
            visited[curr] = True
            weight_graph[curr] = 0
            return i
    return -1
	
def print_spaces(n, adj_list):
    visited = [False] * n
    visited_temp = [False] * n
    weight_graph = [-1] * n
    cycle_index = -1
    for i in range(n):
        cycle_index = find_cycle(n, visited, visited_temp, weight_graph, adj_list, i, -1)
        if cycle_index != -1:
            break	
    for i in range(cycle_index):
        visited[i] = False	
    bfs_queue = deque([a for a in range(len(visited)) if visited[a]])
    while bfs_queue:
        index = bfs_queue.popleft()
        
        for next_index in adj_list[index]:
            if not visited[next_index]:
                weight_graph[next_index] = 1 + weight_graph[index]
                bfs_queue.append(next_index)
                visited[next_index] = True
    return ' '.join(str(a) for a in weight_graph)

if __name__ == '__main__':
    tests = int(input())
    for test in range(tests):
        n = int(input())
        adj_list = defaultdict(set)
        for line in range(n):
            start, stop = list(map(int, input().split(' ')))
            start -= 1
            stop -= 1
            if stop not in adj_list[start]:
                adj_list[start].add(stop)
            if start not in adj_list[stop]:
                adj_list[stop].add(start)
        result = print_spaces(n, adj_list)
        print ('Case #{0}: {1}'.format(test + 1, result))
