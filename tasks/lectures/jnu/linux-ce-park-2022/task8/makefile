sgrep: sgrep.o str.o
	gcc -g -o sgrep sgrep.o str.o
sgrep.o: sgrep.c str.c str.h limits.h
	gcc -c sgrep.c
str.o: str.c str.h limits.h
	gcc -c str.c
