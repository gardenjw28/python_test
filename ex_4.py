#김왼손의 파이썬 예제 뽀개기 no.4
#문자열에서 쉼표 뒤 입력된 문자열의 2번째 index 값을 출력하는 것

def second_index(text: str, symbol: str):
    
    #만약 symbol의 갯수가 2개 미만이면 2번째 index값이 없으니까 None으로 출력
    if text.count(symbol) < 2:
        return 'None'
    
    #text에서 symbol을 찾아서 그 index값을 first에 할당
    first = text.find(symbol)
    
    #text에서 symbol을 찾는데 first에 +1을 해서 여기서부터 symbol의 index값을 찾아서 return
    return print("두번째 index값:", text.find(symbol, first + 1))
