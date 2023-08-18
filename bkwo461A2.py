
"""
Shinbeom Kwon - bkwo461 - This program executes a game between a computer and a user
who gets points when a certain combination of numbers is given three times of random numbers.
"""
import random
def main():
    user_name = "bkwo461" 
    player_wins = 0
    computer_wins = 0
    draws = 0
    player_selection = 1
    display_banner(user_name)
    while player_selection != 0:
        print()
        display_menu()
        player_selection = get_user_input()
        if player_selection == 1:
            player_roll = get_valid_roll()
            computer_roll = get_valid_roll()
            player_score = get_score(player_roll)
            computer_score = get_score(computer_roll)
            print()
            print_separator()
            print_roll("Player", player_roll, player_score)
            print_roll("Computer", computer_roll, computer_score)
            if player_score > computer_score:
                print("Player has won!")
                player_wins += 1
            elif player_score < computer_score:
                print("Computer has won!")
                computer_wins += 1
            else:
                print("It's a draw!")
                draws += 1
            print("Player wins:", player_wins, "Computer wins:", computer_wins, "Draws:", draws)
            print_separator()
    print()
    print_separator()
    print_player_stats(player_wins, computer_wins, draws)
    print_separator()
def print_separator():
    print("*"*46)
def display_banner(user_name):
    print("*"*(15+len(user_name)))
    print("Cee-lo Game by",user_name)
    print("*"*(15+len(user_name)))
def display_menu():
    print("Please make a selection:")
    print("Enter 1 to play a round of Cee-lo")
    print("Enter 0 to exit")
def get_user_input():
    number = int(input("Enter your selection: "))
    while number != 1 and number != 0:
        print("Make a valid selection!")
        number = int(input("Enter your selection: "))
    if number == 1:
        result = number
    elif number == 0:
        result = number
    return result
def roll_three_dice():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    num3 = random.randint(1, 6)
    dice_string = str(num1)+str(num2)+str(num3)
    return dice_string
def is_456(dice_str):
    if 2 >= int(dice_str.find("4"))>=0 and 2 >= int(dice_str.find("5"))>=0 and 2 >= int(dice_str.find("6"))>=0:
        return True
    else:
        return False
def is_123(dice_str):
    if 2 >= int(dice_str.find("1"))>=0 and 2 >= int(dice_str.find("2"))>=0 and 2 >= int(dice_str.find("3"))>=0:
        return True
    else:
        return False
def is_trip(dice_str):
    if dice_str[0]==dice_str[1]==dice_str[2]:
        return True
    else:
        return False
def is_point(dice_str):
    if dice_str[0]==dice_str[1]!=dice_str[2] or dice_str[0]==dice_str[2]!=dice_str[1] or dice_str[1]==dice_str[2]!=dice_str[0]:
        return True
    else:
        return False
def is_valid_roll(dice_str):
    if 2>=dice_str.find('1')>=0 and 2>=dice_str.find('2')>=0 and 2>=dice_str.find('3')>=0:
        return True
    elif 2>=dice_str.find('4')>=0 and 2>=dice_str.find('5')>=0 and 2>=dice_str.find('6')>=0:
        return True
    elif dice_str[0] == dice_str[1] == dice_str[2]:
         return True
    elif dice_str[0]==dice_str[1]!=dice_str[2] or dice_str[2]==dice_str[1]!=dice_str[0] or dice_str[0]==dice_str[2]!=dice_str[1]:
        return True
    else:
        return False
def get_valid_roll():
    dice_str = roll_three_dice()
    if is_valid_roll(dice_str) == True:
        return dice_str
    elif is_valid_roll(dice_str) == False:
        while is_valid_roll(dice_str)==False:
            roll_three_dice()
            dice_str = roll_three_dice()
    return dice_str
def type_of_roll(dice_str, player):
    if is_123(dice_str) == True:
        string = "123"
    else:
        if is_456(dice_str) == True:
            string = "456"
        else:
            if is_trip(dice_str) == True:
                string = "TRIP"
            else:
                if is_point(dice_str) == True:
                    string = "POINT"
                else:
                    string = "None"
                    return string
    return player + " has rolled a "+ string
def get_point_score(dice_str):
     if dice_str[0]==dice_str[1]!=dice_str[2]:
        score = 10 + int(dice_str[2])
     if dice_str[0]==dice_str[2]!=dice_str[1]:
         score = 10 + int(dice_str[1])
     if dice_str[1]==dice_str[2]!=dice_str[0]:
         score = 10 + int(dice_str[0])
     return score
def get_trip_score(dice_str):
    
    if dice_str[0]==dice_str[1]==dice_str[2]=='1':
        score = 21
    elif dice_str[0]==dice_str[1]==dice_str[2]=='2':
         score =22
    elif dice_str[0]==dice_str[1]==dice_str[2]=='3':
        score =23
    elif dice_str[0]==dice_str[1]==dice_str[2]=='4':
        score =24
    elif dice_str[0]==dice_str[1]==dice_str[2]=='5':
        score=25
    elif dice_str[0]==dice_str[1]==dice_str[2]=='6':
        score =26
    return score
def get_score(dice_str):
     if is_123(dice_str) == True:
        score = 0
    
     else:
         
         if is_456(dice_str)==True:
             score = 30
         else:
             if is_point(dice_str) == True:
                 
                 score =get_point_score(dice_str)
             else:
                  if is_trip(dice_str) == True:
                      score = get_trip_score(dice_str)
                  else:
                     score = 0
     return score 
def print_roll(player_name, player_roll, player_score):
    
    print(player_name+ " has rolled: "+ player_roll)
    print("(",type_of_roll(player_roll,player_name)," for a score of ",player_score,")",sep = "")
def print_player_stats(player_wins, computer_wins, draws):
    if player_wins+computer_wins+draws == 0:
         percentage = 0.0
    else:
        
        percentage = round((player_wins*100/(player_wins+computer_wins+draws)),1)
    print("Player wins:", player_wins)
    print("Win percentage: ",percentage,"%",sep="")
    
        
    
main()
