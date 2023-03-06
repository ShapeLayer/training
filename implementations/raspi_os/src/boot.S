#include "mm.h"

.section "text.boot"

.globl _start
_start:
  mrs x0, mpidr_el1
  and x0, x0, #0xFF
  cbz x0, master
  b proc_hang

master:
  adr x0, bss_begin
