# CIT590 - HW1 Lunar Lander game
# Pimkhuan(Pim) Hannanta-anan
# Due 9/6/16

play = 1
while play == 1:
    
    # Initiate parameters
    alt = 100          # altitude, unit m
    vel = 0             # velocity, unit m/s
    fuel_rem = 50     # remaining fuel, unit L
    fuel_const = 1.5    # fuel burning constant
    t = 1               # t=1s/turn
    vel_safe = 10       # safe landing velocity, unit m/s
    
    while alt > 0:

        # Input fuel
        fuel_burn = float(input("Please input amount of fuel to burn:"))

        # check if the input value is legal
        if fuel_burn > fuel_rem:
            fuel_burn = fuel_rem
        if fuel_burn < 0:
            fuel_burn = 0
        
        # Calculate current velocity
        vel = vel + 1.6 - fuel_const*fuel_burn
        
        # Calculate current altitude
        alt = alt - (vel*t)
        
        # Calculate remaining fuel
        fuel_rem = fuel_rem - fuel_burn

    if alt < 0:
        alt = 0
    
    if vel <= vel_safe:
        print("your final velocity is", vel, "m/s")
        print("your current altitude is", alt, "m")
        print("Congratulations! you have landed safely \n")   
    else:
        depth = vel*t
        print("your final velocity is", vel, "m/s")
        print("you have just blast", depth, "m", "in the lunar surface")
        print("your current altitude is", alt, "m")
        print("Sorry! you have landed too strong and destroyed the moon \n")


    # Does the player want to play again
    input_valid = 0

    while input_valid == 0:
        replay = input("Would you like to play again? type 'y' or'Y' for YES and 'n' or 'N' for NO \n")
        if replay == 'y' or replay == 'Y':
            input_valid = 1
            play = 1
        elif replay == 'n' or replay == 'N':
            input_valid = 1
            play = 0
        else:
            input_valid = 0
 
        
