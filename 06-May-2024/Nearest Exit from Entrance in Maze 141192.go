# Problem: Nearest Exit from Entrance in Maze - https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/

public class Solution {
    public int NearestExit(char[][] maze, int[] entrance) {
        bool IsInbound(int x, int y, int maxX, int maxY){
            return x >= 0 && x < maxX && y >= 0 && y < maxY;
        }

        var DIRECTIONS = new Tuple<int, int>[] 
                                { new Tuple<int, int>(0, 1), new Tuple<int, int>(0, -1), new Tuple<int, int>(1, 0), new Tuple<int, int>(-1, 0) };
        var queue = new Queue<Tuple<int, int, int>>();
        var maxRow = maze.Length;
        var maxCol = maze[0].Length; 
        queue.Enqueue(Tuple.Create(0, entrance[0], entrance[1]));
        maze[entrance[0]][entrance[1]] = '+';

        while(queue.Count > 0){
            var (steps, row, col) = queue.Dequeue();

            foreach (var (dRow, dCol) in DIRECTIONS){
                var nextRow = row + dRow; 
                var nextCol = col + dCol; 
                if (!IsInbound(nextRow, nextCol, maxRow, maxCol)){
                    if(steps > 0){
                        return steps;
                    }
                    continue;
                }
                if (maze[nextRow][nextCol] != '+'){ 
                    maze[nextRow][nextCol] = '+'; 
                    queue.Enqueue(Tuple.Create(steps+1, nextRow, nextCol)); 
                }
            }
        }
        return -1;
    }
}
