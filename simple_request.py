import requests





token = '242338579:AAGYuS-JD3pBvEauocbIAO7BRUlCFjFcbjY/'
request_url = 'https://api.telegram.org/bot'
r = requests.get(request_url+token+'getupdates')
result = r.json()
for i in result:
    print(i,'-', result[i], '\n')
res = result['result'][-1]
for i in res:
    print(i,'-', res[i], '\n')
if result['ok']:
    result = result['result'][-1]
    update_id = result['update_id']
    with open('updates.txt', 'r') as read_file:
        lines = [line.strip() for line in read_file.readlines()]
        print(lines)
        if str(update_id) not in lines:
            print(result)
            message = result['message']
            chat = message['chat']
            chat_id = chat['id']
            name = message['from']['first_name'] + ' ' +  message['from']['last_name']
            print(chat_id, name)
            s = requests.get(request_url + token + 'sendmessage?'+'chat_id=' + str(chat_id) + '&text='+ 'Hello, ' + name + '!')
            with open('updates.txt', 'a') as append_file:
                append_file.write(str(update_id)+'\n')
        else:
            print('No updates :(')

