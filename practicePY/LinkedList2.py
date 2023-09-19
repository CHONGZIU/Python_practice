class ListNode_2:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def minus(a):
    current = ListNode_2()  # val == 0
    head = current  # head = 0
    num = None
    while a: 
        if num != a.val:
            current.next = a
            current = current.next
        num = a.val
        a = a.next
    return head.next


def print_linked_list(list):
    item = list
    while item:
        print(item.val, end=' ')
        item = item.next

def main():
    a = ListNode_2(1)
    a.next = ListNode_2(1)
    a.next.next = ListNode_2(2)
    a.next.next.next = ListNode_2(3)
    a.next.next.next.next = ListNode_2(3)
    
    print_linked_list(minus(a))

if __name__ == "__main__":
    main()