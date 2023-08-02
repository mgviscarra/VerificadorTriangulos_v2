using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace V_Triangulos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            // Input sides
            Console.Write("INGRESE EL LADO A DEL TRIANGULO: ");
            double a = GetValidInput('A');

            Console.Write("INGRESE EL LADO B DEL TRIANGULO: ");
            double b = GetValidInput('B');

            Console.Write("INGRESE EL LADO C DEL TRIANGULO: ");
            double c = GetValidInput('C');

            // Determine type of triangle
            if (a == b && b == c)
            {
                Console.WriteLine("El triángulo es equilátero.");
            }
            else if (a == b || b == c || a == c)
            {
                Console.WriteLine("El triángulo es isósceles.");
            }
            else
            {
                Console.WriteLine("El un triángulo es escaleno.");
            }

            Console.ReadKey();
        }
        static double GetValidInput(char side)
        {
            double input;

            if (!double.TryParse(Console.ReadLine(), out input) || input <= 0)
            {
                Console.WriteLine("Entrada inválida. \nIngrese un número positivo para el lado " + side + " :");
                return GetValidInput(side); // llamada recursiva
            }

            return input;
        }
    }
}
