using System;
using PeopleLibrary;

//This client should be in a separate project.
namespace SimpleClient
{
    class Program
    {
        static void Main(string[] args)
        {
            var bart = new ManagedPerson(10, "Bart");
            Console.WriteLine(bart.Name);
            bart.Age++;
            Console.WriteLine(bart.SayHello("Hello"));
        }
    }
}
