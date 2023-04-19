#include <iostream>
using namespace std;

int main()
{
    cout << "Enter the subtotal and a gratuity rate: ";
    int subtotal;
    int gratuity;
    cin >> subtotal >> gratuity;

    double gratuityRate = gratuity / 100.0;
    double gratuityMoney = subtotal * gratuityRate;
    double total = subtotal + gratuityMoney;

    cout << "The gratuity is $" << gratuityMoney << " and total is $" << total << endl;

    return 0;
}