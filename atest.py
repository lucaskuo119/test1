N = int(input())
yesterday = input()
today = input()



sameparck = 0
for parck in range(len(today)):
    if yesterday[parck] == today[parck] == 'C':
        sameparck = sameparck + 1
    
print(sameparck)