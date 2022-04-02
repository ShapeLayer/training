//; # \u000a import java.util.Scanner; /*
//; # \u000a public class Main { /*
//; # \u000a   public static void main(String[] args) { /*
//; # \u000a     Scanner sc = new Scanner(System.in); /*
//; # \u000a     int n = sc.nextInt(); /*
//; # \u000a     String puts = ""; /*
//; # \u000a     for (int i = 0; i <= n; i++) { /*
//; # \u000a       puts += Integer.toBinaryString(i); /*
//; # \u000a     } /*
//; # \u000a     System.out.println(puts); /*
//; # \u000a   } /*
//; # \u000a } /*
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
// */ swift_code // \u000a /*
#endif
/*
=end
# */