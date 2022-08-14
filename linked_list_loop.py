class Node:                        # Node defining class

    def __init__(self, val):       # Function creating node
        self.val = val
        self.next = None


class LinkedList:                  # Linked list (LL) defining class
    def __init__(self):            # Function to initialize the head of the LL
        self.head = None

    def AddNode(self, val):        # Function to insert a new node to the end
        if self.head is None:
            self.head = Node(val)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = Node(val)

    def CreateLoop(self, n):          # Function to create a loop connecting the last node to n'th node (1st node = '1')
        LoopNode = self.head          # Loop node is the connecting node to the last node of LL
        for _ in range(1, n):
            LoopNode = LoopNode.next

        end = self.head               # end node is the last node of the LL
        while end.next:
            end = end.next
        end.next = LoopNode           # Creating the loop

    def detectLoop(self):             # Function to detect the loop and return the length of the loop
        if self.head is None:         # If the LL is empty
            return 0

        slow = self.head              # Using Floyd's Cycle-Finding algorithm / Slow-Fast Pointer Method
        fast = self.head
        flag = 0                      # To show that both slow and fast are at the start of the LL

        while slow and slow.next and fast and fast.next and fast.next.next:
            if slow == fast and flag != 0:       # Means loop is confirmed in the LL
                count = 1                        # Now Slow and Fast are both at the same node which is part of the LL
                slow = slow.next
                while slow != fast:
                    slow = slow.next
                    count += 1
                return count

            slow = slow.next
            fast = fast.next.next
            flag = 1
        return 0                  # No loop


myLL = LinkedList()     # Setting up the code making a LL and adding the nodes

myLL.AddNode(1)
myLL.AddNode(2)
myLL.AddNode(3)
myLL.AddNode(4)
myLL.AddNode(5)

myLL.CreateLoop(3)     # Creating a loop in the LL

looplength = myLL.detectLoop()
if myLL.head is None:
    print("Linked List is empty")
else:
    print(str(looplength))
