def main():
    print("Amount Due: 50")
    x = int(input("Insert Coin: "))
    calcCoin(x)

def calcCoin(money):
    while money < 50 :
        print("Amount Due: ", 50 - money)
        coin = int(input("Insert Coin: "))
        money = money + coin 
        if money < 50:
            continue
        elif money >= 50 :
            print ("Change Owed=", money - 50)
            break
        else :
            break

main()