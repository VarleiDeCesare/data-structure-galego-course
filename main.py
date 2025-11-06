#leetcode 557. Reverse Words in a String III
class Solution:
  def reverseWords_manual(s):
    res = ''
    l, r = 0, 0

    while r < len(s):
      if s[r] != ' ':
        r += 1
      else:
        print('---' + s[l:r+1])
        res += s[l:r+1][::-1]
        r += 1
        l = r
    res += ' '
    res += s[l:r + 2][::-1]
    return res[1:]

# Solution.reverseWords_manual("Let's take LeetCode contest")


def binary_search(array, target, left=0, right=None):
  if right is None:
    right = len(array)
  steps = 0
  while left < right:
    steps += 1
    middle = (left + right) // 2
    if array[middle] == target:
      print(f"steps: {steps}")
      return middle
    elif array[middle] < target:
      left = middle + 1
    else:
      right = middle - 1
  return -1

a = [1,2,3,4,5,6,7,8,9,10]
b = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
# binary_search(b, 11)

#Sliding Window
#LeetCode 3090 - Maximum Lenght Substring With two Occurences.

def maximumLengthSubstring(s):
  l = 0
  r = 0
  _max = 1
  counter = {}
  counter[s[0]] = 1

  while (r < len(s) -1):
    r+=1
    if counter.get(s[r]):
      counter[s[r]] += 1
    else:
      counter[s[r]] = 1

    while counter[s[r]] == 3:
      l += 1
      counter[s[l]] -= 1

    _max = max(_max, (r-l) + 1)
  return _max

# print(maximumLengthSubstring("aadaad"))

#exponential search - Complexidade temporal O(log n) / temporal O(1)

def exponential_search(arr, target):
  if arr[0] == target:
    return 0

  n = len(arr)
  i = 1

  while i < n and arr[i] < target:
    i *= 2

  if arr[i] == target:
    return i

  return binary_search(arr, target, left=i//2, right=min(i, n - 1))

arr = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
# print(exponential_search(arr, 32))


#leetcode 387. First Unique Character in a String
def firstUniqueCharacter(s):
  d = {}
  for idx, char in enumerate(s):
    if not d.get(char):
      d[char] = [idx, 1]
    else:
      d[char][1] += 1

  for ch, val in d.items():
    if val[1] == 1:
      return val[0]
  return -1

# firstUniqueCharacter("leetcode")


#leetcode. 219. Contains Duplicate II

def containsNearbyDuplicate(nums, k):
  d = {}
  result = False
  for idx, n in enumerate(nums):
    number = nums[idx]
    if d.get(number) != None and abs(d.get(number) - idx) <= k:
        result = True
        break
    d[number] = idx
  return result

# print(containsNearbyDuplicate([1,2,3,1], 3))


def twoSum(nums, target):
  d = {}
  for i, num in enumerate(nums):
    diff = target - num
    if d.get(diff) != None:
      return [d.get(diff), i]
    d[num] = i

# print(twoSum([2,7,11,15], 9));


#leetcode 148. Sort List
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
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
                    l2.next = l2
                tail = tail.next
            tail.next = l1 or l2
            return head.next

        def mergeSort(head):
            if not head and head.next:
                return head

            middle = findMiddle(head)
            after_middle = middle.next
            middle.next = None

            left = mergeSort(head)
            right = mergeSort(after_middle)

            return mergeTwoLists(left, right)
        def buildLinkedList(values):
            if not values:
                return None
            head = ListNode(values[0])
            current = head
            for val in values[1:]:
                current.next = ListNode(val, None)
                current = current.next
            return head

        headBuilded = buildLinkedList(head)
        return mergeSort(headBuilded)

solution = Solution()
sorted_list = solution.sortList([-1,5,3,4,0])
print(sorted_list)