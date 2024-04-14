#include <stdio.h>

int main(void){
    float meter = 1; float inch = 39.370079; float ft = 3.28084; float yd = 1.093613;

    int select_1; int select_2;
    printf("다음 단위에서 [변환할 단위] --> [변환결과 단위]로 연산합니다.\n");
    printf(" [1] 미터(m)  [2] 인치(in)  [3] 피트(ft)  [4] 야드(yd)  [0] 종료(stop)\n");
    printf("[이전단위] --> [변환단위], 두 개의 메뉴 번호를 선택하세요. >> ");
    scanf("%d %d", &select_1, &select_2);
    while (true) {
        float val;
        printf("[변환할 단위]의 길이를 입력하세요. >> ");
        scanf("%f", &val);
        if (val == 0) {
            printf("종료합니다.\n");
            break;
        } else {
            if (select_1 == 1) {
                if (select_2 == 2) printf(" [결과] %.2f (미터) --> %.2f (인치)\n", val, val*inch/meter);
                else if (select_2 == 3) printf(" [결과] %.2f (미터) --> %.2f (피트)\n", val, val*ft/meter);
                else if (select_2 == 4) printf(" [결과] %.2f (미터) --> %.2f (야드)\n", val, val*yd/meter);
            }
            else if (select_1 == 2) {
                if (select_2 == 1) printf(" [결과] %.2f (인치) --> %.2f (미터)\n", val, val*meter/inch);
                else if (select_2 == 3) printf(" [결과] %.2f (인치) --> %.2f (피트)\n", val, val*ft/inch);
                else if (select_2 == 4) printf(" [결과] %.2f (인치) --> %.2f (야드)\n", val, val*yd/inch);
            }
            else if (select_1 == 3) {
                if (select_2 == 1) printf(" [결과] %.2f (피트) --> %.2f (미터)\n", val, val*meter/ft);
                else if (select_2 == 2) printf(" [결과] %.2f (피트) --> %.2f (인치)\n", val, val*inch/ft);
                else if (select_2 == 4) printf(" [결과] %.2f (피트) --> %.2f (야드)\n", val, val*yd/ft);
            }
            else if (select_1 == 4) {
                if (select_2 == 1) printf(" [결과] %.2f (야드) --> %.2f (미터)\n", val, val*meter/yd);
                else if (select_2 == 2) printf(" [결과] %.2f (야드) --> %.2f (인치)\n", val, val*inch/yd);
                else if (select_2 == 3) printf(" [결과] %.2f (야드) --> %.2f (피트)\n", val, val*ft/yd);
            }
        }
    }
    return 0;
}