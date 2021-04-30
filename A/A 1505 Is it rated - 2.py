# https://codeforces.com/problemset/problem/1505/A

def main():
    
    while True:
        try:
            if input() == 'Is it rated?':
                print('NO')
        except EOFError:
            break
      
if __name__ == '__main__':
    main()