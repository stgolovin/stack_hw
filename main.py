from constants import *
from stack import Stack


def checker(symbol_string: list):
    s1 = Stack()
    s2 = Stack()
    s3 = Stack()
    balanced = True
    index = 0
    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol == '(':
            s1.push(symbol)
        elif symbol == ')':
            if s1.is_empty():
                balanced = False
            else:
                s1.pop()
        if symbol == '[':
            s2.push(symbol)
        elif symbol == ']':
            if s2.is_empty():
                balanced = False
            else:
                s2.pop()
        if symbol == '{':
            s3.push(symbol)
        elif symbol == '}':
            if s3.is_empty():
                balanced = False
            else:
                s3.pop()
        index += 1
    if balanced and s1.is_empty() and s2.is_empty() and s3.is_empty():
        return f'Cбалансированно'
    else:
        return f'Несбалансированно'


if __name__ == '__main__':
    print(checker(get_str_item(STR_1)))
    print(checker(get_str_item(STR_2)))
    print(checker(get_str_item(STR_3)))
    print('-'*18)
    print(checker(get_str_item(STR_4)))
    print(checker(get_str_item(STR_5)))
    print(checker(get_str_item(STR_6)))
