# https://codeforces.com/problemset/problem/1154/A

def main():
    nums = sorted(list(map(int, input().split())))
    
    print(nums[3] - nums[0], nums[3] - nums[1], nums[3] - nums[2])

if __name__ == '__main__':
    main()