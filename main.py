import random
from uu import Error

your_health = 10
enemy_health = 10

print("Welcome to boxing showdown! Press [Enter] to start!")
input()

print("In the red corner, we have the challenger, y/n!")
print("In the blue corner, we have our reigning, defending, undisputed champion, Quandale Dingle!")

print("Referee: I want a good clean fight. We went over all the rules in the locker room. No punching below the belt. Break when I tell you to. Protect yourselves at all times")

print("Ready? BOX!!!")

your_last_move = -1
enemy_last_move = -1

print("The enemy bobs and weaves before you")

while your_health > 0 and enemy_health > 0:

    '''
    basic mechanics:
    1 - jab - hits most of the time. deals low damage. easily parried/slipped
    2 - cross - lands well after a jab, otherwise, lands sometimes. avoided by slipping/blocking
    3 - hook - avoided by taking a step back/pulling
    4 - uppercut - most damaging. easiest to land if opponent shells up
    '''

    punch = -1
    # throw 1-4
    available_punches = ["Jab", "Cross", "Hook", "Uppercut"]
    defensive_moves = ["Dodg", "Block", "Counter"]

    while punch not in range(len(available_punches)):
        try:
            punch = int(input("What punch will you throw? >> ")) - 1
            if punch not in range(len(available_punches)):
                print("Please throw a valid punch")
            else:
                print("You threw a [" + str(available_punches[punch]) + "]")
        except Error:
                print("Please throw a valid punch")
    
    opponent_defense = random.randint(0, len(defensive_moves) - 1)
    print("Your opponent responds by [" + defensive_moves[opponent_defense] + "ing]")


    # calculate probabilities here I
    if punch == 0:
        if opponent_defense == 0:
            if random.randint(0, 1) == 1:
                print("You land the jab on your opponent. He takes a bit of damage")
                enemy_health -= 1
            else: 
                print("Your opponent slips the jab. Your attack fails!")
        elif opponent_defense == 1:
            print("Your opponent blocks the jab. He takes only a slight amount of damage.")
            enemy_health -= 1
        else:
            if random.randint(0, 3) == 1:
                print("You try to land the jab on your opponent, but your opponent evaded and hit you with a counter! You take some damage.")
                your_health -= 2
            else:
                print("You land the jab on your opponent. You dodge his lazy attempt to counter.")
            enemy_health -= 1
    elif punch == 1:
        if opponent_defense == 0:
            if random.randint(0, 1) == 1:
                print("You land the cross on your opponent. He takes moderate damage!")
                enemy_health -= 3
            else: 
                print("Your opponent slips the cross. Your attack fails!")
        elif opponent_defense == 1:
            print("Your opponent blocks the cross. He takes only a slight amount of damage.")
            enemy_health -= random.randint(1, 2)
        else:
            if random.randint(0, 1) == 1:
                print("Your opponent counters your cross with a quick jab. You take a bit of damage")
                your_health -= 1
            else:
                print("Your opponent tries to counter, but fails! Your cross hits the target")
                enemy_health -= 3
            # continue here
    elif punch == 2:
        if opponent_defense == 0:
            if random.randint(0, 1) == 1:
                print("Your hook lands on your opponents chin! Your opponent takes massive damage.")
                enemy_health -= 4
            else:
                print("Your opponent rolls under your hook! Your hook misses its target.")
        elif opponent_defense == 1:
            print("Your opponent blocks the incoming hook, but you still manage to hurt your opponent!")
            enemy_health -= random.randint(1, 3)
        elif opponent_defense == 2:
            if random.randint(0, 1) == 1:
                print("Your hook lands on your opponents chin despite his attempt to counter! Your opponent takes serious damage")
                enemy_health -= 4
            else:
                print("Your opponent manages to weave under your hook and counter with a right straight! You take some moderate damage")
                your_health -= 3
    elif punch == 3:
        if opponent_defense == 0:
                print("Your opponent takes a step back to avoid your uppercut! Your punch misses its target.")
        elif opponent_defense == 1:
            print("Your opponent tries to block the incoming uppercut, but his guard gets smashed instead!")
            enemy_health -= 5
        elif opponent_defense == 2:
            if random.randint(0, 1) == 1:
                print("Your uppercut lands on your opponents! Your opponent takes serious damage")
                enemy_health -= 5
            else:
                print("Your opponent manages to step back and counter with a right straight! You take some moderate damage")
                your_health -= 3

    if your_health <= 0 or enemy_health <= 0:
        break
    print("Your health: " + str(your_health))
    print("Enemy health: " + str(enemy_health))

    opponent_punch = random.randint(0, len(available_punches) - 1)
    print("Your opponent throws a [" + str(available_punches[opponent_punch]) + "]")


    defense = -1
    while defense not in range(len(defensive_moves)):
        try:
            defense = int(input("How will you defend? >> ")) - 1
            if defense not in range(len(defensive_moves)):
                print("Please enter a valid defensive move")
            else:
                print("You respond by [" + defensive_moves[defense] + "ing]")
        except Error:
            print("Please enter a valid defense")

    # calculate probabilities here I
    if opponent_punch == 0:
        if defense == 0:
            if random.randint(0, 1) == 1:
                print("Your opponent lands the jab on you. You take a bit of damage")
                your_health -= 1
            else: 
                print("Your slip the jab. Your oppoonent's attack fails!")
        elif defense == 1:
            print("You block the jab. You take only a slight amount of damage.")
            your_health -= 1
        else:
            if random.randint(0, 3) == 1:
                print("Your opponent tries to land the jab, but you evade and hit him with a counter! Your opponent takes some damage.")
                enemy_health -= 2
            else:
                print("Your opponent lands the jab on you. You attempt to counter but fail!.")
            your_health -= 1
    elif opponent_punch == 1:
        if defense == 0:
            if random.randint(0, 1) == 1:
                print("Your opponent lands the cross on you. You take moderate damage!")
                your_health -= 3
            else: 
                print("You slip the cross. His attack fails!")
        elif defense == 1:
            print("You block the cross. You only take a slight amount of damage.")
            your_health -= random.randint(1, 2)
        else:
            if random.randint(0, 1) == 1:
                print("You counter your opponent's cross with a quick jab. Your opponent takes a bit of damage")
                enemy_health -= 1
            else:
                print("Your try to counter, but fail! Your opponent's cross hits the target")
                your_health -= 3
            # continue here
    elif opponent_punch == 2:
        if defense == 0:
            if random.randint(0, 1) == 1:
                print("The hook lands on your chin! You takes massive damage.")
                your_health -= 4
            else:
                print("You roll under the hook! Your opponent's hook misses its target.")
        elif defense == 1:
            print("You block the incoming hook, but you still manage to get hurt!")
            # stopped here. finish it soon
            your_health -= random.randint(1, 3)
        elif defense == 2:
            if random.randint(0, 1) == 1:
                print("Your opponent's hook lands on your chin despite your attempt to counter! You take some serious damage")
                your_health -= 4
            else:
                print("You manage to weave under your opponent's hook and counter with a right straight! Your opponent takes some moderate damage")
                enemy_health -= 3
    elif opponent_punch == 3:
        if defense == 0:
                print("You take a step back to avoid the uppercut! The punch misses its target.")
        elif defense == 1:
            print("You try to block the incoming uppercut, but your guard gets smashed instead!")
            your_health -= 5
        elif defense == 2:
            if random.randint(0, 1) == 1:
                print("The uppercut lands on your chin! You take serious damage")
                your_health -= 5
            else:
                print("You manage to step back and counter with a right straight! Your opponent take some moderate damage")
                enemy_health -= 3
                
    print("Your health: " + str(your_health))
    print("Enemy health: " + str(enemy_health))




if your_health > 0:
    print("Congrats! You win!")
else:
    print("You lost. Try again next time!")