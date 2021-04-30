# https://codeforces.com/problemset/problem/580/A

def split(string):
    return [char for char in string]

def main():
    
    n = int(input())
    an = list(map(int, input().split()))
    
    nd_count = 0
    nd_set = {0}

    if len(an) == 1:
        nd_set |= {1}
    else:
        for i in range(len(an)-1):
            if an[i] <= an[i + 1]:
                if nd_count == 0:
                    nd_count += 2
                else:
                    nd_count +=1
            else:
                nd_set |= {nd_count}
                nd_count = 0    
        else:
            if nd_count == 0:
                 nd_set |= {1}
            else:
                nd_set |= {nd_count}
                
    print(max(nd_set))

if __name__ == '__main__':
    main()