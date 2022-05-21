/*
  P.124, Chapter 11.
*/

/* Lab11.c */
int main() {
  int n, m;
  int **arr; // 배열을 담을 포인터들의 배열이 필요하니 이중포인터 사용
  int i, j, k;

  printf("배열의 제1크기와 제2크기를 입력하세요 : ");
  scanf("%d %d", &n, &m);
  
  arr = (int**) malloc(sizeof(int)*n);
  for (i = 0; i < n; i++) {
    arr[i] = (int*) malloc(sizeof(int)*m);
  }

  k = 1;
  for (i = 0; i < n; i++)
    for (j = 0; j < m; j++)
      arr[i][j] = k++;

  printf("<%d x %d 크기의 배열>\n", n, m);
  for (i = 0; i < n; i++) {
    for (j = 0; j < m; j++)
      printf("%3d ", arr[i][j]);
    printf("\n");
  }

  for (i = 0; i < n; i++) {
    free(arr[i]);
  }
  free(arr);

  return 0;
}
