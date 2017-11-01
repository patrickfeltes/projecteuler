from collections import defaultdict
# memoize some of the chains
memo = defaultdict(int)

def get_chain_length(n):
    if n == 1:
        return 1
    elif memo[n] != 0:
        return memo[n]
    else:
        length = 1
        if n % 2 == 0:
            length += get_chain_length(n / 2)
        else:
            length += get_chain_length(3 * n + 1)
        memo[n] = length
        return length

max_length = 0
starting_number = 0
for x in xrange(1, 10 ** 6):
    length = get_chain_length(x)
    if length > max_length:
        max_length = length
        starting_number = x

print starting_number
