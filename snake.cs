









random// See https://aka.ms/new-console-template for more information
using System;
namespace ders
{
    class Sample
    {
        public static void Main()
        {
            char ch;
            int[] satır = new int[100];
            int[] sütun = new int[100];
            int a, b;
            int k = 4;
            satır[0] = 15;
            satır[1] = 15;
            satır[2] = 15;
            satır[3] = 15;
            satır[4] = 15;
            sütun[0] = 38;
            sütun[1] = 39;
            sütun[2] = 40;
            sütun[3] = 41;
            sütun[4] = 42;
            Console.CursorVisible = false;
            Random rnd = new Random();
            Random:;
            a = rnd.Next(Console.WindowWidth);
            b = rnd.Next(Console.WindowHeight);
            Console.SetCursorPosition(a, b);
            Console.Write("*");
            while (0 != 1)
            {
                for (int c = 1; c < k-1; c++)
                {
                    if (sütun[0] == sütun[c] && satır[0] == satır[c])
                    {
                        goto bitti;
                    }
                    Console.SetCursorPosition(sütun[0], satır[0]);
                    Console.Write("0");
                }
                for (int i = k+1; i>0; i--)
                {
                    satır[i] = satır[i - 1];
                }
                for (int y = k + 1; y > 0; y--)
                {
                    sütun[y] = sütun[y - 1];
                }
                for(int x = 1; x <= k; x++)
                {
                    Console.SetCursorPosition(sütun[x+1], satır[x+1]);
                    Console.Write("*");
                }
                Console.SetCursorPosition(sütun[k+1], satır[k+1]);
                Console.Write(" ");
                

                ch = Console.ReadKey(true).KeyChar;
                switch (ch)
                {
                    case 'a':
                        --sütun[0];
                        break;
                    case 'd':
                        ++sütun[0];
                        break;
                    case 'w':
                        --satır[0];
                        break;
                    case 's':
                        ++satır[0];
                        break;

                }
                
                if (a == sütun[0] && b == satır[0])
                {
                    Console.SetCursorPosition(a, b);
                    Console.Write("0");
                    k++;
                    goto Random;
                }
        
            }
        bitti:;
            Console.WriteLine("oyun bitti");
        }


    }
}