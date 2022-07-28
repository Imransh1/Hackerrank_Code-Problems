def print_rangoli(size):
    # your code goes here
    import string
    design = string.ascii_lowercase
    LIST = []
    for iteration in range(size):
        s = "-".join(design[iteration:n])
        LIST.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        
    print('\n'.join(LIST[:0:-1]+LIST))
    
    
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)