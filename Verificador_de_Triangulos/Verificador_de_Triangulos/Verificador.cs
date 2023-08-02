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

        // Validar float
        public static float NumeroValido(string mensaje)
        {
            while (true)
            {
                try
                {
                    Console.WriteLine(mensaje);
                    float numero = float.Parse(Console.ReadLine());

                    if (float.IsInfinity(numero))
                    {
                        throw new OverflowException();
                    }
                    else if (numero > 0)
                    {
                        return numero;
                    }
                    else
                    {
                        Console.WriteLine("ERROR: Ingrese un número mayor a 0.");
                    }
                }
                // Manejo de errores
                // -    Tipo no Numeral
                catch (FormatException)
                {
                    Console.WriteLine("ERROR: Ingrese un número válido.");
                }
                // -    Numero fuera de rango de float
                catch (OverflowException)
                {
                    Console.WriteLine("ERROR: Ingrese un número dentro del rango de float.");
                }
                // -   Errores inesperados
                catch (Exception ex)
                {
                    Console.WriteLine($"ERROR INESPERADO: {ex.Message}");
                }
            }
        }
    }
}
