class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i = 0
        while  i < len(command):
            if command[i] == "G":
                ans += "G"
            else:
                if command[i+1] == "a":
                    ans += "al"
                    i += 3
                else:
                    ans += "o"
                    i += 1
            i += 1
        return ans