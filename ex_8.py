# 김왼손의 파이썬 예제 뽀개기 no.8 Bigger price
# 가장 비싼 물건 찾기, (알고싶은 상품의 갯수, 전체 데이터)
# 데이터는 2개의 key: name과 price -> dict
# 출력은 테이터와 같은 형태

def bigger_price(n: int, data: list) -> dict :
    return sorted(data, key = lambda x: x['price'], reverse = True)[:n]

# sorted로 data를 정렬하는데 정렬의 기준(key)은 price이고
# reverse=True를 사용해서 내림차순으로 정렬해서 n전까지 출력하면 n개를 출력 
    
