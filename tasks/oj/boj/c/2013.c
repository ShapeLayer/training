#include <stdio.h>

int parents[10001];
int is_root[10001];

int find(int n) {
  if (parents[n] == n) { return n; }
  return find(parents[n]);
}

void merge(int a, int b) {
  int pa = find(a), pb = find(b);
  if (a < b) {
    parents[b] = pa;
    parents[pb] = pa;
    is_root[b] = 0;
    is_root[pb] = 0;
  } else if (a > b) {
    parents[a] = pb;
    parents[pa] = pb;
    is_root[a] = 0;
    is_root[pa] = 0;
  }
}

int ccw(double ax, double ay, double bx, double by, double cx, double cy) {
  double op = (ax*by + bx*cy + cx*ay) - (ax*cy + bx*ay + cx*by);
  if (op > 0) return 1;
  else if (op < 0) return -1;
  return 0;
}

void swap(double *a, double *b) {
  int temp = *a;
  *a = *b;
  *b = temp;
}

int is_intersect(double ax, double ay, double bx, double by, double cx, double cy, double dx, double dy) {
  int ab = ccw(ax, ay, bx, by, cx, cy) * ccw(ax, ay, bx, by, dx, dy);
  int cd = ccw(cx, cy, dx, dy, ax, ay) * ccw(cx, cy, dx, dy, bx, by);
  if (ab == 0 && cd == 0) {
    if (ax > bx) { swap(&ax, &bx); swap(&ay, &by); }
    else if (ax == bx && ay > by) { swap(&ax, &bx); swap(&ay, &by); }
    if (cx > dx) { swap(&cx, &dx); swap(&cy, &dy); }
    else if (cx == dx && cy > dy) { swap(&cx, &dx); swap(&cy, &dy); }
    return cx <= bx && ax <= dx;
  }
  return ab <= 0 && cd <= 0;
}

int main() {
  int n;
  scanf("%d", &n);
  for (int i = 0; i < 10001; i++) is_root[i] = 1; // init
  double gets[10001][4];
  for (int i = 1; i <= n; i++) {
    scanf("%lf %lf %lf %lf", &gets[i-1][0], &gets[i-1][1], &gets[i-1][2], &gets[i-1][3]);
    for (int j = 1; j < i; j++) {
      if (is_root[i] && i != j) {
        if (is_intersect(gets[j-1][0], gets[j-1][1], gets[j-1][2], gets[j-1][3], gets[i-1][0], gets[i-1][1], gets[i-1][2], gets[i-1][3])) {
          merge(i, j);
        }
      }
    }
  }
  int counts = 0;
  for (int i = 1; i < n+1; i++) {
    if (is_root[i]) counts++;
  }
  printf("%d\n", counts);
  return 0;
}