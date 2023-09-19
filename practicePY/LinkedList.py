class ListNode:

    def __init__(self, val=0, next=None): # 클래스의 초기화를 위한 메소드
        self.val = val
        self.next = next

def solution(a, b): # a, b solution이라는 함수에 들어갈 변수
    current = ListNode() # head와 current는 ListNode의 인스턴스
    head = current
    while a and b:  # a와 b가 True인 동안 = a와 b가 모두 값이 있는 동안
        if a.val < b.val : # a라는 인스턴스 안에 val라는 속성
            current.next = a #  
            a = a.next # 이게 있기때문에 a자체가 a의 다음 값을 지칭
        else:
            current.next = b 
            b = b.next
        current = current.next
    current.next = a or b  # 마지막은 a or b 둘중 남아있는 값
    return head.next # head의 다음 값들이 줄줄이 나옴 

def print_linked_list(list):
    item = list
    while item:
        print(item.val, end=' ')
        item = item.next


def main():
    a = ListNode(1) # a는 인스턴스
    a.next = ListNode(2)
    a.next.next = ListNode(4)

    b = ListNode(1) # b는 인스턴스
    b.next = ListNode(3)
    b.next.next = ListNode(4)
    
    print_linked_list(solution(a, b))

if __name__ == "__main__":
    main()


# root = ListNode(3)      #[0]
# root.next = ListNode(6) #[1]

# new_item = ListNode(4)
# root.next = new_item

# root.next.next.next.next
