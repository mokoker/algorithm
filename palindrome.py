# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head):

        double = head
        slow = head
        while double.next and double.next.next:
            double = double.next.next
            slow = slow.next
        other = self.reverse(slow)

        while other.next:
            if other.val != head.val:
                return False
            other = other.next
            head = head.next
        return True

    def reverse(self, head):
        prev = None
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        return prev

    def GenerateLists(self, array):
        l = ListNode(array[0])
        one = l
        for x in range(1, len(array)):
            one.next = ListNode(array[x])
            one = one.next
        return l


s = Solution()
d = s.GenerateLists([1, 2, 3, 6, 2, 1])
re = s.isPalindrome(d)
print(re)
