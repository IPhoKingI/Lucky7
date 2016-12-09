###
#Lucky Sevens
###

# Start with $10, every game costs $1 to play
# Roll two dice
# If the result is seven, win 5$ (+$4 overall after the $1 cost)
# The game continuously plays until you run out of money.
# At the end, it tells yoyu how many rounds were played

import random
money = 10
round_number = 0

while money > 0:
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    command = raw_input("Lets play a game kiddo!")
    if command == "yes" or "Yes":
        money -= 1
        round_number += 1
        dice_sum = dice1 + dice2
        if dice_sum == 7:
            print '%s + %s = %s' % (dice1, dice2, dice_sum)
            money += 5
            print "Ok... You currently have %s." % (money)
            print "You've played %s rounds... Buy me something please." % (round_number)
        else:
            print "%s + %s = %s" % (dice1, dice2, dice_sum)
            print "Heh, too bad you got %s" % (dice_sum)
            print "Thanks for your money. You have %s now try again once you've gotten more" % (money)
            print "You've played %s rounds. Come back soon kehehe." % (round_number)


