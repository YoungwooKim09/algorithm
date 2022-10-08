import sys

sys.stdin = open('input.txt', 'r')

input = sys.stdin.readline

n = int(input())

tree = {}

for _ in range(n) :
    root, left, right = input().split()
    tree[root] = [left, right]  # 부모 - 자식의 관계를 가지는 노드로 서브 트리를 구성

def preorder(root) :
    if root != '.' :            # root가 '.'되면 함수 종료
        print(root, end = '')   # 기본적으로 print의 end는 \n
        preorder(tree[root][0]) # 함수의 결과값은 오직 return 명령어로만 돌려받을 수 있음 - 이 경우, None(거짓을 나타내는 자료형)
        preorder(tree[root][1]) # print문은 함수의 구성 요소 중 하나인 <수행할 문장>에 해당하는 부분

def inorder(root) :
    if root != '.' :
        inorder(tree[root][0])
        print(root, end = '')
        inorder(tree[root][1])

def postorder(root) :
    if root != '.' :
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end = '')

preorder('A')
print()                         # 개행
inorder('A')
print()
postorder('A')