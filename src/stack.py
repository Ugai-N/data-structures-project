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
    def assigning(cls, data, next_node):
        """Класс-метод для присвоения узлам стека атрибутов класса Node"""

        return cls(data, next_node)


class Stack:
    """Класс для стека"""

    def __init__(self):
        """Конструктор класса Stack"""

        self.stack_list = []

    def push(self, data):
        """
        Метод для добавления элемента на вершину стека и присвоения аттрибутов Node

        :param data: данные, которые будут добавлены на вершину стека
        """

        if len(self.stack_list) == 0:
            data = Node.assigning(data, None)
        else:
            data = Node.assigning(data, self.stack_list[-1])
        self.stack_list.append(data)

    def pop(self):
        """
        Метод для удаления элемента с вершины стека и его возвращения

        :return: данные удаленного элемента
        """

        if len(self.stack_list) == 0:
            return None
        removed = self.stack_list.pop().data
        return removed

    @property
    def top(self):
        """Метод-аттрибут, взвращает узел на вершине стека"""

        if len(self.stack_list) == 0:
            return None
        else:
            return self.stack_list[-1]
