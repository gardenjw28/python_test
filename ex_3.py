#김왼손의 파이썬 예제 뽀개기 no.3
#텍스트의 첫 단어 출력하기
#단어는 ' '와 ',', '.'로 구분되어 있다

def first_word(text: str):
    
    #replace()를 사용해서 ,와 .를 공백으로 대체
    #strip()을 사용하여 문자열 양쪽 끝 공백과 \n 제거
    text = text.replace('.', ' ').replace(',', ' ').strip()

    #split()을 사용하여 문자를 공백 단위로 나누어서 list형식으로 저장
    #만일 split(',', 3)이라고 하면 ','단위로 나누고 분리되는 갯수는 3개
    text = text.split()
    
    return text[0]
