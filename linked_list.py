class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
    self.prev = None

class DoublyLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None

  def add_to_front(self, value):
    new_node = Node(value)
    new_node.next = self.head
    if self.head:
      self.head.prev = new_node
    else:
      self.tail = new_node
    self.head = new_node

  def add_to_end(self, value):
    new_node = Node(value)
    new_node.prev = self.tail
    if self.tail:
      self.tail.next = new_node
    else:
      self.head = new_node
    self.tail = new_node

  def remove_from_front(self):
    if not self.head:
      return None
    removed_value = self.head.data

    self.head = self.head.next
    if self.head:
      self.head.prev = None
    else:
      self.tail = None
    return removed_value

  def remove_from_end(self):
    if not self.tail:
      return None
    removed_value = self.tail.data

    self.tail = self.tail.prev
    if self.tail:
      self.tail.next = None
    else:
      self.head = None
    return removed_value

  def display_forward(self):
    current = self.head
    elements = []
    while current:
      elements.append(current.data)
      current = current.next
    return elements

  def display_backward(self):
    current = self.tail
    elements = []
    while current:
      elements.append(current.data)
      current = current.prev
    return elements

dll = DoublyLinkedList()
dll.add_to_end(10)
dll.add_to_end(20)
dll.add_to_front(5)
print(dll.display_forward())   # Output: [5, 10, 20]
print(dll.display_backward())  # Output: [20, 10, 5]

dll.remove_from_front()
print(dll.display_forward())   # Output: [10, 20]
dll.remove_from_end()
print(dll.display_forward())   # Output: [10]


#leetcode 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        new_list = None

        while head:
          next_node = head.next
          head.next = new_list
          new_list = head
          head = next_node
        return new_list

# Example usage:
# head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
# solution = Solution()
# reversed_head = solution.reverseList(head)
# # The reversed linked list is now 5 -> 4 -> 3 -> 2 -> 1

# leetcode 876. Middle of the Linked List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

# leetcode 141. Linked List Cycle
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      slow = head
      fast = head

      while fast and fast.next:
          slow = slow.next
          fast = fast.next.next

          if slow == fast:
              return True
      return False

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
      curr = head
      nodes_seen = set()

      while curr:
          if curr in nodes_seen:
              return True
          nodes_seen.add(curr)
          curr = curr.next
      return False


# leetcode. 21 Merge Two Sorted Lists
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
      dummy = ListNode()
      tail = dummy

      while list1 and list2:
          if list1.val < list2.val:
              tail.next = list1
              list1 = list1.next
          else:
              tail.next = list2
              list2 = list2.next
          tail = tail.next

      if list1:
          tail.next = list1
      elif list2:
          tail.next = list2

      return dummy.next