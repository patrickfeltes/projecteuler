f = open('../textfiles/pe13.txt')

numbers = []
for line in f:
    numbers.append(int(line.strip()))

f.close()

print str(sum(numbers))[0:10]