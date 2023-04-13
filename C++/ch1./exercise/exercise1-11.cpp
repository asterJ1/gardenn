#include <iostream>
using namespace std;

int main()
{
    int currentHuman = 312032486;
    int oneYearSeconds = 365 * 24 * 60 * 60;
    double birth = oneYearSeconds / 7.0;
    double death = oneYearSeconds / 13.0;
    double immigrate = oneYearSeconds / 45.0;

    double firstYear = currentHuman + birth - death - immigrate;
    double secondYear = firstYear + birth - death - immigrate;
    double thirdYear = secondYear + birth - death - immigrate;
    double forthYear = thirdYear + birth - death - immigrate;
    double fifthYear = forthYear + birth - death - immigrate;

    cout.precision(10);

    cout << "The population of the first year is " << firstYear << endl;
    cout << "The population of the second year is " << secondYear << endl;
    cout << "The population of the third year is " << thirdYear << endl;
    cout << "The population of the forth year is " << forthYear << endl;
    cout << "The population of the fifth year is " << fifthYear << endl;

    return 0;
}