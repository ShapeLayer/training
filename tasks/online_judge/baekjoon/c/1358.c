#include <stdio.h>
#include <math.h>

double get_distance(double x, double y, double a, double b) {
  return sqrt(pow(x-a, 2) + pow(y-b, 2));
}

int main() {
  int w, h, x, y, p;
  scanf("%d %d %d %d %d", &w, &h, &x, &y, &p);
  int getsx, getsy, counts = 0;
  for (int i = 0; i < p; i++) {
    scanf("%d %d", &getsx, &getsy);
    if ((x <= getsx && y <= getsy) && (x+w >= getsx && y+h >= getsy)) counts++;
    else if (x >= getsx && h/2 >= get_distance(x, y+h/2, getsx, getsy)) counts++;
    else if (x+w <= getsx && h/2 >= get_distance(x+w, y+h/2, getsx, getsy)) counts++;
  }
  printf("%d\n", counts);
}
