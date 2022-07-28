# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import combinations

N = int(input())
L1 = list(input().split(" "))[:N]
K = int(input())

TUPLES = list(combinations(L1, K))
CONTAINS = [word for word in TUPLES if "a" in word]

print(len(CONTAINS)/len(TUPLES))