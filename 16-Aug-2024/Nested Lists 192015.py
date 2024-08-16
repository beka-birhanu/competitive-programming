# Problem: Nested Lists - https://www.hackerrank.com/challenges/nested-list/problem?isFullScreen=true

from collections import defaultdict
if __name__ == '__main__':
    score_board = defaultdict(list)
    scores = set()
    for _ in range(int(input())):
        name = input()
        score = float(input())
        score_board[score].append(name)
        scores.add(score)
    
    second_lowest_grade = sorted(scores)[1]
    print("\n".join(sorted(score_board[second_lowest_grade])))
        