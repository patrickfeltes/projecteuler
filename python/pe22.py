f = open('../textfiles/pe22.txt')

names = map(lambda x: x.replace('\"', ""), f.readline().split(','))
names.sort()

f.close()

total = 0
for i in xrange(len(names)):
    score = 0
    for char in names[i]:
        score += ord(char) - ord('A') + 1
    score *= (i + 1)
    total += score

print total
