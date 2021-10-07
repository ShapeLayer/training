#include <iostream>

int main(void) {
    const int STUDENTS = 10;
    int arr[STUDENTS];
    for (int i = 0; i < STUDENTS; i++) std::cin >> arr[i];
    int sum = 0;
    for (int i = 0; i < STUDENTS; i++) sum += arr[i];
    std::cout << "Average of grade: " << sum/STUDENTS;
    return 0;
}
