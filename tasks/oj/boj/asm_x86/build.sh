nasm -f elf32 -o $1.o $1.asm && gcc -m32 -o $1.bin $1.o
rm $1.o
