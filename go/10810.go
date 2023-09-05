package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var N, M int
	fmt.Scanln(&N, &M)

	buckets := make([]int, N)

	for i := 0; i < M; i++ {
		var i, j, k int
		fmt.Scanln(&i, &j, &k)
		for i <= j {
			buckets[i-1] = k
			i += 1
		}
	}

	buffer := make([]string, N)
	for i, bucket := range buckets {
		buffer[i] = strconv.Itoa(bucket)
	}

	fmt.Println(strings.Join(buffer, " "))
}
