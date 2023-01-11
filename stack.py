class Stack:

    def __init__(self):
        self.sequence = []

    '''проверка стека на пустоту. Метод возвращает True или False'''
    def is_empty(self):
        if self.sequence:
            return False
        else:
            return True

    ''''добавляет новый элемент на вершину стека. Метод ничего не возвращает'''
    def push(self, element):
        self.sequence.insert(0, element)

    '''удаляет верхний элемент стека, стек изменяется'''
    def pop(self):
        return self.sequence.pop(0)

    '''возвращает верхний элемент стека, но не удаляет его. стек не изменяется'''
    def peek(self):
        return self.sequence[0]

    '''возвращает количество элементов в стеке'''
    def size(self):
        return len(self.sequence)
