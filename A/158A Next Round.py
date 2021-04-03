#https://codeforces.com/problemset/problem/158/A

def main():
    
    n, k = map(int, input().split())
    scores = list(map(int, input().split()))
   
    pwa = 0 # participants who advance

    if scores[0] != 0:
        for score in scores:
            if score >= scores[k - 1] and score != 0:
                pwa += 1
                
    print(pwa)

if __name__ == '__main__':
    main()