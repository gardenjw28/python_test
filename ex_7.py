# 김왼손의 파이썬 예제 뽀개기 no.7
# 특정단어가 얼마나 많이 나오는지
# 함수에는 텍스트, 찾을 단어의 리스트
# 대소구분하지 않음, 찾을 단어는 항상 소문자, 못찾으면 0으로 출력,
# 딕셔너리로 출력, 찾을 단어: key, 반복 횟수: value


def popular_words(text: str, words: list) -> dict:
    text = text.lower()  #소문자로 다 바꾸기
    split_text = text.split()  #문장을 공백 기준을 나누기, list로 출력됨.
    answer = {}  #dict로 출력해야하므로, 값이 없다면 0으로 출력

    for w in words:  #찾을 단어 하나씩 가져와서 w에 할당
        answer[w] = split_text.count(w)  #찾을 단어: key이고 단어의 횟수: value로 answer에 할당

    return answer
