def dfs(start):
    visited[start]+=1
    res = 0
    for i in arr[start]:
        if i == G:
            res = 1
            return res
        elif visited[i] == 0:
            visited[i]+=1
            if res:
                return res
            else:
                res = dfs(i)
    return res
