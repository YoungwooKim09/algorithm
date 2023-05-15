import sys, heapq

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b, c = map(int, input().split())

    graph[a].append((c, b))

s, e = map(int, input().split())

INF = int(1e9)

distance = [INF] * (N + 1)                              # 시작 노드로부터 임의의 노드까지의 최단 거리 테이블


def dijkstra(start) :
    heap = []
    distance[start] = 0                                 # 시작 노드까지의 최단 거리 0으로 초기화
    heapq.heappush(heap, (0, start))

    while heap :
        dist, now = heapq.heappop(heap)                 # dist - 시작 노드에서 해당 노드까지의 거리 확인 (직전 노드와의 거리 아님!)
                                                        # now 까지의 거리가 dist - now 까지 도달하기 위한 최단 거리 dist
        if distance[now] < dist :                       # 이후 해당 노드를 거쳐가는 각각의 경우까지 고려
            continue                                    # now 노드를 거쳐가는 것을 기준으로 인접 노드에 대한 최단 거리 갱신
                                                        
        for i in graph[now] :                           # 인접 노드까지의 거리는 graph에 저장되어 있음
            cost = dist + i[0]

            if cost < distance[i[1]] :
                distance[i[1]] = cost                   # (dist, now)의 dist는 distance[now]와 대응 - 갱신된 값이 distance에 저장됨
                heapq.heappush(heap, (cost, i[1]))      # 갱신된 최단 거리 테이블로부터 값을 가져와 저장
                                                        # 갱신될 때마다 우선 순위 큐에 넣어줌으로써 i[1]의 인접 노드들에 대해서도
dijkstra(s)                                             # 위 과정을 반복할 수 있도록 함
print(distance[e])

# if distance[now] < dist :
#             continue 
