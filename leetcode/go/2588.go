package main

import "fmt"

func main() {

	var firstNum, secondNum int
	fmt.Scanln(&firstNum)
	fmt.Scanln(&secondNum)

	fmt.Println(firstNum * (secondNum % 10))
	fmt.Println(firstNum * (secondNum % 100 / 10))
	fmt.Println(firstNum * (secondNum % 1000 / 100))
	fmt.Println(firstNum * secondNum)
}