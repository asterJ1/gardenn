#include <iostream>
using namespace std;

int main()
{
    cout << "Enter a degree in Celsius: ";
    int celsius;
    cin >> celsius;

    double fahrenheit = (9.0 / 5) * celsius + 32;

    cout << celsius << " Celsius is " << fahrenheit << " Fahrenheit" << endl;

    return 0;
}