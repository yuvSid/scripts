
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
        data[user] = [0, 0, i['from'], 0, 0]

    if not i['text_entities']:
        continue

    string = i['text_entities'][0]['text']
    words = string.split()

    resultInStr = str(words[2] if len(words) > 2 else '')
    if words[0] != "Wordle" or not (resultInStr[0].isdigit() or words[2][0] == 'X'):
        continue
    
    tries = int(words[2][0]) if words[2][0] != 'X' else 7
    data[user][3] = data[user][3] + 1
    data[user][4] = data[user][4] + tries
    
    if words[2][0] != 'X':
        data[user][0] = data[user][0] + 1
        data[user][1] = data[user][1] + tries

print("Without lost as 7 tries:")
for item in data.items():
    user = item[1]
    res = user[1]/user[0]
    print(f'{user[2]:10} ==> median: {res:.4f} ==> solved: {user[0]}')

print("\nWith lost as 7 tries:")
for item in data.items():
    user = item[1]
    res = user[4]/user[3]
    print(f'{user[2]:10} ==> median: {res:.4f} ==> solved: {user[3]}')
  
# Closing file
f.close()