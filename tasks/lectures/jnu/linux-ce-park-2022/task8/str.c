#include <assert.h> /* to use assert() */
#include <stdio.h>
#include <string.h>
#include "str.h" #include <ctype.h>

/* Your task is:
Rewrite the body of "Part 1" functions - remove the current body that simply calls the corresponding C
standard library function. */
/*------------------------------------------------------------------------*/
size_t StrGetLength(const char* pcSrc)
{
  const char *pcEnd;
  assert(pcSrc); /* NULL address, 0, and FALSE are identical. */
  pcEnd = pcSrc;
  while (*pcEnd) /* null character and FALSE are identical. */
  pcEnd++; 
  return (size_t)(pcEnd - pcSrc);
}
/*------------------------------------------------------------------------*/
char *StrToLower(char *str)
{
  char *str_clone;
  str_clone = (char *)malloc(1024);
  int count=0;
  /* TODO: fill this function */
  /* Part 1 */
}