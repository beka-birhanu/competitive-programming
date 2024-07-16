# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

public class Solution {
    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries) {
        
        HashSet<string> vis = new HashSet<string>();
        Dictionary<string, Dictionary<string, double>> d = new Dictionary<string, Dictionary<string, double>>();

        for (int i = 0; i < equations.Count; i++)
        {
            string numerator = equations[i][0];
            string denominator = equations[i][1];
            double resultValue = values[i];

            if (!d.ContainsKey(numerator))
                d[numerator] = new Dictionary<string, double>();
            
            if (!d.ContainsKey(denominator))
                d[denominator] = new Dictionary<string, double>();

            d[numerator][denominator] = resultValue;
            d[denominator][numerator]  = 1 / resultValue;
        }

        return queries.Select(q => EvaluateQuery(q[0], q[1], d, vis)).ToArray();
    }

    private double EvaluateQuery(string num, string den, Dictionary<string, Dictionary<string, double>> d, HashSet<string> vis)
    {
        if (!d.ContainsKey(num) || !d.ContainsKey(den))
            return -1;

        if (num == den)
            return 1;

        if (d.ContainsKey(num) && d[num].ContainsKey(den))
            return d[num][den];

        vis.Add(num);
        double cur = -1;
        foreach (var key in d[num].Keys)
        {
            if (!vis.Contains(key))
            {
                cur = EvaluateQuery(key, den, d, vis);
                if (cur != -1)
                {
                    cur = cur * d[num][key];
                    break;
                }
            }
        }

        vis.Remove(num);
        return cur;
    }
}