n = int(input())
s = set(map(int, input().split()))
N = int(input())

for testcases in range(N):
    commands = input().split(' ')
    if commands[0] == "pop":
        if len(commands)== 1:
            s.pop()
        elif len(commands) == 2:
            try:
                commands[1] = int(commands[1])
                s.pop(commands[1])
            except:
                pass
        else:
            pass
    elif commands[0] == "remove":
        try:
            commands[1] = int(commands[1])
            s.remove(commands[1])
        except:
            pass
    elif commands[0] == "discard":
        try:
            commands[1] = int(commands[1])
            s.discard(commands[1])
        except:
            pass
    else:
        print("wrong commands")
        
print(sum(s))