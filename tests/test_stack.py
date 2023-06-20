"""Здесь надо написать тесты с использованием unittest для модуля stack."""
import unittest

from src.stack import Node, Stack

n1 = Node(5, None)
n2 = Node('a', n1)
test_stack = Stack()


class TestAll(unittest.TestCase):
    def test_node_init(self):
        self.assertEqual(n1.data, 5)
        self.assertEqual(n2.data, 'a')
        self.assertEqual(n1, n2.next_node)

    def test_overlap(self):
        n3 = Node.overlap('b', n2)
        self.assertEqual(n3.data, 'b')
        self.assertEqual(n3.next_node, n2)

    def test_stack_init(self):
        self.assertEqual(test_stack.stack_list, [])

    def test_stack_push(self):
        test_stack.push('dataA')
        self.assertEqual(len(test_stack.stack_list), 1)
        self.assertEqual(test_stack.stack_list[0].data, 'dataA')
        self.assertEqual(test_stack.stack_list[0].next_node, None)

        test_stack.push('dataB')
        self.assertEqual(len(test_stack.stack_list), 2)
        self.assertEqual(test_stack.stack_list[-1].data, 'dataB')
        self.assertEqual(test_stack.stack_list[-1].next_node.data, 'dataA')

        with self.assertRaises(AttributeError):
            test_stack.stack_list[-1].next_node.next_node.data

    def test_pop(self):
        self.assertEqual(test_stack.pop(), None)

        test_stack.push('dataC')
        self.assertEqual(test_stack.pop().data, 'dataC')
        self.assertEqual(test_stack.stack_list, [])

    def test_top(self):
        self.assertEqual(test_stack.top, None)

        test_stack.push('dataD')
        test_stack.push('dataE')
        test_stack.push('dataF')
        self.assertEqual(test_stack.top.data, 'dataF')
        self.assertEqual(test_stack.top.next_node.data, 'dataE')
        self.assertEqual(test_stack.top.next_node.next_node.next_node, None)

        with self.assertRaises(AttributeError):
            test_stack.top.next_node.next_node.next_node.data
