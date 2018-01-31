'''CIT590 HW5 - SquareLotron
    Pimkhuan (Pim) Hannanta-anan
    Due 10/4/2016 '''

import copy
import random

def make_squarelotron(num_list):
    '''Make and return squarelotron containing 25 numbers given in num_list'''
    squarelotron = [num_list[0:5],
                    num_list[5:10],
                    num_list[10:15],
                    num_list[15:20],
                    num_list[20:]]
    return squarelotron
        
def make_list(squareLotron):
    '''Return a "flat" list of numbers in squarelotron'''
    num_list = []
    for row in squareLotron:
        for col in row:
            num_list.append(col)
        
    return num_list

def upside_down_flip(squareLotron, ring):
    '''Perform the Upside-Down Flip on the squarelotron, and
    return the new squarelotron'''   
    new_squareLotron = copy.deepcopy(squareLotron)
    if ring == 'O':
        new_squareLotron[0] = squareLotron[4]
        new_squareLotron[4] = squareLotron[0]
    else:
        new_squareLotron[1] = squareLotron[3]
        new_squareLotron[3] = squareLotron[1]

    #print(squareLotron)
    #print("new: ", new_squareLotron) 
    return new_squareLotron

def left_right_flip(squareLotron, ring):
    '''Perform the Left-Right Flip on the squarelotron, and
    return the new squarelotron'''
    new_squareLotron = copy.deepcopy(squareLotron)
    if ring == 'O':
        for i in range(0,len(squareLotron)):
            new_squareLotron[i][0] = squareLotron[i][4]
            new_squareLotron[i][4] = squareLotron[i][0]
    else:
        for i in range(0,len(squareLotron)):
            new_squareLotron[i][1] = squareLotron[i][3]
            new_squareLotron[i][3] = squareLotron[i][1]

    #print(squareLotron)
    #print("new: ", new_squareLotron) 
    return new_squareLotron
    
def inverse_diagonal_flip(squareLotron, ring):
    '''Perform the Main Inverse Diagonal of the squarelotron, and
    return the new squarelotron'''
    new_squareLotron = copy.deepcopy(squareLotron)
    if ring == 'O':
        new_squareLotron[0][4] = squareLotron[4][0]
        new_squareLotron[4][0] = squareLotron[0][4]
    else:
        new_squareLotron[1][3] = squareLotron[3][1]
        new_squareLotron[3][1] = squareLotron[1][3]

    #print(squareLotron)
    #print("new: ", new_squareLotron) 
    return new_squareLotron

def main_diagonal_flip(squareLotron, ring):
    '''Perform the Main Diagonal Flip of the squarelotron, and
    return the new squarelotron'''
    new_squareLotron = copy.deepcopy(squareLotron)
    if ring == 'O':
        new_squareLotron[0][0] = squareLotron[4][4]
        new_squareLotron[4][4] = squareLotron[0][0]
    else:
        new_squareLotron[1][1] = squareLotron[3][3]
        new_squareLotron[3][3] = squareLotron[1][1]

    #print(squareLotron)
    #print("new: ", new_squareLotron) 
    return new_squareLotron

def print_instruction():
    print('''\tA Squarelotron consist basically of a matrix of numbers.
    This matrix can be decomposed as square rings which can rotate
    independently in 4 different ways: Upside-Down (↕), Left-Right (↔),
    reflected through the Inverse Diagonal ( / ), and reflected through
    the Main Diagonal ( \ ).
    \tAs a puzzle, the object of the squarelotron is to take one
    that is scrambled, and return it to its original state.\n
    The game takes 3-letter string input from the player:
    The first two letters determine the type of flip
      UD = Upside-Down
      LR = Left-Right
      ID = Inverse Diagonal
      MD = Main Diagonal
    The last letter determine the ring to be flipped -
      I = inner
      O = outer''')

def print_squarelotron(squarelotron):

    print("\n  Current SquareLotron\n" + "_"*24)    
    for sq in squarelotron:
        print("\n", "{:3d} {:3d} {:3d} {:3d} {:3d}".format(sq[0],sq[1],sq[2],
              sq[3],sq[4]))

def make_move(squareLotron, move):
    ring = move[2]
    if move[0:2] == 'UD':
        new_squareLotron = upside_down_flip(squareLotron, ring)
    elif move[0:2] == 'LR':
        new_squareLotron = left_right_flip(squareLotron, ring)
    elif move[0:2] == 'ID':
        new_squareLotron = inverse_diagonal_flip(squareLotron, ring)
    elif move[0:2] == 'MD':
        new_squareLotron = main_diagonal_flip(squareLotron, ring)

    return new_squareLotron

def isvalid_input(move):
    return (isvalid_flip(move[0:2]) and isvalid_ring(move[2]))
          
def isvalid_flip(flip):
    return (flip=='UD' or flip=='LR' or flip=='ID' or flip=='MD')

def isvalid_ring(ring):
    return (ring=='I' or ring=='O')

def player_input(prompt):
    move = str(input(prompt)).upper()
    
    if isvalid_input(move):
        return move
    else:
        return player_input("Invalid input, enter your move again!\n")

def keep_playing(prompt):
    '''Return 2-tuple boolean whether player wishes to continue playing or start over'''
    ans = str(input(prompt)).upper()
    if ans == 'Y':
        return (True, False)
    elif ans == 'N':
        return (False, False)
    elif ans == 'S':
        return (True, True)
    else:
        return keep_playing("Invalid input! Enter 'Y' for Yes, 'N' for No, 'S' for starting over\n")
        
def main():
    '''Print instruction'''
    print_instruction()

    '''Initiate a list of 25 numbers for the initial squareLotron'''
    numb = list(range(0,25))
    random.shuffle(numb)
    
    '''Make a squarelotron'''
    squarelotron = make_squarelotron(numb)
    print_squarelotron(squarelotron)

    keep_going = 1
    start_over = 0
    # LOOP #
    while keep_going:
        '''Re-initialize the squarelotron if player wishes to start over'''
        if start_over:
            squarelotron = make_squarelotron(numb)
            print_squarelotron(squarelotron)
            
        '''Take player's input'''
        move = player_input('Enter your next move: ')

        '''Flip the squareLotron according to user's input'''
        new_squarelotron = make_move(squarelotron, move)
        
        '''Update the squarelotron'''
        new_numb = make_list(new_squarelotron)
        squarelotron = make_squarelotron(new_numb)
        print_squarelotron(squarelotron)

        '''Ask if player wish to continue'''
        prompt = "Flip again? Enter 'Y' for Yes, 'N' for No, 'S' for starting over: " 
        (keep_going, start_over) = keep_playing(prompt)
        
    # ADD OPTION FOR STARTING OVER
if __name__ == "__main__":
    main()
