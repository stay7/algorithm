package main

import "fmt"

func main() {
	var expected, N, sum, price, amount int
	fmt.Scanln(&expected)
	fmt.Scanln(&N)

	for i := 0; i < N; i++ {
		fmt.Scanln(&price, &amount)
		sum += price * amount
	}
	if expected == sum {
		fmt.Println("Yes")
	} else {
		fmt.Println("No")
	}
}
