#include <iostream>
using namespace std;

int main()
{
    cout << "Enter v0, v1 and t: ";
    double v0;
    double v1;
    double t;
    cin >> v0 >> v1 >> t;

    double average = (v1 - v0) / t;
    cout << "The average acceleration is " << average << endl;

    return 0;
}