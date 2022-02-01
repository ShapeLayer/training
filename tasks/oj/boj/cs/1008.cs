using System;

public class Program
{
    public static void Main(string[] args)
    {
        int[] puts = Console.ReadLine().Split(' ').Select(int.Parse).ToArray();
        Console.WriteLine((double)puts[0] / (double)puts[1]);
    }
}