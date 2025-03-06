Console.WriteLine("Hello, World!");
int number = new Random().Next(1, 7);

switch (number)
{
    case 1:
        Console.WriteLine("Veeretasin nr " + number);
        break;

    case 2:
        Console.WriteLine("Veeretasin arvu nr " + number);
        break;

    case 3:
        Console.WriteLine("Veeretasin nr " + number);
        break;

    case 4:
        Console.WriteLine("Sisestasin nr " + number);
        break;

    case 5:
        Console.WriteLine("Veeretasin nr" + number);
        break;

    case 6:
        Console.WriteLine("Sisestasin nr" + number);
        break;

    default:
        Console.WriteLine("Error");
        break;
}
