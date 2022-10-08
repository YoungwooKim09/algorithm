import sys

sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(10**6)

preorder = []

while True :
    try :
        preorder.append(int(sys.stdin.readline()))  # 실행할 코드

    except :
        break                                       # 예외가 발생했을 때 처리하는 코드

def postorder(start, end) :

    mid = 0

    if start > end :
        return

    for i in range(start + 1, end + 1) :
        if preorder[start] < preorder[i] :
            mid = i
            break

    else :
        mid = end + 1
        
    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(preorder[start])

postorder(0, len(preorder) - 1)

# from __future__ import annotations
# import sys
# from typing import Any

# sys.stdin = open('input.txt', 'r')

# nodeList = list(map(int, sys.stdin.read().splitlines()))


# class Node :


#     def __init__(self, key : Any, left: Node = None, right: Node = None) :

#         self.key = key
        
#         self.left = left
#         self.right = right


# class BinarySearchTree :


#     def __init__(self) :

#         self.root = None


#     def add(self, key: Any) -> bool:

#         def add_node(node: Node, key: Any) -> None:

#             if key == node.key :
#                 return False

#             elif key < node.key :
#                 if node.left is None :
#                     node.left = Node(key, None, None)

#                 else :
#                     add_node(node.left, key)

#             else :
#                 if node.right is None:
#                     node.right = Node(key, None, None)

#                 else :
#                     add_node(node.right, key)

#             return True

#         if self.root is None :
#             self.root = Node(key, None, None)

#         else :
#             return add_node(self.root, key)


#     def dump(self) -> None:

#         def postorder(node: Node) :
#             if node is not None :
#                 postorder(node.left)
#                 postorder(node.right)
#                 print(node.key)
        
#         postorder(self.root)


# bst = BinarySearchTree()

# for node in nodeList :
#     bst.add(node)

# bst.dump()