#include <iostream>
#include <chrono>
#include <valarray>
#include <iomanip>

using namespace std;

int main() {
    double sum = 0;
    double partial_sum = 0;
    long num = 94906266;

    auto start_time = chrono::high_resolution_clock::now();

    while (num>0) {
        partial_sum= 1.0/pow(num,2);
        sum += partial_sum;
        num -=1;

    }
    auto end_time = chrono::high_resolution_clock::now();
    chrono::duration<double> execution_time = end_time-start_time;
    cout << "Execution time: " << execution_time.count() << "seconds"<< std::endl;
    cout << "Total sum: " << setprecision(100) <<sum << std::endl;

    long double analytical = pow(M_PI, 2) / 6;
    cout << "Analytical value is: " << setprecision(100) << analytical << endl;

    long double relative_percentage_difference = ((analytical - sum) / analytical) * 100;
    cout << "Relative percentage difference is: " << relative_percentage_difference << "%" << endl;

    return 0;
}