#김왼손의 파이썬 예제 뽀개기 no.2
#텍스트를 입력하면 첫글자는 대문자로,
#마지막에 마침표가 없으면 마침표를 붙여주고, 있으면 그대로 출력하는
#함수 correct_sentence 만들기

def correct_sentence(text: str) -> str:
    text = text[0].upper() + text[1:]

    if not text.endswith('.'):
        text += '.'

    return text    


