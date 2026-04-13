module Demo
{
    interface Printer
    {
        void printString(string s);
        int add(int a, int b);
        int sub(int a, int b);
    }

    interface Logger
    {
        void log(string message);
    }
}
