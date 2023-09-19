def spiral_pattern(n):
    m = [[0] * n for _ in range(n)]
    dir = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    dir2 = 0  
    row, col = 0, 0  
    num = 1  
    for _ in range(n * n):
        m[row][col] = num
        num += 1
        next_row, next_col = row + dir[dir2][0], col + dir[dir2][1]

        if 0 <= next_row < n and 0 <= next_col < n and m[next_row][next_col] == 0:
            row, col = next_row, next_col
        else:
            dir2 = (dir2 + 1) % 4
            row, col = row + dir[dir2][0], col + dir[dir2][1]

    for i in range(n):
        for j in range(n):
            print(m[i][j], end=' ')
        print()
n = int(input("Enter an integer n: "))

spiral_pattern(n)

