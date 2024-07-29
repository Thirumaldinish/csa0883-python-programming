import itertools
n = input("Enter the number: ")
res = list(itertools.permutations(n))
for i in res:
    print(''.join(i))
