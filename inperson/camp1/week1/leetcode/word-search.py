class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def validate_position(pos, board):
            #validate the indexes are not out of bound and that possition haven been used already
            return (0 <= pos[0] < len(board)) and (0 <= pos[1] < len(board[0])) and (board[pos[0]][pos[1]] !="s")


        def new_positions(curr_pos, board):
            #generate vlaid new positions by using all the possible directions
            for di, dj in [(0,1), (0,-1), (-1,0), (1,0)]:
                new_pos = curr_pos[0]+di, curr_pos[1]+dj

                if validate_position(new_pos, board):
                    yield new_pos
            

        def backtrack(board_pos, word_pos, board, word):
            if word_pos >= len(word):
                return True

            for new_pos in new_positions(board_pos, board):
                i, j = new_pos
                #if the new possition have the letter in need check for the rest of the word
                if board[i][j] == word[word_pos]:
                    board[i][j] = "s" #marking as seen

                    if backtrack(new_pos, word_pos+1, board, word):
                        return True

                    board[i][j] = word[word_pos]

            return False

        R = len(board)
        C = len(board[0])
        
        if len(word) > R*C:
            return False
        
        count = Counter(sum(board, []))
        
        for c, countWord in Counter(word).items():
            if count[c] < countWord:
                return False
            
        if count[word[0]] > count[word[-1]]:
             word = word[::-1]
             
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    board[i][j] = "s"

                    if backtrack((i,j), 1, board, word):
                        return True

                    board[i][j] = word[0]
                    
        return False
        
