#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define NAME_LIM 100

typedef struct MOVIE Movie;
void print_movie_array(Movie* arr);
int cmp_name(const void *a, const void *b);
int cmp_pro_rate(const void *a, const void *b);
int cmp_user_rate(const void *a, const void *b);


typedef struct MOVIE {
  char name[NAME_LIM];
  double pro_rate;
  double user_rate;
} Movie;

int main() {
  Movie rates[] = {
    { "범죄도시", 6.00, 9.15 },
    { "명량", 6.29, 8.44 },
    { "마녀", 5.63, 8.22 },
    { "7번방의선물", 6.58, 8.83 },
    { "올드보이", 8.50, 9.03 }
  };

  
  printf("--- 정렬 전 ---\n");
  print_movie_array(rates);
  printf("\n");

  qsort(rates, 5, sizeof(*rates), cmp_name);
  printf("--- 이름 순 정렬 ---\n");
  print_movie_array(rates);
  printf("\n");

  qsort(rates, 5, sizeof(*rates), cmp_pro_rate);
  printf("--- 전문가 평점 순 정렬 ---\n");
  print_movie_array(rates);
  printf("\n");

  qsort(rates, 5, sizeof(*rates), cmp_user_rate);
  printf("--- 네티즌 평점 순 정렬 ---\n");
  print_movie_array(rates);
  printf("\n");

  return 0;
}

void print_movie_array(Movie* arr) {
  for (int i = 0; i < 5; i++) {
    printf("%-20s \t 전문가: %.2lf 네티즌: %.2lf \n", arr[i].name, arr[i].pro_rate, arr[i].user_rate);
  }
}

int cmp_name(const void *a, const void *b) { 
  Movie x = *(Movie *)a;
  Movie y = *(Movie *)b;
  return strcmp(x.name, y.name);
}
int cmp_pro_rate(const void *a, const void *b) {
  Movie x = *(Movie *)a;
  Movie y = *(Movie *)b;
  if (x.pro_rate > y.pro_rate) return 1;
  else if (x.pro_rate < y.pro_rate) return -1;
  return 0;
}
int cmp_user_rate(const void *a, const void *b){
  Movie x = *(Movie *)a;
  Movie y = *(Movie *)b;
  if (x.user_rate > y.user_rate) return 1;
  else if (x.user_rate < y.user_rate) return -1;
  return 0;
}
