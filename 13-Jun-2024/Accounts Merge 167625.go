# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

public class Solution {
    public IList<IList<string>> AccountsMerge(IList<IList<string>> accounts) {
        int Find(int idx, int[] groups) {
            while (idx != groups[idx]) {
                groups[idx] = groups[groups[idx]];
                idx = groups[idx];
            }
            return idx;
        }

        Dictionary<string, int> emailToIndexMap = new Dictionary<string, int>();
        int[] groups = new int[accounts.Count];

        for (int i = 0; i < accounts.Count; i++) {
            IList<string> account = accounts[i];
            groups[i] = i;

            for (int j = 1; j < account.Count; j++) {
                string email = account[j];

                if (emailToIndexMap.ContainsKey(email)) {
                    int idx = emailToIndexMap[email];
                    int groupIdx = Find(idx, groups);

                    groups[groupIdx] = i;
                }

                emailToIndexMap[email] = i;
            }
        }

        IList<IList<string>> mergedAccounts = new List<IList<string>>();

        for (int i = accounts.Count - 1; i >= 0; i--) {
            List<string> mergedAccount = new List<string>();

            for (int j = 0; j < groups.Length; j++) {
                int group = Find(j, groups);

                if (group == i) {
                    IList<string> account = accounts[j];

                    for (int k = 1; k < account.Count; k++) {
                        string email = account[k];
                        if (!mergedAccount.Contains(email)) {
                            mergedAccount.Add(email);
                        }
                    }
                }
            }

            if (mergedAccount.Count == 0) {
                continue;
            }

            string name = accounts[i][0];
            mergedAccount.Sort(StringComparer.Ordinal);
            mergedAccount.Insert(0, name);

            mergedAccounts.Add(mergedAccount);
        }
        
        return mergedAccounts;
    }
}
