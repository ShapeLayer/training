//; # \u000a import java.util.Scanner; public class Main { public static void main(String[] args) { Scanner sc = new Scanner(System.in); int n = sc.nextInt(); String puts = ""; for (int i = 0; i <= n; i++) { puts += Integer.toBinaryString(i); } System.out.println(puts); } } /*
#if true /*
n = gets.to_i
put = ""
for i in 0..n do
  put += i.to_s(2)
end
puts put
=begin
/* */ // \u000a /*
#include <iostream>

using namespace std;

int main() {
    int arr[] = {0, 1, 10, 11, 100, 101, 110, 111, 1000, 1001, 1010};
    int n;
    cin >> n;
    for (int i = 0; i <= n; i++) {
        cout << arr[i];
    }
    
    return 0;
}
// */
// */ let n = Int(readLine()!)!; var puts = ""; for i in 0...n { puts += String(i, radix: 2); }; print(puts); // \u000a /*
#endif
/*
=end
# */