# Problem: Maximal Square - https://leetcode.com/problems/maximal-square/

public class Solution
{
    public int MaximalSquare(char[][] matrix)
    {
        int[][] m = new int[matrix.Length][];
        for(int i=0; i<m.Length; i++)
            m[i] = new int[matrix[0].Length];

        for(int i=0; i<m.Length; i++)
        {
            for(int j=0; j<m[0].Length; j++)
                m[i][j] = matrix[i][j] == '1' ? 1 : 0;
        }

        return MaximalSquare(m);
    }

    public int MaximalSquare(int[][] m)
    {
        int p = m.Length;
        int q = m[0].Length;

        int max = 0;

        for(int i=p-1; i>=0; i--)
        {
            for(int j=q-1; j>=0; j--)
            {
                if(m[i][j] != 0)
                {
                    int a = j+1 >= q ? 0 : m[i][j+1];
                    int b = i+1 >= p ? 0 : m[i+1][j];
                    int c = i+1 >= p || j+1 >= q ? 0 : m[i+1][j+1];

                    m[i][j] = Math.Min(a, b);
                    m[i][j] = Math.Min(m[i][j], c);

                    m[i][j]++;
                }

                max = Math.Max(max, m[i][j]);
            }
        }

        return max*max;
    }
}