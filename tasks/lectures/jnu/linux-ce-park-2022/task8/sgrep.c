#include <stdio.h>
#include <stdlib.h>
#include <string.h> /* for skeleton code */
#include <unistd.h> /* for getopt */
#include "str.h"
#define FALSE 0
#define TRUE 1
/*
* Fill out your own functions here (If you need)
*/
/*--------------------------------------------------------------------*/
/* PrintUsage()
print out the usage of the Simple Grep Program */
/*--------------------------------------------------------------------*/
void PrintUsage(const char* argv0)
{
  const static char *fmt =
    "Simple match (match) Usage:\n"
    "%s pattern \n";
  printf(fmt, argv0);
}

/*-------------------------------------------------------------------*/
/* SearchPattern()
Your task:
1. Do argument and input string validation - String or file argument length is no more than 1023 - If you encounter an input argument that's too long, print out "Error: pattern is too long"
2. Read the each line from input file(infile) - If you encounter a line larger than 1023 bytes, print out "Error: input line is too long" - Error message should be printed out to standard error (stderr)
3. Check & print out the line contains a given string (search-string)
Tips: - fgets() is an useful function to read characters from file. Note
that the fget() reads until newline or the end-of-file is reached. - fprintf(sderr, ...) should be useful for printing out error
message to standard error
NOTE: If there is any problem, return FALSE; if not, return TRUE */
/*-------------------------------------------------------------------*/
int SearchPattern(const char *pattern)
{
  char buf[MAX_STR_LEN + 2];
  FILE *fp;
  if( (fp = fopen("infile", "r")) == NULL) {
    fprintf(stderr, "Error: file open error\n");
    return(EXIT_FAILURE);
  }
  /*
  * TODO: check if pattern is too long and there exists
  */
  
  int lines = 0;
  int matched = 0;
  while (fgets(buf, MAX_STR_LEN + 2, fp) != NULL) {
    char *lowered = StrToLower(buf);
    lines++;
    for (int i = 0; i < StrGetLength(lowered) - StrGetLength(pattern); i++) {
      int flag = 0;
      for (int j = 0; j < StrGetLength(pattern); j++) {
        if (lowered[i+j] != pattern[j]) {
          flag = 0;
          break;
        } else {
          flag = 1;
        }
      }
      if (flag) {
        matched = 1;
        printf("(ln %d, pos %d) %s", lines, i+1, buf);
        if (buf[StrGetLength(buf)-1] != '\n') printf("\n");
      }
    }
  }
  if (!matched) {
    fprintf(stderr, "No pattern\n");
    return FALSE;
  }
  return TRUE;
  
}

/*-------------------------------------------------------------------*/
int main(const int argc, const char *argv[])
{
  /* Do argument check and parsing */
  if (argc <= 1) {
    fprintf(stderr, "Error: argument parsing error\n");
    PrintUsage(argv[0]);
    return EXIT_FAILURE;
  }
  if (StrGetLength(argv[1]) > MAX_STR_LEN) {
    fprintf(stderr, "Too long\n");
    return EXIT_FAILURE;
  }
  return SearchPattern(StrToLower(argv[1])) ? EXIT_SUCCESS : EXIT_FAILURE;
}
