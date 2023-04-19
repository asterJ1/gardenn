#include <iostream>
using namespace std;

int main()
{
    double const PI = 3.14159;
    cout << "Enter the radius and length of a cylinder: ";
    double radius;
    cin >> radius;
    double length;
    cin >> length;

    double area = radius * radius * PI;
    double volume = area * length;

    cout << "The area is " << area << endl;
    cout << "The volume is " << volume << endl;

    return 0;
}