class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id
        self.__korean_quiz = 0
        self.__math_quiz = 0
        self.__science_quiz = 0
        self.__total_score = 0
    
    def __str__(self) -> str:
        return '''이름 : {name}, 학번: {id}
국어 성적 : {kr}, 수학 성적 : {mat}, 과학 성적 : {sci}
합계 : {sum}, 평균 : {avg}'''.format(
            name=self.get_name(), id=self.get_student_id(), kr=self.get_korean_quiz(), mat=self.get_math_quiz(), sci=self.get_science_quiz(), sum=self.get_total_score(), avg=self.get_avg_score()
        )

    def get_name(self) -> str:
        return self.name
    def get_student_id(self) -> int:
        return self.student_id
    def get_korean_quiz(self) -> int:
        return self.__korean_quiz
    def get_math_quiz(self) -> int:
        return self.__math_quiz
    def get_science_quiz(self) -> int:
        return self.__science_quiz
    def get_total_score(self) -> int:
        return self.__total_score
    def get_avg_score(self) -> float:
        return self.__total_score / 3

    def set_korean_quiz(self, score) -> None:
        self.__korean_quiz = score
        self.update_total_score()
    def set_math_quiz(self, score) -> None:
        self.__math_quiz = score
        self.update_total_score()
    def set_science_quiz(self, score) -> None:
        self.__science_quiz = score
        self.update_total_score()
    def update_total_score(self) -> None:
        self.__total_score = self.__korean_quiz + self.__math_quiz + self.__science_quiz

if __name__ == '__main__':
    name = input('학생의 이름을 입력하세요 : ')
    student_id = input('학생의 학번을 입력하세요 : ')
    
    student = Student(name, student_id)

    korean_quiz = int(input('학생의 국어 성적을 입력하세요 : '))
    math_quiz = int(input('학생의 수학 성적을 입력하세요 : '))
    science_quiz = int(input('학생의 과학 성적을 입력하세요 : '))
    student.set_korean_quiz(korean_quiz)
    student.set_math_quiz(math_quiz)
    student.set_science_quiz(science_quiz)
    print(student)