from itertools import product
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

lst = list(product(A,B))
for i in range(len(lst)):
    print(lst[i],end = ' ')