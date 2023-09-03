package main

import (
	"fmt"
	"strings"
)

func main() {
	var N int

	fmt.Scanln(&N)
	array := make([]string, N/4)

	for i := 0; i < N/4; i++ {
		array[i] = "long"
	}

	fmt.Println(strings.Join(array, " ") + " int")
}
