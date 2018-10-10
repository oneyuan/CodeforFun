package main

import "fmt"

func main() {
    fmt.Println(isScramble("great", "rgeat"))
}



func isScramble(s1 string, s2 string) bool {
    if s1 == s2 {
        return true
    }
	var count [26]int
    n := len(s1)
    for i:=0; i<n; i++ {
        count[int(s1[i]) - int('a')]++
        count[int(s2[i]) - int('a')]--
    }
    
    for i:=0; i<26; i++ {
        if count[i] != 0 {
            return false
        }
    }
    
    for i:=1; i<n; i++ {
        if isScramble(s1[:i], s2[:i]) && isScramble(s1[i:], s2[i:]) {
            return true
        }
        if isScramble(s1[:i], s2[n-i:]) && isScramble(s1[i:], s2[:n-i]) {
            return true
        }
    }
    return false
}