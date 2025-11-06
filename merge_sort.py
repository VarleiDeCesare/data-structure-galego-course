class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def findMiddle(head):
    slow = head
    fast = head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def mergeTwoLists(l1, l2):
    head = ListNode()
    tail = head

    while l1 and l2:
        if l1.val < l2.val:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    tail.next = l1 or l2
    return head.next


def mergesort(head):
    if not head or not head.next:
        return head

    middle = findMiddle(head)
    after_middle = middle.next
    middle.next = None

    left = mergesort(head)
    right = mergesort(after_middle)

    return mergeTwoLists(left, right)


def buildLinkedList(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head


def printLinkedList(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    print(result)


values = [4, 2, 1, 3]
print("Unsorted Linked List:", values)
head = buildLinkedList(values)
sorted_head = mergesort(head)
print("Sorted Linked List:", end=" ")
printLinkedList(sorted_head)


