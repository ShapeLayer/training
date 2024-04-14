#include <stdio.h>
#include <time.h>

int main(void) {
  void split_time(long total_sec, int* hr, int* min, int* sec) {
    *sec = total_sec % 60;
    total_sec /= 60;
    *min = total_sec % 60;
    total_sec /= 60;
    *hr = total_sec % 60;
  }
  int hr, min, sec;
  split_time(time(NULL), &hr, &min, &sec);
  printf("Current UTC: %d시%d분%d초 입니다.\n", hr, min, sec);
  return 0;
}