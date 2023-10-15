package main

func main() {
	var nums1 = []int{1, 2, 3, 1, 1, 3}
	var nums2 = []int{1, 1, 1, 1}
	var nums3 = []int{1, 2, 3}

	println(numIdenticalPairs(nums1))
	println(numIdenticalPairs(nums2))
	println(numIdenticalPairs(nums3))
}

func numIdenticalPairs(nums []int) int {
	dict := make(map[int][]int)
	result := 0

	for index, element := range nums {
		value, exist := dict[element]
		if exist {
			dict[element] = append(value, index)
		} else {
			dict[element] = []int{index}
		}
	}

	for _, element := range dict {
		result += combination2(len(element))
	}
	return result
}

func combination2(n int) int {
	if n < 2 {
		return 0
	}
	return n * (n - 1) / 2
}
