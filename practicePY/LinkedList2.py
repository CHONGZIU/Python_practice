class ListNode_2:
    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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

def remove(a):
    current = a  # 현재값를 a로 초기화
    head = current
    while current and current.next:  # 현재 값와 다음 값이 모두 존재하는 경우
        if current.val == current.next.val:  # 현재 노드와 다음 노드의 값이 같으면 중복
            current.next = current.next.next  # 중복 제거
        else:
            current = current.next  # 중복이 없는 경우 현재값을 다음값으로 설정
    return head

def minus(a):
    current = ListNode_2() 
    head = current 
    num = None
    while a: 
        if num != a.val:
            current.next = a
            current = current.next
        num = a.val
        a = a.next
    current.next = None
    return head.next

if __name__ == "__main__":
    main()
    
# num이 필요한지, 다른 값이 필요하다.
''' num을 사용했던 이유가 뭐지? '''
''' num을 current는 결국 마지막에 넣은 숫자를 의미할꺼고 그 들어온
숫자들의 첫번째를 지칭 하는 head의 다음부터 지칭을 하면 된다.'''
''' 각자의 역할이 있으니까 처음에 0으로 초기화 하고 그 0과 a를 
비교할 수 있으면서, 해당 숫자를 a로 바꿔줄 변수가 필요했어서'''