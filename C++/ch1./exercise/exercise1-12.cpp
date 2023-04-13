#include <iostream>
using namespace std;

int main()
{
    double minutes = 40 + 7 / 10.0;
    double hours = minutes / 60;
    int miles = 24;
    double kilometers = miles / 1.6;
    double kilometerPerHour = kilometers / hours;

    cout << "The kilometer per hour of the player is " << kilometerPerHour << endl;

    return 0;
}