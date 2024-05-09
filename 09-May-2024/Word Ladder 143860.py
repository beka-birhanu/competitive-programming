# Problem: Word Ladder - https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def check_adjacence(word1, word2):
            n = len(word1)
            diff = 0
            for i in range(n):
                if word1[i] != word2[i]:
                    diff += 1
                    if diff > 1:
                        return False
            
            return True
        
        n = len(wordList)
        word_adj_list = defaultdict(list)

        for i in range(n):
            word1 = wordList[i]
            for j in range(i+1, n):
                word2 = wordList[j]

                if check_adjacence(word1, word2):
                    word_adj_list[word1].append(word2)
                    word_adj_list[word2].append(word1)

        queue = deque([(beginWord, 1)])
        visited = set([beginWord])
        if beginWord not in wordList:
            queue.pop()
            for word in wordList:
                if check_adjacence(beginWord, word):
                    queue.append((word, 2))

        while queue:
            word, words_num = queue.popleft()
            if word == endWord:
                return words_num
            
            for adj in word_adj_list[word]:
                if adj not in visited:
                    visited.add(adj)
                    queue.append((adj, words_num+1))
        
        return 0
