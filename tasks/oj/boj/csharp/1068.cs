using System;

public class Program
{
    static int[] parents = new int[50];
    static int rm;
    static bool[] isLeaf = new bool[50];
    public static void Main(string[] args)
    {
        int n = int.Parse(Console.ReadLine());
        for (int i = 0; i < n; i++) Program.isLeaf[i] = true;
        string[] gets = Console.ReadLine().Split(' ');
        for (int i = 0; i < n; i++) parents[i] = int.Parse(gets[i]);
        rm = int.Parse(Console.ReadLine());
        for (int i = 0; i < n; i++)
        {
            if (parents[i] == -1) continue;
            if (!find(i)) continue;
            isLeaf[parents[i]] = false;
        }
        int counts = 0;
        for (int i = 0; i < n; i++)
        {
            if (isLeaf[i] && find(i)) counts++;
        }
        Console.WriteLine(counts);
    }

    public static bool find(int puts)
    {
        if (puts == rm) return false;
        if (parents[puts] == -1) return true;
        return find(parents[puts]);
    }
}