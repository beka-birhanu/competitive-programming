# Problem: N Queens II - https://leetcode.com/problems/n-queens-ii/

public class Solution
{
    public int TotalNQueens(int n)
    {
        int solutions = 0;

        bool[] isAtCol = new bool[n];
        bool[] isAtD1 = new bool[2 * n - 1]; 
        bool[] isAtD2 = new bool[2 * n - 1]; 

        void Solve(int row)
        {
            if (row == n)
            {
                solutions++;
                return;
            }

            for (int i = 0; i < n; i++)
            {
                int d1Index = row - i + (n - 1);
                int d2Index = row + i;

                if (!isAtCol[i] && !isAtD1[d1Index] && !isAtD2[d2Index])
                {
                    isAtCol[i] = true;
                    isAtD1[d1Index] = true;
                    isAtD2[d2Index] = true;

                    Solve(row + 1);

                    isAtCol[i] = false;
                    isAtD1[d1Index] = false;
                    isAtD2[d2Index] = false;
                }
            }
        }

        Solve(0);
        return solutions;
    }
}
