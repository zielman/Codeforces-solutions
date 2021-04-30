# https://codeforces.com/problemset/problem/266/B

n, t = map(int, input().split()) # number of children in the queue and the time
s = input() #  the schoolchildren's initial arrangement

queues = [s]

for i in range(t):
    queues.append(queues[i].replace('BG','GB'))

print(queues[-1])