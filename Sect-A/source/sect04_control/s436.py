# 중첩 for문
matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for x in range(3):
    for y in range(3):
        # print('matrix[', x, '][', y, ']:', matrix[x][y], end=', \t')
        print('matrix[%d][%d]:'%(x, y), matrix[x][y], end=', \t')
    print()
