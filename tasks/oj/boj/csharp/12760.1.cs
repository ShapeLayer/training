using System;
using System.Collections.Generic;

public class Program 
{
    public static void Main(string[] args)
    {
        string[] puts = Console.ReadLine().Split(' ');
        (int n, int m) = (int.Parse(puts[0]), int.Parse(puts[1]));
        int[][] decks = new int[n][];
        for (int i = 0; i < n; i++)
        {
            string[] input = Console.ReadLine().Split(' ');
            int[] cards = new int[m];
            for (int j = 0; j < m; j++)
            {
                cards[j] = int.Parse(input[j]);
            }
            decks[i] = cards;
        }
        foreach (var cards in decks)
        {
            Array.Sort(cards);
            Array.Reverse(cards);
        }
        List<Queue<int>> queues = new List<Queue<int>>();
        foreach (var cards in decks)
        {
            Queue<int> q = new Queue<int>(cards);
            queues.Add(q);
        }

        int[] score = new int[n];
        for (int round = 0; round < m; round++)
        {
            int[] card_submitted = new int[n];
            for (int i = 0; i < n; i++)
            {
                card_submitted[i] = queues[i].Dequeue();
            }
            int max = card_submitted.Max();
            for (int i = 0; i < n; i++)
            {
                if (card_submitted[i] == max)
                {
                    score[i] += 1;
                }
            }
        }
        int maxScore = score.Max();
        List<int> winners = new List<int>();
        for (int i = 0; i < n; i++)
        {
            if (score[i] == maxScore)
            {
                winners.Add(i+1);
            }
        }
        Console.WriteLine(string.Join(" ", winners));
    }
}