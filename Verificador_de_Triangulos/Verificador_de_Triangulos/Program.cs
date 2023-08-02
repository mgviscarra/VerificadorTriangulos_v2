namespace Verificador_de_Triangulos
{
    public class Program
    {
        static void Main(string[] args)
        {
            while (true)
            {
                try
                {
                    float a = Verificador.NumeroValido("INGRESE EL LADO A DEL TRIANGULO:");
                    float b = Verificador.NumeroValido("INGRESE EL LADO B DEL TRIANGULO:");
                    float c = Verificador.NumeroValido("INGRESE EL LADO C DEL TRIANGULO:");

                    Console.WriteLine(Verificador.DeterminarTriangulo(a, b, c));
                }
                // Errores inesperados
                catch (Exception ex)
                {
                    Console.WriteLine($"ERROR INESPERADO: {ex.Message}");
                }
                //Control del ciclo
                Console.WriteLine("¿DESEA VOLVER A INTENTAR VERIFICAR UN TRIANGULO? (S/Cualquier otra respuesta)");
                string respuesta = Console.ReadLine();
                if (!respuesta.Equals("S", StringComparison.OrdinalIgnoreCase))
                {
                    break;
                }
            }
        }
    }
}