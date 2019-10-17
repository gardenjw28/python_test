#김왼손의 파이썬 예제 뽀개기 no.4
#문자열에서 쉼표 뒤 입력된 문자열의 2번째 index 값을 출력하는 것

def second_index(text: str, symbol: str):
    if text.count(symbol) < 2:
        return 'None'

    first = text.find(symbol)

    return print("두번째 index값:", text.find(symbol, first + 1))
