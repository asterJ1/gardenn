#include <iostream>
using namespace std;

int main()
{
    double minutes = 45.5;
    double oneHour = minutes / 60.0;

    int kimometers = 14;
    double miles = kimometers / 1.6;

    double milesPerHour = miles / oneHour;

    cout << "Milesperhour of the player is " << milesPerHour << endl;

    return 0;
}