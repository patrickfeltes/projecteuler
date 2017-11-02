f = open('../textfiles/pe11.txt')

mat = []
for line in f:
    mat.append(map(int, line.split()))

f.close()

def prod(lst):
    p = 1
    for item in lst:
        p *= item
    return p

def get_col(mat, c):
    lst = []
    for x in xrange(0, len(mat)):
        lst.append(mat[x][c])
    return lst

max_prod = 0

for r in xrange(0, len(mat)):
    for c in xrange(0, len(mat[r])):
        if c <= len(mat[r]) - 4:
            max_prod = max(prod(mat[r][c:c+4]), max_prod)
        if c >= 3:
            max_prod = max(prod(mat[r][c-3:c + 1]), max_prod)
        if r <= len(mat) - 4:
            max_prod = max(prod(get_col(mat, c)[r:r+4]), max_prod)
        if r >= 3:
            max_prod = max(prod(get_col(mat, c)[r - 3: r + 1]), max_prod)
        if r <= len(mat) - 4 and c <= len(mat[r]) - 4:
            diag = []
            for r1 in xrange(0, 4):
                diag.append(mat[r + r1][c + r1])
            max_prod = max(prod(diag), max_prod)
        if c <= len(mat) - 4 and r >= 3:
            diag = []
            for r1 in xrange(0, 4):
                diag.append(mat[r - r1][c + r1])
            max_prod = max(prod(diag), max_prod)
print max_prod
