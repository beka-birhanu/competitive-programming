# Problem: Find Common Characters - https://leetcode.com/problems/find-common-characters/

public class Solution {
    public IList<string> CommonChars(string[] words) {
        List<string> result = new List<string>();
        if (words == null || words.Length == 0) {
            return result;
        }

        int[] minFreq = new int[26];
        Array.Fill(minFreq, int.MaxValue);

        foreach (string word in words) {
            int[] charCount = new int[26];
            foreach (char c in word) {
                charCount[c - 'a']++;
            }
            for (int i = 0; i < 26; i++) {
                minFreq[i] = Math.Min(minFreq[i], charCount[i]);
            }
        }

        for (int i = 0; i < 26; i++) {
            for (int j = 0; j < minFreq[i]; j++) {
                result.Add(((char)(i + 'a')).ToString());
            }
        }

        return result;
    }
}