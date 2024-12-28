from collections import defaultdict, deque

def solution(e):
    # dfs로 그래프 찾기
    def findGraph(s):
        visited = set() # visited를 set으로 하면 O(1)로 탐색 가능
        dq = deque([s])
        isEight = 0
        nonlocal edgeDict

        while dq: # dfs 시작
            [a, b] = dq.popleft()
            if a in visited: # cycle
                return a, isEight
            visited.add(a)
            if b in edgeDict:
                dq.append([b, edgeDict[b][0]])
                if len(edgeDict[b]) >= 2: # 간선이 두개 이상이면 8자 그래프
                    isEight = 1
        return 0, isEight
    
    edgeDict = defaultdict(list)
    tmp = []
    answer = [0, 0, 0, 0]
    for edge in e:
        edgeDict[edge[0]].append(edge[1])

    for k, v in edgeDict.items():
        if len(v) >= 2:
            tmp.append([k, v])
            if len(v) >= 3: # 이면 정점노드
                answer[0] = k
                break
    # 정점 노드 찾기
    if answer[0] == 0:
        for t in tmp:
            node, edges = t
            if node != findGraph([node, edges[0]])[0]: # 한 노드에서 시작해서 다시 돌아오지 않으면 정점노드
                answer[0] = node
                break
    edge = edgeDict[answer[0]] # 정점노드
    for node in edge:
        [type, isEight] = findGraph([answer[0], node])
        if type == 0: # 0이면 막대그래프
            answer[2] += 1
        else:
            if isEight:
                answer[-1] += 1
            else:
                answer[1] += 1
    return answer
    

    

    
            

print(solution([[2, 3], [4, 3], [1, 1], [2, 1]]))