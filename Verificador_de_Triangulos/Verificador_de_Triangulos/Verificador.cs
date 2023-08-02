namespace Verificador_de_Triangulos
{
    public static class Verificador
    {
        //Verificacion del tipo del triangulo
        public static string DeterminarTriangulo(float a, float b, float c)
        {
            if (!ValidarTriangulo(a, b, c))
            {
                return ("TRIANGULO INVALIDO");
            }

            if (a == b && b == c)
            {
                return ("EL TRIANGULO ES EQUILATERO");
            }
            else if (a == b || a == c || b == c)
            {
                return ("EL TRIANGULO ES ISOSCELES");
            }
            else
            {
                return ("EL TRIANGULO ES ESCALENO");
            }
        }

        // Verificacion de validez de los valores a, b y c
        private static bool ValidarTriangulo(float a, float b, float c)
        {
            return (a + b > c && a + c > b && b + c > a);
        }
    }
}
