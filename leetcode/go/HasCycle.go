package main

type ListNode struct {
	Val  int
	Next *ListNode
}


func hasCycle(head *ListNode) bool {
	var visit = make(map[*ListNode]bool)

	cur := head
	for cur != nil {
		if _, ok := visit[cur]; ok {
			return true
		}

		visit[cur] = true
		cur = cur.Next
	}
	return false
}

func hasCycle(head *ListNode) bool {
	if head == nil || head.Next == nil {
		return false
	}

	slow := head
	fast := head.Next

	for slow != fast {
		if fast == nil || fast.Next == nil {
			return false
		}
		slow = slow.Next
		fast = fast.Next.Next
	}
	return true
}
