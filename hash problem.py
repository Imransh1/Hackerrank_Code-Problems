if __name__ == '__main__':
    n = int(input())
    def solve(t):
        return hash(t)
    integer_list = list(map(int,input().split(' ')))
    t = tuple(integer_list)
    print(solve(t))