nasm -f elf64 -o $1.o $1.asm && gcc -o $1.bin $1.o
rm $1.o
