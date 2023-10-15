package main

import (
	"fmt"
	"strconv"
	"strings"
)

func main() {
	var N, M int
	fmt.Scanln(&N, &M)

	buckets := make([]string, N)
	for i := 0; i < N; i++ {
		buckets[i] = strconv.Itoa(i + 1)
	}

	for i := 0; i < M; i++ {
		var a, b int
		fmt.Scanln(&a, &b)
		buckets[a-1], buckets[b-1] = buckets[b-1], buckets[a-1]
	}

	fmt.Println(strings.Join(buckets, " "))
}
