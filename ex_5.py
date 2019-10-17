#김왼손의 파이썬 예제 뽀개기 no.5
#문자열에서 구분자 2개 사이의 값 출력하기
#len(): 문자열 길이 구하기

def between_markers(text: str, begin: str, end: str):
    
    if begin in text:

        #begin자리 + begin의 길이를 해야만 완전히 begin 이후의 값을 읽을 수 있음
        begin_index = text.find(begin) + len(begin)
        
    else:
        begin_index = 0 #첫번째 문자부터 출력하면 되니까 


    if end in text:
        end_index = text.find(end) #end 뒤로는 상관없으므로
    else:
        end_index = len(text) #text의 길이를 index로 두면 아무 값도 index에 할당되지  않음


    return text[begin_index:end_index] 
