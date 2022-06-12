#ifndef _STR_H_
#define _STR_H_
#include "limits.h" /* for MAX_STR_LEN */
#include <unistd.h> /* for typedef of size_t */
size_t StrGetLength(const char* pcSrc);
char *StrToLower(char *str);
#endif /* _STR_H_ */