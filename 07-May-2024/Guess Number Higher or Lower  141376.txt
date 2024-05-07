# Problem: Guess Number Higher or Lower  - https://leetcode.com/problems/guess-number-higher-or-lower/

/** 
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * int guess(int num);
 */

public class Solution : GuessGame {
    private int higher = -1;
    private int lower = 1;

    public int GuessNumber(int n) {
        var left = 0;
        var right = n;

        while (left <= right){
            var mid = left + (right - left) / 2;
            var response = guess(mid);

            if (response == this.higher){
                right = mid -1;
            }else if(response == this.lower){
                left = mid+1;
            }else{
                return mid;
            }
        }
        return -1;
    }
}