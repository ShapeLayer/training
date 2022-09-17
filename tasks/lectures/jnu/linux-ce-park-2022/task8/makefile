cc = gcc

sgrep: sgrep.o str.o
	$(cc) -g -o sgrep sgrep.o str.o
sgrep.o: sgrep.c str.c str.h limits.h
	$(cc) -c sgrep.c
str.o: str.c str.h limits.h
	$(cc) -c str.c
