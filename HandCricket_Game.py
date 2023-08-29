import random, time
wins = 0
lost = 0
ties = 0


def main(wins, lost, ties):
    score = 0
    def scnd_bat(target, score, wins, lost, ties): #Function for second innnings if player bats
        print("\nSTART Batting")
        while(score <= target):
            try:
                user_runs = int(input("Enter a number(1-6): "))
                if(user_runs > 6):
                    print("Invalid Entry!!!")
                    continue
            except ValueError:
                print("Invalid Entry!!!")
                continue
            comp_runs = random.randint(1,6)
            time.sleep(0.5)
            print("\nUser hits: " + str(user_runs))
            print("Computer puts: " + str(comp_runs))
            if(user_runs == comp_runs):
                print("\nYou are OUT!!!")
                print("Your Total score = " + str(score))
                if(score != target):
                    print("\nYou LOST and Computer WINS by " + str((target - score)) + " runs!!!")
                    lost += 1
                break
            else:
                score += user_runs
                print("Score = " + str(score))
        if score > target:
            print("\nYour Total score = " + str(score))
            print("\nYou WON!!!")
            wins += 1
        if score == target:
            print("\nThe Match is DRAWN!!!")
            ties += 1
        play_againfunc()

    def scnd_bowl(target, score, wins, lost, ties): # Function for second innnings if player bowls
        print("\nSTART Bowling")
        while(score <= target):
            try:
                user_runs = int(input("Enter a number(1-6): "))
                if(user_runs > 6):
                    print("Invalid Entry!!!")
                    continue
            except ValueError:
                print("Invalid Entry!!!")
                continue
            comp_runs = random.randint(1,6)
            time.sleep(0.5)
            print("\nUser puts: " + str(user_runs))
            print("Computer hits: " + str(comp_runs))
            if(user_runs == comp_runs):
                print("\nComputer is OUT!!!")
                print("Computer total score = "+ str(score))
                print("\nYou WON by " + str((target - score)) + " runs!!!")
                wins += 1
                break
            else:
                score += comp_runs
                print("Score = " + str(score))
        if score > target:
            print("\nComputer total score = "+ str(score))
            print("\nYou LOST and Computer WON!!!")
            lost += 1
        if score == target:
            print("\nThe Match is DRAWN!!!")
            ties += 1
        play_againfunc()
    
    def play_againfunc(): # Function to ask the player if they want to play again 
        play_again = input("\nDo you want to play again?(Enter Y for Yes and N for No): ")
        if(play_again.lower() == 'y' or play_again.lower() == 'yes'):
            main(wins, lost, ties)
        elif(play_again.lower() == 'n' or play_again.lower() == 'no'):
            print("Thank You, See you again!!!")
            time.sleep(1)
        else:
            print("Invalid Entry")
            play_againfunc()


    """ FUNCTION FOR BATTING in 1st INNINGS """
    def fst_bat(score):
        print("\nSTART Batting")
        while(1):
            try:
                user_runs = int(input("Enter a number(1-6): "))
                if(user_runs > 6):
                    print("Invalid Entry!!!")
                    continue
            except ValueError:
                print("Invalid Entry!!!")
                continue
            comp_runs = random.randint(1,6)
            time.sleep(0.5)
            print("\nUser hits: " + str(user_runs))
            print("Computer puts: " + str(comp_runs))
            if(user_runs == comp_runs):
                print("\nYou are OUT!!!")
                break
            else:
                score += user_runs
                print("Score = " + str(score))
        print("\nYour Total score = " + str(score))
        print("\nComputer needs "+ str(score + 1)+ " runs to win!!! ")
        scnd_bowl(score, 0, wins, lost, ties)

    """ FUNCTION FOR BOWLING in 1st INNINGS"""
    def fst_bowl(score):
        print("\nSTART Bowling")
        while(1):
            try:
                user_runs = int(input("Enter a number(1-6): "))
                if(user_runs > 6):
                    print("Invalid Entry!!!")
                    continue
            except ValueError:
                print("Invalid Entry!!!")
                continue
            comp_runs = random.randint(1,6)
            time.sleep(0.5)
            print("\nUser puts: " + str(user_runs))
            print("Computer hits: " + str(comp_runs))
            if(user_runs == comp_runs):
                print("\nComputer is OUT!!!")
                break
            else:
                score += user_runs
                print("Score = " + str(score))
        print("\nComputer's Total score = " + str(score))
        print("\nYou need "+ str(score + 1)+ " runs to win!!! ")
        scnd_bat(score,0, wins, lost, ties)

    """ FUNCTION FOR USER's BATTING OR FIELDING CHOICE"""
    def brfchoice():
            choice = input("Enter B for batting or F for Bowling: ")
            if(choice.lower() == "b"):
                print("\nYou Chose Batting")
                fst_bat(score)
            elif(choice.lower() == "f"):
                print("\nYou Chose Bowling")
                fst_bowl(score)
            else:
                print("\nInvalid choice!!!")
                brfchoice() 
                
    def toss(): # Functionn for TOSS
        user_toss = input("\nEnter H for heads and T for tails: ")
        if(user_toss.lower() == 'h'):
            user_toss = 1
        elif(user_toss.lower() == 't'):
            user_toss = 2
        else:
            print("\nInvalid choice!!!")
            toss()
        return user_toss

    print("Welcome to the Handcricket game!!!Wins: ",wins," Lost: ", lost, " Ties: ", ties, "\nLet's go for the TOSS>>>")
    
    user_toss = toss()
    comp_toss = random.randint(1,2)

    time.sleep(0.5)
    if(user_toss == comp_toss):
        print("\nYou WON the Toss")
        brfchoice()  
    else:
        print("\nYou lost the toss")
        comp_brf = random.randint(1,2)
        if(comp_brf == 1):
            print("\nComputer WON the toss and Chose to BAT")
            fst_bowl(score)
        else:
            print("\nComputer WON the toss and Chose to Bowl")
            fst_bat(score)
main(wins, lost, ties)
