class ListNode:
    def __init__(self, val=0, next=None):
       
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        hud = 0
        
        # p.next l1.next l2.next
        while l1 and l2:
            
            unt = int((l1.val + l2.val + hud) % 10)
            hud = int((l1.val + l2.val + hud) / 10)
            
            p.next = ListNode(unt)
            p = p.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            unt = int((l1.val + hud) % 10)
            hud = int((l1.val + hud) / 10)        
            p.next = ListNode(unt)
            p = p.next
            l1 = l1.next
        while l2:
            unt = int((l2.val + hud) % 10)
            hud = int((l2.val + hud) / 10)        
            p.next = ListNode(unt)
            p = p.next
            l2 = l2.next
        if hud != 0:
            p.next = ListNode(1)

        res = []
        while head.next:
            res.append(head.val)
            head = head.next
        
        return res

    def addTwoNumbers_demo(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode()
        p = head
        carry = 0
        
        while l1 or l2 or carry:
        
            if l1:
                carry = carry + l1.val      
                l1 = l1.next
            if l2:
                carry = carry + l2.val      
                l2 = l2.next

            p.next = ListNode(int(carry % 10))
            p = p.next
            carry = int(carry / 10)
            
        res = []
        while head.next:
            res.append(head.val)
            head = head.next
        
        return res

#p1_3 = ListNode(3)
#p1_2 = ListNode(4, p1_3)
p1_2 = ListNode(4)
p1_1 = ListNode(2, p1_2)


p2_3 = ListNode(4)
p2_2 = ListNode(6, p2_3)
p2_1 = ListNode(5, p2_2)

p3_1 = ListNode(0)
p3_2 = ListNode(0)

print(Solution().addTwoNumbers_demo(p1_1, p2_1))
print(Solution().addTwoNumbers_demo(p3_1, p3_1))



# print(addTwoNumbers(l1 = [9,9,9,9], l2 = [9]))
# print(addTwoNumbers(l1 = [2,4,3], l2 = [5,6,4]))
# print(addTwoNumbers(l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]))












def addTwoNumbers_list(l1, l2):
    
    n = max(len(l1), len(l2)) + 1
    for i in range(0, n - len(l1)):
        l1.append(0)
    for j in range(0, n - len(l2)):
        l2.append(0)
    res = [0] * n 
    tmp = 0
    #print(l1,l2)
    for k in range(0, n):
  
        res[k] = int((l1[k] + l2[k] + tmp) % 10) 
        
        tmp = int((l1[k] + l2[k] + tmp) / 10)
    if res[-1] == 0:
        res.pop()
    return res

    

