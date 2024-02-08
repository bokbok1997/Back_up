def dfs(graph, start_node):
    need_visited.append(start_node)

    while need_visited:
        node = need_visited.pop()
        if node not in visited:
            visited.append(node)
            need_visited.extend(graph[node])
    return visited