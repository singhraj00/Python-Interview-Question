# Maximum Subarray Sum
def max_subarray(arr):
    max_sum = arr[0]
    curr_sum = 0

    for num in arr:
        curr_sum += num
        if curr_sum > max_sum:
            max_sum = curr_sum
        if curr_sum < 0:
            curr_sum = 0
    return max_sum


#  Cycle Detection in a Singly Linked List
class NodeList:
    def __init__(self, val=0):
        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # insert node at end
    def insert(self, val):
        new_node = NodeList(val)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def createcycle(self, pos):
        if pos < 0:
            return
        cycle_node = None
        temp = self.head
        idx = 0
        last = None

        while temp:
            if idx == pos:
                cycle_node = temp
            last = temp
            temp = temp.next
            idx += 1
        if last:
            last.next = cycle_node

    # detect cycle
    def hascycle(self):
        slow = fast = self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False


# Maximum Product Subarray
def maxProduct(arr):
    curr_max = curr_min = ans = arr[0]

    for i in range(1, len(arr)):
        x = arr[i]

        temp_max = max(x, curr_max * x, curr_min * x)
        temp_min = min(x, curr_max * x, curr_min * x)

        curr_max = temp_max
        curr_min = temp_min

        ans = max(ans, curr_max)

    return curr_max


print(max_subarray([1, 2, 7, -4, 3, 2, -10, 9, 1]))
print(maxProduct([-3, 4, 5]))

l1 = LinkedList()
l1.insert(1)
l1.insert(2)
l1.insert(3)
l1.insert(4)
l1.createcycle(3)
print(l1.hascycle())
