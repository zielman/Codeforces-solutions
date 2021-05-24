import requests, json

username = 'zielman' # Codeforces username
req = requests.get(f"https://codeforces.com/api/user.status?handle={username}&from=1").json()

if req['status'] != 'OK':
    print('Server not responding')
else:
    data = req['result']
    '''
    # make dump
    with open(f"{username}_status.json", 'w') as user_status:
        json.dump(data, user_status, indent= 4)
    '''
    # set of solved contest problems
    contest = set([f"{item['problem']['index']}{item['contestId']}" for item in data if 'contestId' in item.keys() and item['verdict'] == 'OK'])
    
    # set of solved acms problems
    acms = set([f"{item['problem']['index']}" for item in data if 'problemsetName' in item['problem'].keys() and item['verdict'] == 'OK'])

    # problems per index
    d = {'acms': len(acms)}
    for item in contest:
        if item[0] not in d:
            d[item[0]] = 1
        else:
            d[item[0]] += 1
    d = dict(sorted(d.items()))

    # output for README.md
    print(f"Solved per index:")
    for key in d.keys():
        print(f"{key}: {d[key]}")
    print(f"Total problems solved: {len(contest)+len(acms)}")