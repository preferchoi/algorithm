N = int(input())
key1, key2 = 3, 5

depth = N // (key1 * key2) * key1

N2 = N % (key1 * key2)

if N2 % key2 == 0:
    depth += N2 // key2
elif N2 % key1 == 0:
    depth += N2 // key1
else:
    depth = -1

print(depth)