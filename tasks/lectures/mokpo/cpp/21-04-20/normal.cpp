#include <stdio.h>

int main(void){
    /* vault, display 배열에 차례대로 미터, 인치, 피트, 야드에 대한 정보 넣음
       vault에는 미터를 1로 잡았을 때 변환 비율을 기록함
       display에는 각 단위의 명칭을 기록함
       display 뒤에 [4][7]가 붙은 이유는 한글 두글자를 처리할 때 영어 7글자만큼의 용량을 소비하기 때문임 (유니코드)
    */
    float vault[4] = {1, 39.370079, 3.28084, 1.093613};
    char display[4][7] = {"미터", "인치", "피트", "야드"};

    /* select 배열은 나중에 변환할 단위와 변환결과 단위 정보를 넣을 것임
    */
    int select[2];

    /* 화면에 보일 내용 출력
    */
    printf("다음 단위에서 [변환할 단위] --> [변환결과 단위]로 연산합니다.\n");
    printf(" [1] 미터(m)  [2] 인치(in)  [3] 피트(ft)  [4] 야드(yd)  [0] 종료(stop)\n");
    printf("[이전단위] --> [변환단위], 두 개의 메뉴 번호를 선택하세요. >> "); // \n을 하지 않아 이 뒤로 커서가 멈춤
    
    /* scanf에 "%d %d"한 이유는 두 값을 입력받기 때문: scanf()에 처음으로 들어가는 값은 문서 양식처럼 생각하면 됨
       "%d %d" 로 설정되어 있기 때문에 "1 2"와 같은 형태로만 입력해야함
       "%d, %d"로 설정되어 있었다면 "1, 2"와 같은 형태로만 입력해야 했을것임
    */
    scanf("%d %d", &select[0], &select[1]);
    
    /* 계산은 0을 받을때까지 계속해서 돌기 때문에 while () 조건을 참으로 만들어 무한 루프를 만듬
       while (조건) {(code)}
    */
    while (true) {

        /* val 변수에 변환할 길이를 입력하게 할 것
        */
        float val;
        printf("[변환할 단위]의 길이를 입력하세요. >> ");
        scanf("%f", &val);

        /* 만약 변환할 길이(입력받은 값)가 0이라면 프로그램을 종료해야함
        */
        if (val == 0) {
            printf("종료합니다.\n");

            /* break을 사용하여 무한루프를 빠져나가면 남은 코드는 return 0밖에 없으므로 프로그램이 종료됨.
            */
            break;
        } else {
            /* 결과의 계산은 (입력값)*(변환결과 단위)/(변환할 단위)임
               입력값 = val
               변환결과 단위 = vault[select[1]-1]
               변환할 단위 = vault[select[0]-1]

               select[n]-1을 vault 인덱싱에 넣은 이유?
               select[0], select[1]은 각각 변환할 단위와 변환결과 단위를 지정한 것임
               1.미터 2.인치 3.피트 4.야드
               변환할 단위가 1.미터라면 select[0]에는 1이 들어감
               그럼 vault에서 첫번째 변환 비율을 가져오면 되지만, 컴퓨터는 수를 1이 아닌 0부터 셈
               따라서 select[n]-1 은 입력이 1일때 0으로 바꿔줄 수 있음
               select[0] = 1일 때 select[0]-1을 vault를 통하면 미터 변환 비율로 만드는 효과를 볼 수 있음.

               printf() 사용 중 display[select[0]-1], display[select[1]-1] 역시 같은 맥락에서 이렇게 짠 것임
            */
            float result = val*vault[select[1]-1]/vault[select[0]-1];
            printf(" [결과] %.2f (%s) --> %.2f (%s)\n", val, display[select[0]-1], result, display[select[1]-1]);
        }
    }
    return 0;
}