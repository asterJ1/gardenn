#include <iostream>
using namespace std;

int main()
{
    cout << "Enter the amount of water in kilograms: ";
    double amountInKilograms;
    cin >> amountInKilograms;

    cout << "Enter the initial temperature: ";
    double initTemp;
    cin >> initTemp;

    cout << "Enter the final temperature: ";
    double finTemp;
    cin >> finTemp;

    double Q = amountInKilograms * (finTemp - initTemp) * 4184;
    cout.precision(10);
    cout << "The energy needed is " << Q << endl;

    return 0;
}