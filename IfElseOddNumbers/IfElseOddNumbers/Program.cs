namespace IfElseOddNumbers
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            Console.WriteLine("Sisesta number ");
            int number = int.Parse(Console.ReadLine());

            if (true)
            {
                Console.WriteLine("Sisestasid paaris arvu" + number);
            }
            else 
            {
               Console.WriteLine("Sisetasid paaritu arvu" + number);
            
              }
           }
    }
}
