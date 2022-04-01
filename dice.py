from random import randint

def game():

    #  Rules of the game
    print("Welcome the the dice game. All the dices must have the same value in a maximum of 3 rounds. You can rethrow 2 times per round.")

    # While you don't insert 'GO', the game will not start
    print("Insert 'GO' to start.")

    start_game = input()

    while start_game != "GO" :
        print("Insert 'GO' to start.")
        start_game = input()
    
    print("Let the game begin : ")

    # A variable calls three functions that chose random values for the three dices
    throw = throw_first_dice(), throw_second_dice(),throw_third_dice()
    print('\n',throw)

    # If all the dices have the same value, you win
    if first_dice == second_dice == third_dice : 
        print("All the dices have the same value, you win !")
        return 
    
    # If two or all the dices have different values, a function is called
    elif first_dice != second_dice != third_dice  or first_dice != second_dice or first_dice != third_dice:
        rethrow()


def rethrow ():
    global new_dice

    # This condition is placed within the loop in case all the dices have the same value during the loop 
    for i in range(2):

        if first_dice == second_dice == third_dice : 
            print("All the dices have the same value, you win !")
            return

        # You have the chose which dice you want to throw. If all the values are not identical, you have to chose or a second time
        else : 
            print("Which dice do you want to throw again ? 1, 2 or 3 ?")
            rethrow_dice = int(input())

            while rethrow_dice < 0 or rethrow_dice > 3:
                print("Please enter 1, 2 or 3")
                rethrow_dice = int(input())

            if rethrow_dice == 1 :
                new_dice = throw_first_dice()
                print('\n',"New value :",new_dice,second_dice,third_dice)
    
            elif rethrow_dice == 2 :
                new_dice = throw_second_dice()
                print('\n',"New value :",first_dice,new_dice,third_dice)
    
            elif rethrow_dice == 3 :
                new_dice = throw_third_dice()
                print('\n',"New value :",first_dice,second_dice,new_dice)

    print('\n',"End of the first round.",'\n') 

    # If all the values are not identical, another function is called to play the second round which is basically the same function as the one above
    second_rethrow()
    
def second_rethrow ():
    global new_dice

    print("Second round !")

    print("Insert 'GO' to start.")   
    start_game = input()

    while start_game != "GO" :
        print("Insert 'GO' to start.")
        start_game = input()
    
    
    for i in range(2):
        if first_dice == second_dice == third_dice : 
            print("All the dices have the same value, you win !")
            return

        else :
            print('\n',"Which dice do you want to throw again ? 1, 2 or 3 ?")
            rethrow_dice = int(input())

            
            while rethrow_dice < 0 and rethrow_dice > 3:
                print("Please enter 1, 2 or 3")
                rethrow_dice = int(input())
                
            if rethrow_dice == 1 :
                new_dice = throw_first_dice()
                print('\n',"New value :",new_dice,second_dice,third_dice)
    
            elif rethrow_dice == 2 :
                new_dice = throw_second_dice()
                print('\n',"New value :",first_dice,new_dice,third_dice)
    
            elif rethrow_dice == 3 :
                new_dice = throw_third_dice()
                print('\n',"New value :",first_dice,second_dice,new_dice)

    print("End of the second round.") 

    # If the are still not identical, the last las round begins   
    last_rethrow()

def last_rethrow ():
    global new_dice

    print("Last round !")

    print("Insert 'GO' to start.")
    start_game = input()

    while start_game != "GO" :
        print("Insert 'GO' to start.")
        start_game = input()
    
    for i in range(2):
        if first_dice == second_dice == third_dice : 
            print("All the dices have the same value, you win !")
            return

        else : 
            print('\n',"Which dice do you want to throw again ? 1, 2 or 3 ?")
            rethrow_dice = int(input())

            if isinstance(rethrow_dice,str):
                print("Please, enter 1, 2 or 3.")
                rethrow_dice = int(input())

            while rethrow_dice < 0 and rethrow_dice > 3:
                print("Please enter 1, 2 or 3")
                rethrow_dice = int(input())

            if rethrow_dice == 1 :
                new_dice = throw_first_dice()
                print('\n',"New value :",new_dice,second_dice,third_dice)
    
            elif rethrow_dice == 2 :
                new_dice = throw_second_dice()
                print('\n',"New value :",first_dice,new_dice,third_dice)
    
            elif rethrow_dice == 3 :
                new_dice = throw_third_dice()
                print('\n',"New value :",first_dice,second_dice,new_dice)

        if first_dice == second_dice == third_dice : 
            print("All the dices have the same value, you win !")
            return

    if first_dice != second_dice != third_dice  or first_dice != second_dice or first_dice != third_dice:
        print('\n',"You lost.")    



# Three functions that give random numbers to three dices
def throw_first_dice():
    global first_dice
    first_dice = randint(1,6)
    return first_dice

def throw_second_dice():
    global second_dice
    second_dice = randint(1,6)
    return second_dice

def throw_third_dice():
    global third_dice
    third_dice = randint(1,6)
    return third_dice



game()

