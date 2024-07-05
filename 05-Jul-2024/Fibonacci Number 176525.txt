# Problem: Fibonacci Number - https://leetcode.com/problems/fibonacci-number/

public class Solution {
    public int Fib(int n) {
        if (n < 2) {
            return n;
        }

        int prev = 0;
        int curr = 1;

        for (int i = 1; i < n; i++) {
            int temp = prev;
            prev = curr;
            curr += temp;
        }

        return curr;
    }
}