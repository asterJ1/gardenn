#include <iostream>
#include <ctime>
using namespace std;

int main()
{
    cout << "Enter the number of minutes: ";
    int totalMinutes;
    cin >> totalMinutes;

    int totalHours = totalMinutes / 60;
    int totalDays = totalHours / 24;
    int currentDays = totalDays % 365;
    int totalYears = totalDays / 365;

    cout << totalMinutes << " minutes is approximately " << totalYears << " years and " << currentDays << "days" << endl;

    return 0;
}