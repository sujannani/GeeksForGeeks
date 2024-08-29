class Solution:
    def countNodesInLoop(self, head):
        if not head or not head.next:
            return 0
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  
                loop_size = 1
                current = slow
                while current.next != slow:
                    current = current.next
                    loop_size += 1
                return loop_size
        return 0