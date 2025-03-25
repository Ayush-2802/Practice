class node:
    def __init__(self,data):
        self.data = data
        self.next = None

def traverselistIterative(head):
    while head is not None:
        print(head.data,end=" ")
        head = head.next
    print()

def traverseListRecursive(head):
    if head is None:
        print()
        return
    print(head.data,end = " ")
    traverseListRecursive(head.next)


def main():
    head = node(10)
    head.next = node(20)
    head.next.next = node(30)
    head.next.next.next = node(40)

    # traverselistIterative(head)
    traverseListRecursive(head)

if __name__ == "__main__":
    main()