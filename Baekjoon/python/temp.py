import sys
input = sys.stdin.readline
INF = 1e7
n = int(input())
# 입력으로 받은 비용 행렬
cost_arr = [list(map(int, input().split())) for x in range(n)]
# 모든 경로에 대한 최소비용 리스트
dist_arr = [[0] * (1 << n) for x in range(n)] # 0의 개수(열의 개수)가 2^n개
# start에서 출발해서 route에 포함되지 않은(아직 방문하지 않은) 도시를 모두 방문했을 때 드는 최소 비용을 return
def traveling_salesman(start, route): # 여기서 route는 이진수로 표현됨 00011 이라면 -> 도시1, 도시2 방문
    # 최소비용 리스트에 값이 있으면 그냥 가져옴(DP)
    if dist_arr[start][route]:
        return dist_arr[start][route]
    # route의 모든 비트가 1 = 모든 곳을 방문
    # 다시 시작점으로 복귀
    if route == (1 << n) - 1: # 2^n-1 이므로 111...1 임
        return cost_arr[start][0] if cost_arr[start][0] > 0 else INF
    cost = INF
    # 다시 시작점으로 돌아오기 때문에 한점에서 출발하는 경우만 계산해도 됨
    for i in range(1, n):
        # i번째 도시 방문 여부 체크 and 길이 연결되어 있는지 체크
        if not route & (1 << i) and cost_arr[start][i]:
            # i와 i번째 도시를 방문으로 갱신한 route로 재귀
            value = traveling_salesman(i, route | (1 << i))
            cost = min(cost, value + cost_arr[start][i]) # 예시: 0->1로 간 경우 : cost_arr[start][i] = 0->1 비용, value = 1에서부터 다시 0으로 돌아오는 최소 cost
    dist_arr[start][route] = cost
    return dist_arr[start][route]
print(traveling_salesman(0, 1))