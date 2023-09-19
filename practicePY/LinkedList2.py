class ListNode_2:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

def minus(a):
    while True:
        if a.next == None:
            break
        if a.val == a.next :
            return a.val
        else:
            a.next
        a = a.next
        
''' a.next 다음은 a.next.next랑 비교를 해야하는데 그러면 비교를 할 때마다 써줘야... '''
''' 애초에 저 식이 맞기는 한가 '''


def print_linked_list(list):
    item = list
    while item:
        print(item.val, end=' ')
        item = item.daum

def main():
    a = ListNode_2(1)
    a.next = ListNode_2(1)
    a.next.next = ListNode_2(2)
    a.next.next.next = ListNode_2(3)
    a.next.next.next.next = ListNode_2(3)
    
    print_linked_list(minus(a))

if __name__ == "__main__":
    main()