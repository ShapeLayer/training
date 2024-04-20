#include <thread> // thread lib.
#include <stdio.h>
#include <stdlib.h>
void func1()
{
  for (int i = 0; i < 100; i++)
    printf("I am thread 1");
}
void func2()
{
  for (int i = 0; i < 100; i++)
    printf("I am thread 2");
}
void func3()
{
  for (int i = 0; i < 100; i++)
    printf("I am thread 3");
}
int main()
{
  thread t1(func1);
  thread t2(func2);
  thread t3(func3);
  t1.join();
  t2.join();
  t3.join();
}