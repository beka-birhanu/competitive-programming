# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

public class Solution {
    public int LengthOfLongestSubstring(string s) 
    {
        var aux = "";
        var substrings = new List<string>();

        if (s.Length == 0)
            return 0;

        for (int i = 0; i < s.Length; i++)
        {
            var charIndex = aux.IndexOf(s[i]);
            if (charIndex == -1)
                aux += s[i];
            else
            {
                substrings.Add(aux);

                aux = aux.Substring(charIndex + 1);
                aux += s[i];
            }

            if (i == s.Length - 1)
                substrings.Add(aux);
        }

        return substrings.Max(x => x.Length);
    }
}