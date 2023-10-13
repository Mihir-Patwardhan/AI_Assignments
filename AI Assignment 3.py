import random as r
n = int(input("Enter the size of Matrix: "))
matrix = [[0] * n for _ in range(n)]
def print_matrix(matrix):
    for row in matrix:
        print("\t".join(map(str, row)))
for i in range(n):
    used = []
    for j in range(n):
        while True:
            num = r.randint(1, n)
            if num not in used:
                matrix[i][j] = num
                used.append(num)
                break

print_matrix(matrix)