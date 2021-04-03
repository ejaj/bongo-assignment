class Node:
    """
    A class to represent a Node.
    """

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent


def lca(node1, node2):
    """
    Check the value of node1 are equal value of the node2, if are equaled, return node1 value
    Store node1 value to a new list and node2 value to an another list
    Check list value each other are existed.

    Worst case time complexity: O(n^2) as while loop takes array of size.
    Best case time complexity: Ω(1) (if array are sorted).
    Space complexity: O(n).

    :param node1:
    :param node2:
    :return:
    """

    if node1.value == node2.value:
        print(node1.value)
        return

    values_node1 = [node1.value]
    values_node2 = [node2.value]
    while True:
        if node1.parent:
            node1 = node1.parent
            if node1.value in values_node2:
                print(node1.value)
                return
            values_node1.append(node1.value)
        if node2.parent:
            node2 = node2.parent
            if node2.value in values_node1:
                print(node2.value)
                return
            values_node2.append(node2.value)
