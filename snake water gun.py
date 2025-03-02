# print("#"*10,"WELCOME TO SNAKE WATER GUN GAME","#"*10)
# one = input("Player one choose: ")
# two = input("Player two choose: ")
# if one == "snake" and two == "water":
#     print("Player one Wins.")
# elif one == "water" and two == "snake":
#     print("Player two Wins.")
# elif one == "snake" and two == "gun":
#     print("Player two Wins.")
# elif one == "gun" and two == "snake":
#     print("Player one Wins.")
# elif one == "gun" and two == "water":
#     print("Player two Wins.")
# elif one == "water" and two == "gun":
#     print("Player one Wins.")
# else:
#     print("Wrong input.")


#___________________________________________________________________________
#___________________________________________________________________________


# -1 for snake
# 0 for water
# 1 for gun


# print("#"*10,"WELCOME TO SNAKE WATER GUN GAME","#"*10)
# import random
# computer = random.choice([-1,0,1])
# comp = {-1:"snake" , 0:"water" , 1:"gun"}
# user = {"snake":-1 , "water":0 , "gun":1}
# user_chose = input("\nEnter your choice: ")
# if user != "snake" or user != "water" or user != "gun" :
#     print('')
# else:
#     print("\nWrong Input.")
#     exit(0)
# print(f"\nSo,\tYou chose: {user_chose}",f"\nAnd computer chose: {comp[computer]}")
#
# if computer == user[user_chose]:
#     print("\nIts a draw.")
# else:
#     if computer == -1 and user[user_chose] == 0:
#         print("\nComputer Wins.")
#     elif computer == 0 and user[user_chose] == -1:
#         print("\nYou Win.")
#     elif computer == -1 and user[user_chose] == 1:
#         print("\nYou Win.")
#     elif computer == 1 and user[user_chose] == -1:
#         print("\nComputer Wins.")
#     elif computer == 0 and user[user_chose] == 1:
#         print("\nComputer Wins.")
#     elif computer == 1 and user[user_chose] == 0:
#         print("\nYou Win.")
#     else:
#         print("\nWrong Input.")



#----------------------------------------------------------------------------
#----------------------------------------------------------------------------


# print("#"*10,"WELCOME TO SNAKE WATER GUN GAME","#"*10)
# import random
# computer = random.choice([-1,0,1])
# comp = {-1:"snake" , 0:"water" , 1:"gun"}
# user = {"snake":-1 , "water":0 , "gun":1}
# user_chose = input("\nEnter your choice: ")
# if user != "snake" or user != "water" or user != "gun" :
#     print('')
# else:
#     print("\nWrong Input.")
#     exit(0)
# print(f"\nSo,\tYou chose: {user_chose}",f"\nAnd computer chose: {comp[computer]}")
#
# if computer == user[user_chose]:
#     print("\nIts a draw.")
# elif computer-user[user_chose] == -1 or  computer-user[user_chose] == 2 :
#     print("\nComputer Wins.")
# elif computer-user[user_chose] == 1 or  computer-user[user_chose] == -2 :
#     print("\nYou Win.")
# else:
#     print("Something went wrong.")