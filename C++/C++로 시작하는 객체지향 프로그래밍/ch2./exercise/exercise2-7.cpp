#include <iostream>
using namespace std;

int main()
{
    cout << "Enter the number of minutees: ";
    int minutes;
    cin >> minutes;

    double hours = minutes / 60.0;
    double days = hours / 24;
    double years = days / 365;

    cout << minutes << " minutes is approximately " << years << " years and " << days << " days" << endl;

    return 0;
}