# Problem: Sorting the Sentence - https://leetcode.com/problems/sorting-the-sentence/

public class Solution {
    public string SortSentence(string s) {
        string[] words = s.Split();
        int N = words.Length;
        string[] sorted = new string[N];

        foreach(string word in words){
            int idx = int.Parse(word[word.Length - 1].ToString());
            sorted[idx-1] = word.Substring(0, word.Length - 1);
        }
        return string.Join(" ", sorted);
    }
}