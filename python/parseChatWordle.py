
import json
  
# Opening JSON file
f = open('/Users/yurasidorov/Repos/scripts/python/result.json')
  
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
        data[user] = [0, 0, i['from']]

    if not i['text_entities']:
        continue

    string = i['text_entities'][0]['text']
    words = string.split()

    if words[0] != "Wordle" or words[2][0] == 'X':
        continue

    data[user][0] = data[user][0] + 1
    data[user][1] = data[user][1] + int(words[2][0])

for item in data.items():
    user = item[1]
    res = user[1]/user[0]
    print(f'{user[2]:10} ==> median: {res:.4f} ==> solved: {user[0]}')
  
# Closing file
f.close()