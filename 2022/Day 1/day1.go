package main

import (
	"bufio"
	"fmt"
	"os"
	"sort"
	"strconv"
	"time"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func part1(input_file []string) int {
	total := 0
	totals := []int{}
	for i := 0; i < len(input_file); i++ {
		if input_file[i] == "" {
			totals = append(totals, total)
			total = 0
		} else {
			intVar, err := strconv.Atoi(input_file[i])
			check(err)
			total += intVar
		}
	}
	totals = append(totals, total)

	sort.Sort(sort.Reverse(sort.IntSlice(totals)))

	// sum of totals array
	sum := 0
	for i := 0; i < 1; i++ {
		sum += totals[i]
	}

	return sum
}

func part2(input_file []string) int {
	total := 0
	totals := []int{}
	for i := 0; i < len(input_file); i++ {
		if input_file[i] == "" {
			totals = append(totals, total)
			total = 0
		} else {
			intVar, err := strconv.Atoi(input_file[i])
			check(err)
			total += intVar
		}
	}
	totals = append(totals, total)

	sort.Sort(sort.Reverse(sort.IntSlice(totals)))

	// sum of totals array
	sum := 0
	for i := 0; i < 3; i++ {
		sum += totals[i]
	}

	return sum
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
