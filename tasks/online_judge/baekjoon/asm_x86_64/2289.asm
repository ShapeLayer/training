section .text
global main
main:
  mov rax, 1
  mov rdi, 1
  mov rsi, msg
  mov rdx, msglen
  syscall

  mov rax, 0x0
  ret

section .rodata
  msg: db "<(o )___", 10, " ( \_> /", 10, "  ", 34 , "~~~", 34, 10
  msglen: equ $ - msg
