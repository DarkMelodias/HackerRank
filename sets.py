def run():
    # n = int(input())
    # s = set(map(int, input().split()))
    # pasos = int(input())
    # for _ in range(0, pasos):
    #     command = []
    #     command.clear()
    #     command = input().split()
    #     if command[0] == 'discard':
    #         s.discard(int(command[1]))
    #     elif command[0] == 'remove':
    #         s.remove(int(command[1]))
    #     elif command[0] == 'pop':
    #         s.pop()
    
    # print(sum(s))

    n = int(input())
    s = set(map(int, input().split())) 
    for _ in range(int(input())):
        eval('s.{0}({1})'.format(*input().split()+['']))

    print(sum(s))

if __name__ == '__main__':
    run()