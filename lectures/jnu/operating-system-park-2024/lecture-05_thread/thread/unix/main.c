#include <pthread.h> // pthread lib
#include <stdio.h>
#include <stdlib.h>
int sum = 0; // global variable
void *myThread1(void *p)
{ // for the thread 1
  printf("\t myThread 1 starts\n");

  int *i = (int *)malloc(sizeof(int));
  for (i = 0; i < (*(int *)p); i++)
    sum += 1;
  return (void *)i;
}
void *myThread2(void *p)
{ // for the thread 2
  printf("\t myThread 2 starts \n");

  int *i = (int *)malloc(sizeof(int));
  for (i = 0; i < (*(int *)p); i++)
    sum -= 1;
  return (void *)i;
}
int main()
{
  pthread_t tid1, tid2; // thread id
  int count = 200000;
  int *ret1, *ret2;

  // create thread (id, attribute, function_pointer, argument)
  pthread_create(&tid1, NULL, myThread1, &count);
  printf("myThread1's tid: %0X \n", (int)tid1);
  pthread_create(&tid2, NULL, myThread2, &count);
  printf("myThread2's tid: %0X \n", (int)tid2);

  pthread_join(tid1, (void **)&ret1); // waiting for 'tid1'
  pthread_join(tid2, (void **)&ret2); // waiting for 'tid2'

  printf("myThreads have been finished \n");
  printf("sum = %d\n", sum);
  printf("ret1 = %d\n", (int)ret1);
  printf("ret2 = %d\n", (int)ret2);
  return 0;
}
