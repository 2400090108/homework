class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_number = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, number):
        node = self.root
        for digit in number:
            if digit not in node.children:
                node.children[digit] = TrieNode()
            node = node.children[digit]
            if node.is_end_of_number:
                return False

        node.is_end_of_number = True
        return len(node.children) == 0

    def is_consistent(self, numbers):
        numbers.sort(key=len)
        for number in numbers:
            if not self.insert(number):
                return False
            return True

def main():
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    results = []

    for _ in range(t):
        n = int(data[index])
        index += 1
        numbers = data[index:index + n]
        index += n

        trie = Trie()
        if trie.is_consistent(numbers):
            results.append("YES")
        else:
            results.append("NO")

    print("\n".join(results))

if __name__ == "__main__":
    main()
