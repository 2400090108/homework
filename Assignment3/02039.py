cols = int(input())
encrypted = input()

rows = len(encrypted) // cols
matrix = [['' for _ in range(cols)] for _ in range(rows)]

index = 0
for row in range(rows):
    if row % 2 == 0:
        for col in range(cols):
            matrix[row][col] = encrypted[index]
            index += 1
    else:
        for col in range(cols - 1, -1, -1):
            matrix[row][col] = encrypted[index]
            index += 1

original = ''
for col in range(cols):
    for row in range(rows):
        original += matrix[row][col]
print(original)
