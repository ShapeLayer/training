#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define ARRAY_SIZE 10
#define swap(a, b) int c = a; a = b; b = c

void sort(int* arr, int size);

int main(void) {
	FILE* fp = fopen("before.txt", "r");
	if (fp == NULL) return EXIT_FAILURE;
	int arr[ARRAY_SIZE] = { 0 };
	for (int i = 0; i < ARRAY_SIZE; i++) {
		fscanf(fp, "%d", &arr[i]);
	}
	fclose(fp);
	sort(arr, ARRAY_SIZE);
	fp = fopen("after.txt", "w");
	for (int i = 0; i < ARRAY_SIZE; i++) {
		fprintf(fp, "%d ", arr[i]);
	}
	fclose(fp);
	return 0;
}

void sort(int* arr, int size) {
	for (int i = 0; i < size - 1; i++) {
		for (int j = i + 1; j < size; j++) {
			if (arr[i] % 10 == arr[j] / 10) {
				swap(arr[i + 1], arr[j]);
				break;
			}
		}
	}
}
