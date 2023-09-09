print('''
 ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input("You just entered a mysterious island. Do you want move forward or wait for rescue? forward/wait\n")
if choice1.lower() == "forward":
  choice2 = input("As you explore the island you found a bottle with a paper in it. Do you want to open the bottle? y/n\n")
  if choice2.lower() == "y":
    choice3 = input("Yay you found a treasure map. Do you want to find the treasure? y/n\n")
    if choice3.lower() == "y":
      choice4 = input("As follow the map you enter a forest area. There is you found a mysterious door. To open the door you need to solve a puzzle. If you answer it correctly you can directly cross the forest through the door or you will go through the forest and encounter dangers. Do you want to slove the puzzle? y/n\n")
      if choice4.lower() == "y":
        choice5 = input("Here is the puzzle. 'You are in a dark room with a candle, a wood stove and a gas lamp. You only have one match, so what do you light first?'\n")
        if choice5.lower() == "match":
          choice6 = input("You successfully crossed the forest. Now you are at a cross roads which road do you choose? right/left/straight\n")
          if choice6.lower() == "right":
            choice7 = input("There is a river you need to cross to reach the treasure. There is a boat nearby but you need to solve a puzzle to use the boat. Do you want to solve the puzzle? y/n\n")
            if choice7.lower() == "y":
              choice8 = input("Two ladies played cards for candy; the winner received one piece per game from the loser. When it was time for one of the ladies to go home, one lady had won three games, while the other lady had a profit of three pieces of candy.How many individual games had they played?\n")
              if choice8 == "9":
                choice9 = input("You have succesfully crossed the river. There are three doors infront of you in different colours.choose a door. red/blue/yellow\n")
                if choice9.lower() == "red":
                  print("The door you opened contains fire.")
                  print("Game Over")
                elif choice9.lower() == "yellow":
                  print("You have found the treasure. CONGRATULATIONS!!")
                else:
                  print("The door you opened contains beasts")
                  print("Game Over")
              else:
                print("You fell into water. Game Over")
            else: 
              print("You encoutered monsters while you swam. Game Over")
          elif(choice6.lower() == "left"):
            print("You fell into a pit. Game Over")
          else:
            print("You encountered pirates and lost the map. Game Over")
        else:
          print("Your answer is wrong.Game Over")
      else:
        print("You were eaten by the animals. Game Over")
    else:
      print("You returned to the shore. Game Over")
  else:
    print("You dropped the bottle.")
else:
  print("You were rescued.")
