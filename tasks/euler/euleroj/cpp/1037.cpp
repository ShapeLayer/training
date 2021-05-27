#include <cstdio>

int main(void) {
  int s, t;
  int s1, s2, s3, s4;
  int t1, t2, t3, t4;

  scanf("%d %d %d %d", &s1, &s2, &s3, &s4);
  scanf("%d %d %d %d", &t1, &t2, &t3, &t4);
  t = t1 + t2 + t3 + t4;
  s = s1 + s2 + s3 + s4;
  if (s > t) printf("%d", s);
  else printf("%d", t);

  return 0;
}
