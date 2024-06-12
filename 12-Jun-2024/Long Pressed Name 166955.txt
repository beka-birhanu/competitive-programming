# Problem: Long Pressed Name - https://leetcode.com/problems/long-pressed-name/

public class Solution {
    public bool IsLongPressedName(string name, string typed) {
        int i = 0;

        foreach(char letter in name){
            while(i > 0  && i < typed.Length && letter != typed[i] && typed[i] == typed[i-1]){
                i++;
            }
            if (i >= typed.Length){
                return false;
            }
            if(letter != typed[i]){
                return false;
            }
            i++;
        }

        for(;i < typed.Length; i++){
            if (typed[i] != typed[i-1]){
                return false;
            }
        }
        return true;
    }
}