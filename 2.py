from collections import deque


def is_palindrome(dq):
    while len(dq) > 1:
        if dq.popleft() != dq.pop():
            return False
    return True


def prepare_string(string):
    string = string.replace(' ', '')
    string = string.casefold()
    print(string)
    return deque(string)


while True:
    try:
        text = input('Enter a string: ')

        dq = prepare_string(text)

        print(is_palindrome(dq))
    except KeyboardInterrupt:
        break
