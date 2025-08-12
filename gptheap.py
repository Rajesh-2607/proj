class Queue:
    def __init__(self):
        self.q = []

    def is_empty(self):
        return len(self.q) == 0

    def length(self):
        return len(self.q)

    def right(self, index):
        return index * 2 + 2

    def left(self, index):
        return index * 2 + 1

    def parent(self, index):
        return (index - 1) // 2

    def upheap(self, index):
        parent_index = self.parent(index)
        if index > 0 and self.q[parent_index] < self.q[index]:
            self.q[parent_index], self.q[index] = self.q[index], self.q[parent_index]
            self.upheap(parent_index)

    def add(self, val):
        self.q.append(val)
        self.upheap(self.length() - 1)

    def dis(self):
        print("Queue:", self.q)


# Create queue object outside the loop
q = Queue()

while True:
    print("\nMenu:")
    print("1. Add Item")
    print("4. View Queue")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        p = int(input("Enter the priority key: "))
        q.add(p)
    elif choice == 4:
        q.dis()
    elif choice == 5:
        break
    else:
        print("Invalid choice.")
