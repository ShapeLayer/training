using System;

public class Program {
    public static void Main(string[] args) {
        string[] gets = Console.ReadLine().Split(' ');
        int _str = int.Parse(gets[0]), _dex = int.Parse(gets[1]), _int = int.Parse(gets[2]), _luk = int.Parse(gets[3]), n = int.Parse(gets[4]);
        int total = _str + _dex + _int + _luk;
        Console.WriteLine(n * 4 - total > 0 ? n * 4 - total : 0);
    }
}