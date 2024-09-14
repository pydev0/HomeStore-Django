class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)

        if not self.head:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def display(self):
        current_node = self.head

        while current_node:
            print(current_node.data, end="<->")
            current_node = current_node.next
        print("None")


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.display()  # Вывод: 1 -> 2 -> 3 -> None
