#include <iostream>
using namespace std;

int main()
{
    cout.precision(10);
    int currentHuman = 312032486;
    int oneYearSeconds = 365 * 24 * 60 * 60;
    double birth = oneYearSeconds / 7.0;
    double death = oneYearSeconds / 13.0;
    double immigrate = oneYearSeconds / 45.0;

    int year;
    cout << "Enter the number of years: ";
    cin >> year;

    double totalHuman = currentHuman + (birth - death + immigrate) * year;
    cout << "The population in " << year << " is " << totalHuman << endl;

    return 0;
}