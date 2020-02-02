coffee = int(input("커피 양?:"))
money =int(input("돈?:"))

while True: #무한 루프
    print("돈 받았으니까 커피 준다")
    coffee -=1
    money -=1
    
    print("남은 커피 양 {}, 남은 돈 {}".format(coffee, money))
    if not coffee and not money: #if coffee == 0 and money == 0
        print("동시에 떨어짐")
        break 
    
    elif not coffee:
        print("커피 없음")
        break
     
    elif not money:
        print("돈이 다 떨어짐")
        break
      
# break가 없으면 무한반복이라 끝나지 않음
