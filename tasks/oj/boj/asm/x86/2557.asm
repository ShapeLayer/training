section .text:
global main
main:
  mov eax, 0x4
  mov ebx, 1
  mov ecx, msg
  mov edx, msg_len
  int 0x80

  mov eax, 0x1
  mov ebx, 0
  int 0x80

  ret

section .data:
  msg: db "Hello World!", 0xa
  msg_len: equ $-msg