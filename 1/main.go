package main

//https://leetcode.com/problems/generate-parentheses/
import "fmt"

func main() {
	res := generateParenthesis(4)
	fmt.Println(len(res))
	fmt.Println(res)
}

func generateParenthesis(n int) []string {
	var res = make([]string, 0)
	generate(n, n, "", &res)
	return res
}

func generate(open int, close int, temp string, res *[]string) {
	if open > close {
		return
	}
	if open == 0 && close == 0 {
		*res = append(*res, temp)
	}
	if open > 0 {
		generate(open-1, close, temp+"(", res)
	}
	if close > 0 {
		generate(open, close-1, temp+")", res)
	}
}
