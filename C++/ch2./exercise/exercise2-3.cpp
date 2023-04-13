#include <iostream>
using namespace std;

int main()
{
    cout << "Enter a number in pounds: ";
    double pounds;
    cin >> pounds;

    double poundInKilogram = 0.454;
    double kilometers = pounds * poundInKilogram;

    cout << pounds << " pounds is " << kilometers << endl;

    return 0;


}