if __name__ == '__main__':
    N = int(input())
    array = []
    temp_array = []
    for testcases in range(N):
        commands = input().split(' ')
        if commands[0] == "append":
            for i in range(len(commands)- 1):
                i+=1
                array.append(commands[i])
                array[i-1] = int(array[i-1])
                i-=1
            for j in range(len(array)):
                temp_array.append(array[j])
            print(temp_array)
            array.clear()
        elif commands[0] == "pop":
            temp_array.pop()
            print(temp_array)
        elif commands[0] == "remove":
            commands[1] = int(commands[1])
            temp_array.remove(commands[1])
            print(temp_array)
        elif commands[0] == "reverse":
            temp_array.reverse()
            print(temp_array)
        elif commands[0] == "sort":
            temp_array.sort()
        elif commands[0] == "print":
            print(temp_array)
        elif commands[0] == "insert":
            commands[1] = int(commands[1])
            commands[2] = int(commands[2])
            temp_array.insert(commands[1],commands[2])
            print(temp_array)
        else:
            print("wrong commands")