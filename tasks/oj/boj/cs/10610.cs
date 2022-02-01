using System;

public class Program
{
    public static void Main(string[] args)
    {
        char[] puts = Console.ReadLine().ToCharArray();
        if (!puts.Contains('0'))
        {
            Console.WriteLine(-1);
            return;
        }
        int[] nums = new int[puts.Length];
        for (int i = 0; i < puts.Length; i++)
        {
            nums[i] = (int)puts[i] - 48;
        }
        if (nums.Sum() % 3 != 0) {
            Console.WriteLine(-1);
            return;
        }
        Array.Sort(nums);
        Array.Reverse(nums);
        Console.WriteLine(String.Join("", nums));
    }
}