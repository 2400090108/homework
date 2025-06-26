from collections import deque
import sys

class Node:
    def __init__(self, value, degree):
        self.value = value
        self.degree = degree
        self.children = []

def build_tree(tokens):
    root = Node(tokens[0], int(tokens[1]))
    queue = deque([root])
    index = 2
    while queue and index < len(tokens):
        current = queue.popleft()
        for _ in range(current.degree):
            child = Node(tokens[index], int(tokens[index + 1]))
            current.children.append(child)
            queue.append(child)
            index += 2
    return root

def postorder(node, output):
    for child in node.children:
        postorder(child, output)
    output.append(node.value)

def main():
    input_lines = sys.stdin.read().splitlines()
    if not input_lines:
        return
    n = int(input_lines[0].strip())
    result = []
    for i in range(1, n+1):
        tokens = input_lines[i].split()
        if not tokens:
            continue
        root = build_tree(tokens)
        temp = []
        postorder(root, temp)
        result.extend(temp)
    print(" ".join(result))

if __name__ == '__main__':
    main()