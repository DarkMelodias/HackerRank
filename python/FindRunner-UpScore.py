def run():
    
    i = int(input())
    lis = list(map(int,input().strip().split()))[:i]
    z = max(lis)
    while max(lis) == z:
        lis.remove(max(lis))
    
    print (max(lis))
    

if __name__ == '__main__':
    run()