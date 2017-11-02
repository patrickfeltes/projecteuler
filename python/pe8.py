f = open('../textfiles/pe8.txt')
s = ''

for line in f:
    s += line.strip()

f.close()

def prod(s):
    p = 1
    for ch in s:
        p *= int(ch)
    return p

ma = 0
for x in xrange(0, len(s) - 13):
    p = prod(s[x: x + 13])
    if p > ma:
        ma = p

print ma