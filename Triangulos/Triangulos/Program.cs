using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Triangulos
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Triangulos triangulos = new Triangulos();
            Console.WriteLine("INGRESE EL LADO A DEL TRIANGULO:");
            int ladoA = int.Parse(Console.ReadLine());
            Console.WriteLine("INGRESE EL LADO B DEL TRIANGULO:");
            int ladoB = int.Parse(Console.ReadLine());
            Console.WriteLine("INGRESE EL LADO C DEL TRIANGULO:");
            int ladoC = int.Parse(Console.ReadLine());
            Console.WriteLine(triangulos.CalcularTipo(ladoA,ladoB,ladoC));
            Console.ReadKey();
        }
    }
}
