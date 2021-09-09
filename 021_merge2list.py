class ListNode:
    def __init__(self, val=0, next=None):
       
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        
   
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
                p = p.next
      
            else:
                p.next = l2
                l2 = l2.next
                p = p.next
        if l1:
            p.next = l1
        if l2:
            p.next = l2
 

        res = []
        while head.next:
            res.append(head.val)
            head = head.next
        
        return res

p1_3 = ListNode(4)
p1_2 = ListNode(2, p1_3)
p1_1 = ListNode(1, p1_2)


p2_3 = ListNode(4)
p2_2 = ListNode(3, p2_3)
p2_1 = ListNode(1, p2_2)

print(Solution().mergeTwoLists(p1_1, p2_1))























def mergeTwoLists_diy(l1, l2):
   
    n = len(l2)
    res = l1
    for j in range (0, n):
        m = len(res)
        for i in range (0, m - 1):
            if l2[j] > res[i] and l2[j] <= res[i + 1]:
                res.insert(i + 1, l2[j])
        
    return res