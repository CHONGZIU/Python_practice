class ListNode:

    def __init__(self, val=0, daum=None): # 클래스의 초기화를 위한 메소드
        self.val = val
        self.daum = daum


def solution(a, b): # a, b solution이라는 함수에 들어갈 변수
    current = ListNode() # head와 current는 ListNode의 인스턴스
    head = current
    while a and b:  # a와 b가 True인 동안 = a와 b가 모두 값이 있는 동안
        if a.val < b.val : # .val의 이유: 노드의 주소를 사용해야해서
            current.daum = a
            a = a.daum
        else:
            current.daum = b
            b = b.daum
        current = current.daum
    current.daum = a or b  # 마지막은 a or b 둘중 남아있는 값
    return head.daum # head의 다음 값들이 줄줄이 나옴 
''' head가 맨처음 수 아니었나..? 근데 이렇게 쓰면 어떻게 다음수가 나오지? '''

def print_linked_list(list):
    item = list
    while item:
        print(item.val, end=' ')
        item = item.daum


def main():
    a = ListNode(1)
    a.daum = ListNode(2)
    a.daum.daum = ListNode(4)

    b = ListNode(1)
    b.daum = ListNode(3)
    b.daum.daum = ListNode(4)
    
    print_linked_list(solution(a, b))

if __name__ == "__main__":
    main()


# root = ListNode(3)      #[0]
# root.next = ListNode(6) #[1]

# new_item = ListNode(4)
# root.next = new_item

# root.next.next.next.next
