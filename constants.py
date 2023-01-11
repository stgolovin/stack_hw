
STR_1 = '(((([{}]))))'
STR_2 = '[([])((([[[]]])))]{()}'
STR_3 = '{{[()]}}'

STR_4 = '}{}'
STR_5 = '{{[(])]}}'
STR_6 = '[[{())}]'


def get_str_item(str_: str):
    list_ = list()
    for item in str_:
        list_.append(item)
    return list_
