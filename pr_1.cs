using System;
using System.Collections.Generic;

namespace ConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            List<List<double>> start_matrix = new List<List<double>>
            {
                new List<double> { -1, 0, 2, 3 },
                new List<double> { 0, 1, 9, 28 }
            };

            foreach (var row in start_matrix)
            {
                for (int i = 0; i < 4; i++) 
                {
                    Console.Write("{0} ", row[i]);
                }
                Console.WriteLine();
            }
            List<double> row_x = new List<double>(start_matrix[0]);
            List<double> row_f = new List<double>(start_matrix[1]);
            int count_len = row_x.Count;
            List<List<double>> itog = new List<List<double>>();
            for (int i = 0; i < 4; i++)
            {
                itog.Add(new List<double>(new double[5]));
            }
            for (int i = 0; i < count_len; i++)
            {
                for (int j = 0; j < count_len; j++)
                {
                    itog[i][j] = Math.Pow(row_x[i], count_len - j - 1);
                }
                itog[i][4] = row_f[i];
            }
            foreach (var row in itog)
            {
                for (int i = 0; i < 5; i++)
                {
                    Console.Write("{0} ", row[i]);
                }
                Console.WriteLine();
            }
        }
    }
}
