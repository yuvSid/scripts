
import json
import re

# Opening JSON file
f = open('/Users/yurasidorov/Repos/scripts/python/result.json')

# Search regex pattern
message_pattern = re.compile(r'Wordle.*?([X,\d])\/([\d])')
  
# returns JSON object as 
# a dictionary
rawData = json.load(f)
  
# Iterating through the json
# list

data = {}
for i in rawData['messages']:
    if i['type'] != "message":
        continue

    user = i['from_id']
    if user not in data:
        data[user] = [0, 0, i['from'], 0, 0]

    if not i['text_entities']:
        continue

    string = i['text_entities'][0]['text']
    res = message_pattern.match(string)

    if not res:
        continue
    
    tries = int(res[1]) if res[1] != 'X' else 7
    data[user][3] = data[user][3] + 1
    data[user][4] = data[user][4] + tries
    
    if res[1] != 'X':
        data[user][0] = data[user][0] + 1
        data[user][1] = data[user][1] + tries

max_solved = 0
solvers = []
for item in data.items():
    if item[1][0] > max_solved:
        max_solved = item[1][0]
        solvers = []
    if item[1][0] == max_solved:
        solvers.append(item[1][2])

print("Without lost count:")
res = []
for item in data.items():
    user = item[1]
    res.append({"res" : user[1]/user[0], "name" : user[2], "solved" : user[0]})
res.sort(key=lambda x: x["res"])
for each in res:
    print(f'{each["name"]:10} ==> average: {each["res"]:.4f} ==> solved: {each["solved"]}')

# res = []
# print("\nWith lost as 7 tries:")
# for item in data.items():
#     user = item[1] 
#     res.append({"res" : user[4]/user[3], "name" : user[2], "solved" : user[3]})
# res.sort(key=lambda x: x["res"])
# for each in res:
#     print(f'{each["name"]:10} ==> average: {each["res"]:.4f} ==> solved: {each["solved"]}')

res = []
print(f'\nWith unsolved for all days as 7 tries. Maximum solved {max_solved} by {", ".join(solvers)}:')
for item in data.items():
    user = item[1]
    res.append({"res" : (user[1] + 7 * (max_solved - user[0]))/max_solved, "name" : user[2]})
res.sort(key=lambda x: x["res"])
for each in res:
    print(f'{each["name"]:10} ==> average: {each["res"]:.4f}')
  
# Closing file
f.close()