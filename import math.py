print(" ")
print("Tic-Tac-Toe")
print(" ")


player1 = "X"
player2 = "O"



number1 = 1
number2 = 2
number3 = 3
number4 = 4
number5 = 5
number6 = 6
number7 = 7
number8 = 8
number9 = 9



def hra():
    print(" ")
    print(f"{number1} | {number2} | {number3}")
    print(f"{number4} | {number5} | {number6}")
    print(f"{number7} | {number8} | {number9}")


trun = 0
r = 0
win = 0

while win == 0 :
        
    
    r = 0
    trun = player1

    if win == 0:
        while r== 0:
            hra()
            
            select =int(input("Select the box(X): "))
            r = 0
            if select == number1 or number2 or number3 or number4 or number5 or number6 or number7 or number8 or number9:
                if select == number1:
                    number1 = trun
                    r =1
                elif select == number2:
                    number2 =trun
                    r =1
                elif select == number3:
                    number3 =trun
                    r =1
                elif select == number4:
                    number4 =trun
                    r =1
                elif select == number5:
                    number5 =trun
                    r =1
                elif select == number6:
                    number6 =trun
                    r =1
                elif select == number7:
                    number7 =trun
                    r =1
                elif select == number8:
                    number8 =trun
                    r =1
                elif select == number9:
                    number9 =trun
                    r =1
                else:
                    print(" ")
                    print("select the UNSELECTED box")
                if win == 0:
                    if number1 == number2 == number3 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number4 == number5 == number6 ==player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number7 == number8 == number9 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number4 == number7 ==player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number2 == number5 == number8 ==player1:
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number6 == number9 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number5 == number9 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number5 == number7 ==player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number2 == number3 == player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number4 == number5 == number6 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number7 == number8 == number9 == player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number4 == number7 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number2 == number5 == number8 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number6 == number9 ==  player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number5 == number9 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number5 == number7 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
              

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    trun = player2
    print(" ")
    r = 0
    if win == 0:
        while r== 0:
            hra()
            
            select =int(input("Select the box(X): "))
            r = 0
            if select == number1 or number2 or number3 or number4 or number5 or number6 or number7 or number8 or number9:
                
                if select == number1:
                    number1 = trun
                    r =1
                elif select == number2:
                    number2 =trun
                    r =1
                elif select == number3:
                    number3 =trun
                    r =1
                elif select == number4:
                    number4 =trun
                    r =1
                elif select == number5:
                    number5 =trun
                    r =1
                elif select == number6:
                    number6 =trun
                    r =1
                elif select == number7:
                    number7 =trun
                    r =1
                elif select == number8:
                    number8 =trun
                    r =1
                elif select == number9:
                    number9 =trun
                    r =1
                else:
                    print(" ")
                    print("select the UNSELECTED box")
                if win == 0:
                    if number1 == number2 == number3 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number4 == number5 == number6 ==player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number7 == number8 == number9 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number4 == number7 ==player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number2 == number5 == number8 ==player1:
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number6 == number9 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number5 == number9 == player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number5 == number7 ==player1 :
                        print(f"🎉🎊🎉{player1} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number2 == number3 == player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number4 == number5 == number6 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number7 == number8 == number9 == player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number4 == number7 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number2 == number5 == number8 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number6 == number9 ==  player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number1 == number5 == number9 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1
                    elif number3 == number5 == number7 ==player2:
                        print(f"🎉🎊🎉{player2} win🎉🎊🎉")
                        hra()
                        win = 1