#include <stdio.h>

struct person
{
  char name[20];
  char gender;
  int job_code;
  union { // 공용체
    char company_name[20];
    char school_name[20];
  } job_info;
};
