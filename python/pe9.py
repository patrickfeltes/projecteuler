# iterate through possible values of a and b
for a in xrange(1, 1000):
    for b in xrange(a + 1, 1000):
        # since they have to satisfy this sum property, we know what c is
        c = 1000 - a - b
        if a ** 2 + b ** 2 == c ** 2:
            print a * b * c