mat = []
for x in xrange(21):
    mat.append([0] * 21)

for x in xrange(len(mat)):
    mat[x][0] = 1
    mat[0][x] = 1

for r in xrange(len(mat)):
    for c in xrange(len(mat[r])):
        if mat[r][c] != 0:
            continue
        mat[r][c] = mat[r - 1][c] + mat[r][c - 1]

print mat[20][20]
