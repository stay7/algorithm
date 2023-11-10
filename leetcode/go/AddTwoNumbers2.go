package main

import "strconv"

type ListNode struct {
	Val  int
	Next *ListNode
}

func main() {
	l1 := ListNode{7, &ListNode{2, &ListNode{4, &ListNode{3, nil}}}}
	l2 := ListNode{5, &ListNode{6, &ListNode{4, nil}}}

	addTwoNumbers(&l1, &l2)
}

func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	var num1, num2 []int

	for l1 != nil {
		num1 = append(num1, l1.Val)
		l1 = l1.Next
	}

	for l2 != nil {
		num2 = append(num2, l2.Val)
		l2 = l2.Next
	}

	sum, digit := 0, 1
	var i, j = len(num1) - 1, len(num2) - 1
	for i >= 0 || j >= 0 {
		if i >= 0 {
			sum += num1[i] * digit
			i -= 1
		}

		if j >= 0 {
			sum += num2[j] * digit
			j -= 1
		}
		digit *= 10
	}
	sumStr := strconv.Itoa(sum)
	head := &ListNode{0, nil}
	cur := head
	for _, char := range sumStr {
		cur.Next = &ListNode{int(char - '0'), nil}
		cur = cur.Next
	}
	return head.Next
}
