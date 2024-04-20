#include <pthread.h> // pthread lib
#include <stdio.h>
#include <stdlib.h>
int gsum = 0;
int __thread tsum = 1;
void func(int a)
{
  printf("5_%d. gsum= %d / tsum= %d \n", a, gsum, tsum);
  int b = a + 10;
  gsum += b;
  tsum += b;
  printf("6_%d. gsum= %d / tsum= %d \n", a, gsum, tsum);
}
void *myThread(void *p)
{
  int a = (*(int *)p);
  printf("2_%d. gsum= %d / tsum= %d \n", a, gsum, tsum);
  for (int i = 0; i < 30000000 / a; i++)
    ;
  gsum += a;
  tsum += a;
  printf("3_%d. gsum= %d / tsum= %d \n", a, gsum, tsum);

  func(a);
  printf("7_%d. gsum= %d / tsum= %d \n", a, gsum, tsum);
}
int main()
{
  pthread_t tid[2];
  int arg[2] = {1000, 3000};
  printf("1_main. gsum= %d / tsum= %d \n", gsum, tsum);
  pthread_create(&tid[0], NULL, myThread, &arg[0]);
  pthread_create(&tid[1], NULL, myThread, &arg[1]);
  pthread_join(tid[0], NULL);
  pthread_join(tid[1], NULL);
  printf("8_main. gsum= %d / tsum= %d \n", gsum, tsum);
  return 0;
}
