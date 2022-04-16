import random 
num = 1, 2, 3, 4, 5, 6, 7, 8, 9, 10


def player():
    tot = 0
    totdealer = 0
    while True:
        question = input('Do you want a card? Write "yes" or "no": ')
        if question == 'yes' and tot <= 21:
            card = random.choice(num)
            if card == 1:
                card = int(input('Do you want it as 1 or 11?: '))
            print('This is your card', card) 
            tot = tot + card 
            print('Your total is', tot) 
            if tot == 21:
                print('You won')
                quit()
            if tot > 21:
                print('You lost')
                quit()
        if question == 'no' and tot == 0:
            print('Goodbye') 
        if question != 'yes' and question != 'no':
            print('Please enter a valid option')
            continue 
        if  question == 'no' and tot > 0:
            break

    print('Now the dealer starts')
    while True:
        dealercard = random.choice(num)
        print('The dealer card is', dealercard)
        totdealer = totdealer + dealercard
        print('The dealer has', totdealer)
        if totdealer > tot and totdealer <= 21:
            print('The dealer won')
            break
        if totdealer > 21:
            print('You won')
            break 

            
player() 
