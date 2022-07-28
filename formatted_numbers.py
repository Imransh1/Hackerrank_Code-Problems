def print_formatted(number):
    for n in range(1, number+1):
        len_num = str(n)
        space = bin(number)[2:]
        def_space = str(space)
        octal = oct(n)[2:]
        hexa = hex(n)[2:]
        hexa = hexa.upper()
        binary = bin(n)[2:]
        print(f"{' '* (len(def_space) - len(len_num))}{n}",end= ' ')
        print(f"{' '* (len(def_space) - len(octal))}{octal}",end= ' ')
        print(f"{' '* (len(def_space) - len(hexa))}{hexa}",end= ' ')
        if (len(def_space) - len(binary))>=0:
            print(f"{' '* (len(def_space) - len(binary))}{binary}")
        else:
            print(binary)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)