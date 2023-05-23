import sys

sys.stdin = open('input.txt', 'r')

# 최소 스패닝 트리(Minimum Spanning Tree) : 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 
#                                          그 가중치의 합이 최소인 트리

# 크루스칼(Kruskal) 알고리즘, 프림(Prim) 알고리즘
# 입력값이 달라져서 그래프가 달라져도 최소 비용은 보장되므로 출력값은 동일

input = sys.stdin.readline

V, E = map(int, input().split())

Vertex = [i for i in range(V+1)]           # Vertex = list(range(1, V+1))


Edges = [list(map(int, input().split())) for _ in range(E)]

Edges.sort(key = lambda x : x[2])          # 간선의 가중치가 같으면 입력받은 순서대로 정렬?


def find(k) :

    if k != Vertex[k] :
        Vertex[k] = find(Vertex[k])        # 재귀 함수를 통해 base case 추적

    return Vertex[k]

res = 0

for s, e, w in Edges :

    sRoot = find(s)                        # Vertex[s] - 루트 노드로 갱신이 안돼서 잘못된 추적 발생
    eRoot = find(e)

    if sRoot != eRoot :
        if sRoot > eRoot :
            Vertex[sRoot] = eRoot          # '루트' 노드를 통해 같은 집합인지 확인
        else :
            Vertex[eRoot] = sRoot
        res += w

print(res)

# Kruskal 알고리즘은 간선 선택을 기반으로 하여 이전 단계에서 만들어진 신장 트리와는 상관없이 무조건 최소 간선만을 선택한다.
# 이는 Prim 알고리즘처럼 시작 정점을 기준으로 단계적으로 확장되는 것이 아니므로 루트 노드로 계속 갱신된다는 보장이 없음.
# 가중치가 최소인 간선들을 선택하는 과정에서 노드들이 모두 이어져 있지 않다면, 모든 노드가 루트 노드로 갱신되지 않기 때문에
# 추적 과정이 올바르게 수행되지 않고, 결과적으로 사이클이 형성된다.
# 따라서 재귀 함수를 통해 루트 노드까지의 추적을 실행할 필요가 있다.