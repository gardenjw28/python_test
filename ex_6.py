# 김왼손의 파이썬 예제 뽀개기 no.6
# 주식의 이름과 가격이 저장되어있는 딕셔너리에서 가격이 가장 높은 주식 문자열로 출력
# 딕셔너리는 키와 값의 쌍으로 이루어져있다. {} 사용

def best_stock(data):
    max_price = 0
    answer = ''

    for s in data:  #data에서 키를 가져와서 s에 차례로 넣어서 실행
        if data[s] > max_price:  #data[s]는 키의 이름이 s인 값
            max_price = data[s]
            answer = s

        return answer
