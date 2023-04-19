#include <iostream>
using namespace std;

int main()
{
    cout << "Enter a number between 0 and 1000: ";
    int num;
    cin >> num;

    int firstNum = num / 100;
    num = num % 100;
    int secondNum = num / 10;
    num = num % 10;
    int sum = firstNum + secondNum + num;

    cout << "The sum of the digits is " << sum << endl;

    return 0;
}