# Problem: Accounts Merge - https://leetcode.com/problems/accounts-merge/

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        def find_real_owner(real_owners, owner):
            while owner != real_owners[owner]:
                real_owners[owner] = real_owners[real_owners[owner]]
                owner = real_owners[owner]
            
            return owner

        n = len(accounts)
        real_owners = [i for i in range(n)]
        owners = {}

        # map every email to their real owner
        for idx ,(_, *emails) in enumerate(accounts):
            for email in emails:
                if email in owners:
                    curr_email_owner = owners[email]
                    curr_email_real_owner = find_real_owner(real_owners, curr_email_owner)

                    curr_account_real_owner =find_real_owner(real_owners, idx)

                    real_owners[curr_account_real_owner] = curr_email_real_owner
                
                else:
                    owners[email] = idx

        merged_accounts = [[] for _ in range(n)]

        for email, owner in owners.items():
            real_owner = find_real_owner(real_owners, owner)
            merged_accounts[real_owner].append(email)
        
        merged_acounts_with_owner = []
        for idx, merged_account in enumerate(merged_accounts):
            if not merged_account:
                continue
            name_of_owner = accounts[idx][0]
            merged_account.sort(reverse = True)
            merged_account.append(name_of_owner)

            merged_account.reverse()
            merged_acounts_with_owner.append(merged_account)

        return merged_acounts_with_owner

