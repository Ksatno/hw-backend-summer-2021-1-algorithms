import collections
from typing import Any

__all__ = (
    'Node',
    'Graph'
)


class Node:
    def __init__(self, value: Any):
        self.value = value

        self.outbound = []
        self.inbound = []

    def point_to(self, other: 'Node'):
        self.outbound.append(other)
        other.inbound.append(self)

    def __str__(self):
        return f'Node({repr(self.value)})'

    __repr__ = __str__


class Graph:
    def __init__(self, root: Node):
        self._root = root

    def dfs(self) -> list[Node]:
        path = []   
        stack = []  
        stack.append(self._root) 
        while len(stack) != 0:
            print("Стек выглядит так - ", end = "")
            print(*stack)


            node = stack.pop()
            print(f"Взяли из стека - {node}")


            if node not in path:
                path.append(node)

            print("От этой вершины мы можем попасть - ", end="")
            print(f"{node.outbound}")


            for i in range(len(node.outbound)):
                n = node.outbound.pop()
                print(f"Взяли из вершины {n}")

            
                if n not in path:
                    print (f"Поместили на стек  - {n}")
                    stack.append(n)


        print(path)
        return path     

    def bfs(self) -> list[Node]:
        path = []   
        dq = collections.deque()
        dq.append(self._root) 
        while len(dq) != 0:
            print("Очередь выглядит так - ", end = "")
            print(*dq)


            node = dq.popleft()
            print(f"Взяли из стека - {node}")

            if node not in path:
                path.append(node)
            else:
                continue

            print("От этой вершины мы можем попасть - ", end="")
            print(f"{node.outbound}")

            print("Добавим эти вершины в список справа")
            dq.extend(node.outbound)

        # В итоге путь такой
        print(path)
        return path     

a = Node('a')
b = Node('b')

a.point_to(b)
b.point_to(a)

g = Graph(a)
g.bfs()