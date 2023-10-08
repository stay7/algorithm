package main

type ListNode struct {
	Val  int
	Next *ListNode
}

var tail *ListNode

func main() {
	head := ListNode{1, &ListNode{2, &ListNode{3, &ListNode{4, &ListNode{5, nil}}}}}
	printNode(reverse(&head))
}

// iterative
func reverseList(head *ListNode) *ListNode {
	if head == nil || head.Next == nil {
		return head
	}

	prev := head
	cur := head.Next
	prev.Next = nil

	for cur != nil {
		next := cur.Next
		cur.Next = prev
		prev = cur
		cur = next
	}
	return prev
}

// recursive
func reverse(node *ListNode) *ListNode {
	if node == nil || node.Next == nil {
		return node
	}

	head := reverse(node.Next)
	node.Next.Next = node
	node.Next = nil
	return head
}

func printNode(head *ListNode) {
	if head == nil {
		return
	}
	println(head.Val)
	printNode(head.Next)
}
