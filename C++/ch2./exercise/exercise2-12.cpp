#include <iostream>
using namespace std;

int main()
{
    cout << "Enter speed and acceleration: ";
    double s, a;
    cin >> s >> a;

    double l = (s * s) / (2.0 * a);
    cout.precision(6);

    cout << "The minimum runway length for this airplane is " << l << endl;

    return 0;
}