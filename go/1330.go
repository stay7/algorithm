package main

import "fmt"

func main() {
	var a, b int
	fmt.Scanf("%d %d", &a, &b)

	switch {
	case a < b:
		fmt.Println("<")
	case a > b:
		fmt.Println(">")
	default:
		fmt.Println("==")
	}
}
