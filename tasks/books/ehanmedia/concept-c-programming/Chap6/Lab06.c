/*
  P.58, Chapter 6.
*/

/* Lab6.c */
#include <stdio.h>

unsigned int make_rgb(unsigned int red, unsigned int green, unsigned blue); // 4 바이트 크기의 RGB 색상을 만드는 함수
unsigned int get_red(); // RGB 색상에서 red를 구하는 함수
unsigned int get_green(); // RGB 색상에서 green을 구하는 함수
unsigned int get_blue();// RGB 색상에서 blue를 구하는 함수

int main() {
  unsigned int r, g, b;
  unsigned int rgb;

  printf("red를 입력하세요(0~255) : ");
  scanf("%d", &r);

  printf("green를 입력하세요(0~255) : ");
  scanf("%d", &g);

  printf("blue를 입력하세요(0~255) : ");
  scanf("%d", &b);

  rgb = make_rgb(r, g, b);
  printf("RGB값 : %06x\n\n", rgb);

  printf("RGB 값을 16진수로 입력하세요 : ");
  scanf("%x", &rgb);

  printf("RGB 값 %06x 중 red   : %3d\n", rgb, get_red(rgb));
  printf("RGB 값 %06x 중 green : %3d\n", rgb, get_green(rgb));
  printf("RGB 값 %06x 중 blue  : %3d\n", rgb, get_blue(rgb));

  return 0;
}

unsigned int make_rgb(unsigned int red, unsigned int green, unsigned int blue) {
  return (red | (green << 8) | blue << 16);
}

unsigned int get_red(unsigned int rgb) {
  return (rgb & 0x0000ff);
}

unsigned int get_green(unsigned int rgb) {
  return (rgb & 0x00ff00) >> 8;
}

unsigned int get_blue(unsigned int rgb) {
  return (rgb & 0xff0000) >> 16;
}
