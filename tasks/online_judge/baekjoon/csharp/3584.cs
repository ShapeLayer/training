using System;
using System.Collections.Generic;

public class Program
{
    static int[] parents = new int[10001];

    public static void Main(string[] args)
    {
        int t = int.Parse(Console.ReadLine());
        for (int tp = 0; tp < t; tp++)
        {
            for (int i = 0; i < 10001; i++) parents[i] = -1;
            int n = int.Parse(Console.ReadLine());
            for (int i = 1; i < n; i++)
            {
                int[] gets = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
                parents[gets[1]] = gets[0];
            }
            int[] puts = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
            int[] finds0 = find(puts[0]).ToArray();
            int[] finds1 = find(puts[1]).ToArray();
            for (int j = 0; j < finds0.Length; j++)
            {
                if (finds1.Contains(finds0[j]))
                {
                    Console.WriteLine(finds0[j]);
                    break;
                }
            }
        }
    }

    public static List<int> find(int n)
    {
        List<int> self = new List<int>();
        self.Add(n);
        if (parents[n] == -1) return self;
        self.AddRange(find(parents[n]));
        return self;
    }
}