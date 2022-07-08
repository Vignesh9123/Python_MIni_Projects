import random, time, sys

play_again = True

user_total = 0
comp_total = 0

target = 0

user_out = False
comp_out = False

user_won = False
comp_won = False

wins = 0
losses = 0
ties = 0

while play_again:
    print("Hand Cricket!!")
    print('Wins : ' + str(wins), 'Losses : ' + str(losses) , 'Ties : ' +str(ties) , sep=' | ')
    print(' Press b for batting first and f for bowling first and q to Quit the game')
    choice = input()
    play_again = False
    if choice == 'b':
        print("You chose to bat\nNow HIT!")
        while not user_out:
         user_runs = int(input())
         print(str(user_runs) + " VS.." , end='')
         comp_bowl = random.randint(1, 6)
         time.sleep(0.5)
         print(comp_bowl)
         if user_runs != comp_bowl:
            user_total = user_total + user_runs
            print("Your runs : " + str(user_total))
         else:
            print("You are OUT!!")
            print("Your Total : " + str(user_total))
            user_out = True
            while user_out and not comp_won and not user_won :
                time.sleep(1)
                print("Now you BOWL!!\n Start")
                while not comp_out:
                 user_bowl = int(input())
                 print(str(user_bowl) + ' VS..', end=' ')
                 comp_runs = random.randint(1, 6)
                 time.sleep(0.5)
                 print(comp_runs)

                 if comp_runs != user_bowl:
                    comp_total = comp_total + comp_runs
                    print("Computer runs : " + str(comp_total))

                 if comp_total > user_total:
                    print("Computer Total : " + str(comp_total))
                    print("Computer WON!!")
                    comp_won = True
                    losses += 1
                    break

                 elif comp_runs == user_bowl:
                    print("Computer is OUT!")
                    print("Computer total : " + str(comp_total))
                    comp_out = True

                    if comp_out:
                     print("You WON by " + str(user_total - comp_total ) + " runs")
                     wins +=1
                     user_won = True
                     break

                 elif comp_total == user_total and user_won == True :
                     print("It is a tie!")
                     ties += 1

    if choice == 'f':
        print("You Chose to bowl\nNow Start")
        while not comp_out and not user_out:
            user_bowl = int(input())
            print(str(user_bowl) + ' VS.. ', end=' ')
            comp_runs = random.randint(1, 6)
            time.sleep(0.5)
            print(comp_runs)
            if comp_runs != user_bowl:
                comp_total = comp_total + comp_runs
                print('Computer runs : ' + str(comp_total) )
            else:
                time.sleep(0.5)
                print('Computer is OUT!!')
                print("Computer total : " + str(comp_total))
                comp_out = True
                if comp_out and not user_out:
                    time.sleep(0.5)
                    print("Now you should hit " + str(comp_total + 1) + ' runs to WIN\n Start')
                    while not user_out:
                     comp_out = False
                     user_runs = int(input())
                     print(str(user_runs) + ' VS..' , end='')
                     comp_bowl = random.randint(1, 6)
                     print(comp_bowl)
                     if user_runs != comp_bowl:
                       user_total = user_runs + user_total
                       print('Your runs : ' + str(user_total))
                     elif user_runs == comp_bowl:
                        print("You are OUT!\n Your Total :" + str(user_total))
                        user_out = True
                        comp_out = True
                        if comp_total > user_total:
                           time.sleep(0.5)
                           print('Computer WON by ' + str(comp_total - user_total) + ' runs')
                           comp_won = True
                           losses += 1
                           break

                        elif comp_total == user_total:
                          print("It is a tie")
                          comp_out = False
                          user_out = True
                          ties += 1
                          break

                     if user_total > comp_total:
                         time.sleep(0.5)
                         print("You WON!!")
                         comp_out = False
                         user_out = True
                         user_won = True
                         wins += 1
                         break
                    # if user_total == comp_total and user_out:
                        # print("It is a tie")
                         #comp_out = False
                        # user_out = True
                        # ties += 1
                       #  break
    if choice == 'q' :
        print("You chose to quit")
        sys.exit()




    again = input("Do You Wish To Play Again ? \n")
    if again == "Yes" or again == 'yes':
        play_again = True
        user_out = False
        comp_out = False
        user_total = 0
        comp_total = 0
        user_runs = 0
        comp_runs = 0
        user_won = False
        comp_won = False
    elif again == "No" or again =='no':
        print("Thank you for playing")
        sys.exit()





















