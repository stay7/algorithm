package main

import "fmt"

func main() {
	var hour, minutes int
	fmt.Scanf("%d %d", &hour, &minutes)

	var minusHour bool = minutes < 45
	if minusHour {
		minutes += 60
		if hour == 0 {
			hour = 23
		} else {
			hour -= 1
		}
	}
	fmt.Println(hour, minutes-45)
}
