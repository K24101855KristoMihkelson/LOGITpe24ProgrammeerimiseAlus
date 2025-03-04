namespace IfAndElse
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");

            Console.WriteLine("Sisesta enda age ");

            int age = int.Parse(Console.ReadLine());

            if (age >= 0 && age <= 18)
            {
                Console.WriteLine("Sa oled alaealine");
            }
            else if (age >= 19 && age <= 65)
            {
                Console.WriteLine("Sa oled juba täiskasvanud");
            }

            else
            {
                Console.WriteLine("Sa oled pensionäär");
            }
        }
    }
}











