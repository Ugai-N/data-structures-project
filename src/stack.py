class Node:
    """Класс для узла стека"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node

    @classmethod
    def overlap(cls, data, next_node):
        return cls(data, next_node)


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""
        self.stack_list = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека

        :param data: данные, которые будут добавлены на вершину стека
        """
        if len(self.stack_list) == 0:
            data = Node.overlap(data, None)
        else:
            data = Node.overlap(data, self.stack_list[-1])
        self.stack_list.append(data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """
        if len(self.stack_list) == 0:
            return None
        removed = self.stack_list.pop()
        return removed

    @property
    def top(self):
        if len(self.stack_list) == 0:
            return None
        else:
            return self.stack_list[-1]
