namespace MethodCode2
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            int number = int parse(Console.ReadLine());

            if (int.IsEvenInteger(number))
            {
                EvenNumbers(EvenNumbers);
            }
            else
            {
                OddNumbers(number);

           static void EvenNumbers(int nr) 
           {
                Console.WriteLine("Tegemist on paaris arvuga" + nr);

           static void OddNumbers(int nr) 
           {
                Console.WriteLine("Tegemist on paaritu arvuga" + nr);
        }
    }
}
