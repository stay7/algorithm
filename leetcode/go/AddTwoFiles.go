package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	l1 := ListNode{2, &ListNode{4, &ListNode{9, nil}}}
	l2 := ListNode{5, &ListNode{6, &ListNode{4, &ListNode{9, nil}}}}
	result := addTwoNumbers(&l1, &l2)

	for result != nil {
		println(result.Val)
		result = result.Next
	}
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	head := &ListNode{0, nil}
	cur := head
	var sum int = 0

	for l1 != nil || l2 != nil {
		if l1 != nil {
			sum += l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			sum += l2.Val
			l2 = l2.Next
		}

		cur.Next = &ListNode{sum % 10, nil}
		cur = cur.Next
		if sum >= 10 {
			sum = 1
		} else {
			sum = 0
		}
	}
	if sum == 1 {
		cur.Next = &ListNode{1, nil}
	}
	return head.Next
}
