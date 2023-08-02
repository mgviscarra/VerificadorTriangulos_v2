using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Triangulos
{
    internal class Triangulos
    {
        int ladoA;
        int ladoB;
        int ladoC;  
        public string CalcularTipo(int ladoA, int ladoB, int ladoC)
        {
            this.ladoA = ladoA;
            this.ladoB = ladoB;
            this.ladoC = ladoC;
            if (ladoA == ladoB && ladoB == ladoC)
            {
                return "EL TRIANGULO ES EQUILATERO";
            }
            else if (ladoA == ladoB || ladoA == ladoC || ladoB == ladoC)
            {
                return "EL TRIANGULO ES ISOSCELES";
            }
            else 
            {
                return "EL TRIANGULO ES ESCALENO";
            }
        }
    }
}
