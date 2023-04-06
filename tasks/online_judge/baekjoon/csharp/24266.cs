using System;

public class Program
{
    public static void Main(string[] args)
    {
        long n = long.Parse(Console.ReadLine());
        // Console.WriteLine((long)Math.Pow(n, 3)); 은 부동소수점 연산의 정밀도 때문에 오답으로 처리된다.
        Console.WriteLine(n*n*n);
        Console.WriteLine(3);
    }
}