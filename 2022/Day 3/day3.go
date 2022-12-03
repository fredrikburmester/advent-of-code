// Only part one for now.

package main

import (
	"bufio"
	"fmt"
	"os"
	"time"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func get_value(l string) int {
	letters := "abcdefghijklmnopqrstuvwxyz"
	capital_letters := "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

	for j := 0; j < len(letters); j++ {
		if l == string(letters[j]) {
			return j + 1
		}
	}
	for j := 0; j < len(capital_letters); j++ {
		if l == string(capital_letters[j]) {
			return j + 27
		}
	}
	return 0
}

func part1(input_file []string) int {
	total := 0

	for i := 0; i < len(input_file); i++ {
		line := input_file[i]
		length := len(line)

		first_half := line[0 : length/2]
		second_half := line[length/2 : length]

		match := ""

		for j := 0; j < len(first_half); j++ {
			for k := 0; k < len(second_half); k++ {
				if first_half[j] == second_half[k] {
					match = string(first_half[j])
					break
				}
			}
		}

		total += get_value(match)
	}

	return total
}

func part2(input_file []string) int {
	return 0
}

func main() {
	f, err := os.Open("./input.txt")
	check(err)

	fileScanner := bufio.NewScanner(f)
	fileScanner.Split(bufio.ScanLines)
	array_of_strings := []string{}

	for fileScanner.Scan() {
		array_of_strings = append(array_of_strings, fileScanner.Text())
	}
	start := time.Now()
	fmt.Println(part1(array_of_strings))
	elapsed := time.Since(start)

	fmt.Printf("Part 1 took %s \n", elapsed)

	start = time.Now()
	fmt.Println(part2(array_of_strings))
	elapsed = time.Since(start)

	fmt.Printf("Part 2 took %s \n", elapsed)

	f.Close()
}
