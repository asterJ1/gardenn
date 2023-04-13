#include <iostream>
using namespace std;

int main()
{
    double r = 5.5;
    double const PI = 3.14159;
    double l = PI * r * 2;
    double s = PI * r * r;

    cout << "The area of the circle is " << s << endl;
    cout << "The circumference of the circle is " << l << endl;

    return 0;
}