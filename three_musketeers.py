# HW3: The Three Musketeers Game
# by David Matuszek and Pimkhuan(Pim) Hannanta-anan.

# In all methods,
#   A 'location' is a two-tuple of integers, each in the range 0 to 4.
#        The first integer is the row number, the second is the column number.
#   A 'direction' is one of the strings "up", "down", "left", or "right".
#   A 'board' is a list of 5 lists, each containing 5 strings: "M", "R", or "-".
#        "M" = Musketeer, "R" = Cardinal Richleau's man, "-" = empty.
#        Each list of 5 strings is a "row"
#   A 'player' is one of the strings "M" or "R" (or sometimes "-").
#
# For brevity, Cardinal Richleau's men are referred to as "enemy".
# 'pass' is a no-nothing Python statement. Replace it with actual code.
import random

def create_board():
    global board
    """Creates the initial Three Musketeers board and makes it globally
       available (That is, it doesn't have to be passed around as a
       parameter.) 'M' represents a Musketeer, 'R' represents one of
       Cardinal Richleau's men, and '-' denotes an empty space."""
    m = 'M'
    r = 'R'
    board = [ [r, r, r, r, m],
              [r, r, r, r, r],
              [r, r, m, r, r],
              [r, r, r, r, r],
              [m, r, r, r, r] ]

def set_board(new_board):
    """Replaces the global board with new_board."""
    global board
    board = new_board

def get_board():
    """Just returns the board. Possibly useful for unit tests."""
    return board

def string_to_location(s):
    """Given a two-character string (such as 'A5'), returns the designated
       location as a 2-tuple (such as (0, 4))."""
    assert s[0] >= 'A' and s[0] <= 'E'
    assert s[1] >= '1' and s[1] <= '5'

    # Replace with code
    rows = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4}
    cols = {'1':0, '2':1, '3':2, '4':3, '5':4}

    row = rows[s[0]]
    col = cols[s[1]]
    loc = (row,col)
    return loc
        
def location_to_string(location):
    """Returns the string representation of a location."""
    assert location[0] >= 0 and location[0] <= 4
    assert location[1] >= 0 and location[1] <= 4

    # Replace with code
    rows = {0:'A', 1:'B', 2:'C', 3:'D', 4:'E'}
    cols = {0:'1', 1:'2', 2:'3', 3:'4', 4:'5'}

    row = rows[location[0]]
    col = cols[location[1]]

    str_loc = row + col
    return str_loc

def at(location):
    """Returns the contents of the board at the given location."""
    return board[location[0]][location[1]]

def all_locations():
    """Returns a list of all 25 locations on the board."""
    # Replace with code
    all_loc = [(0,0), (0,1), (0,2), (0,3), (0,4),
               (1,0), (1,1), (1,2), (1,3), (1,4),
               (2,0), (2,1), (2,2), (2,3), (2,4),
               (3,0), (3,1), (3,2), (3,3), (3,4),
               (4,0), (4,1), (4,2), (4,3), (4,4),]
    return all_loc

def adjacent_location(location, direction):
    """Return the location next to the given one, in the given direction.
       Does not check if the location returned is legal on a 5x5 board."""
    (row, column) = location
    
    # Replace with code
    if direction == 'left' or direction == 'L':
        column = column - 1
    elif direction == 'right' or direction == 'R':
        column = column + 1
    elif direction == 'up' or direction == 'U':
        row = row - 1
    elif direction == 'down' or direction == 'D':
        row = row + 1

    loc_next = (row, column)
    return loc_next

def is_legal_move_by_musketeer(location, direction):
    """Tests if the Musketeer at the location can move in the direction."""
    assert at(location) == 'M'
    
    # Replace with code
    loc_next = adjacent_location(location, direction)
    adj_piece = at(loc_next)
    if adj_piece == 'R':
        return True
    else:
        return False

    #### CHECK THIS AGAIN WHAT TO DO WITH ILLEGAL MOVE

def is_legal_move_by_enemy(location, direction):
    """Tests if the enemy at the location can move in the direction."""
    assert at(location) == 'R'

    # Replace with code
    loc_next = adjacent_location(location, direction)
    adj_piece = at(loc_next)
    if adj_piece == '-':
        return True
    else:
        return False
    
def is_legal_move(location, direction):
    """Tests whether it is legal to move the piece at the location
    in the given direction."""

    # Replace with code
    cur_piece = at(location)

    if is_within_board(location, direction):
        if cur_piece == 'M':
            is_legal = is_legal_move_by_musketeer(location, direction)
        elif cur_piece == 'R':
            is_legal = is_legal_move_by_enemy(location, direction)
        elif cur_piece == '-':
            is_legal = False
    else:
        is_legal = False

    return is_legal

def has_some_legal_move_somewhere(who):
    """Tests whether a legal move exists for player "who" (which must
    be either 'M' or 'R'). Does not provide any information on where
    the legal move is."""
    # Replace with code
    if who == 'R':
        has_legal_move = find_legal_move('R')
    elif who == 'M':
        has_legal_move = find_legal_move('M')

    return has_legal_move

def find_legal_move(who):
    """Loop through the board to find the first legal move.(I create this
    function myself) """
    found_legal_move = 0
    row = 0
   
    while (not found_legal_move) and row <= 4:
        col = 0       
        while ((not found_legal_move) and (col <= 4)
               and (who in board[row][col:])):
            if board[row][col] == who:
                location = (row,col)
                if can_move_piece_at(location):
                    found_legal_move = 1
            col += 1

        row += 1

    return found_legal_move

def possible_moves_from(location):
    """Returns a list of directions ('left', etc.) in which it is legal
       for the player at location to move. If there is no player at
       location, returns the empty list, []."""
    # Replace with code
    pos_dir = []
    if is_legal_move(location, 'left'):
        pos_dir.append('left')
    if is_legal_move(location, 'right'):
        pos_dir.append('right')
    if is_legal_move(location, 'up'):
        pos_dir.append('up')
    if is_legal_move(location, 'down'):
        pos_dir.append('down')

    return pos_dir

def can_move_piece_at(location):
    """Tests whether the player at the location has at least one move available."""
    # Replace with code
    pos_mov = possible_moves_from(location)
    if not pos_mov:
        return False
    else:
        return True

def is_legal_location(location):
    """Tests if the location is legal on a 5x5 board."""
    # Replace with code
    if (location[0] >= 0
            and location[0] <= 4
            and location[1] >= 0
            and location[1] <= 4):
        return True
    else:
        return False
    
def is_within_board(location, direction):
    """Tests if the move stays within the boundaries of the board."""
    # Replace with code
    adj_loc = adjacent_location(location, direction)
    is_legal = is_legal_location(adj_loc)
    return is_legal
    
def all_possible_moves_for(player):
    """Returns every possible move for the player ('M' or 'R') as a list
       (location, direction) tuples."""
    # Replace with code
    all_loc = all_locations()
    pos_moves = []
    for loc in all_loc:
        if at(loc) == player:
            pos_dirs = possible_moves_from(loc)
            for dir in pos_dirs:
                pos_moves.append((loc, dir))
            
    return pos_moves
    
def make_move(location, direction):
    """Moves the piece in location in the indicated direction."""
    # Replace with code
    piece = at(location)
    next_loc = adjacent_location(location, direction)
    new_board = board
    new_board[next_loc[0]][next_loc[1]] = piece
    new_board[location[0]][location[1]] = '-'
    set_board(new_board)
    
    
def choose_computer_move(who):
    """The computer chooses a move for a Musketeer (who = 'M') or an
       enemy (who = 'R') and returns it as the tuple (location, direction),
       where a location is a (row, column) tuple as usual."""
    # Replace with code
    pos_moves = all_possible_moves_for(who)
    n_pos_moves = len(pos_moves)
    select_loc_idx = random.randint(1,n_pos_moves) - 1
    select_move = pos_moves[select_loc_idx]

    return select_move

def is_enemy_win():
    """Returns True if all 3 Musketeers are in the same row or column."""
    # Replace with code
    M_loc = []
    for i, row in enumerate(board):
        nM = row.count('M')
        if nM == 3:
            is_enm_win = True
            return is_enm_win
        elif nM == 2:
            is_enm_win = False
            return is_enm_win
        elif nM == 1:
            col = row.index('M')
            M_loc.append(col)
            
    if len(M_loc) == 3 and (M_loc[0] == M_loc[1] == M_loc[2]):
        is_enm_win = True
        return is_enm_win
    else:
        is_enm_win = False
        return is_enm_win
        
#---------- Communicating with the user ----------

def print_board():
    print("    1  2  3  4  5")
    print("  ---------------")
    ch = "A"
    for i in range(0, 5):
        print(ch, "|", end = " ")
        for j in range(0, 5):
            print(board[i][j] + " ", end = " ")
        print()
        ch = chr(ord(ch) + 1)
    print()

def print_instructions():
    print()
    print("""To make a move, enter the location of the piece you want to move,
and the direction you want it to move. Locations are indicated as a
letter (A, B, C, D, or E) followed by an integer (1, 2, 3, 4, or 5).
Directions are indicated as left, right, up, or down (or simply L, R,
U, or D). For example, to move the Musketeer from the top right-hand
corner to the row below, enter 'A5 left' (without quotes).
For convenience in typing, you may use lowercase letters.""")
    print()

def choose_users_side():
    """Returns 'M' if user is playing Musketeers, 'R' otherwise."""
    user = ""
    while user != 'M' and user != 'R':
        answer = input("Would you like to play Musketeer (M) or enemy (R)? ")
        answer = answer.strip()
        if answer != "":
            user = answer.upper()[0]
    return user

def get_users_move():
    """Gets a legal move from the user, and returns it as a
       (location, direction) tuple."""    
    directions = {'L':'left', 'R':'right', 'U':'up', 'D':'down'}
    move = input("Your move? ").upper().replace(' ', '')
    if (len(move) >= 3
            and move[0] in 'ABCDE'
            and move[1] in '12345'
            and move[2] in 'LRUD'):
        location = string_to_location(move[0:2])
        direction = directions[move[2]]
        if is_legal_move(location, direction):
            return (location, direction)
    print("Illegal move--'" + move + "'")
    return get_users_move()

def move_musketeer(users_side):
    """Gets the Musketeer's move (from either the user or the computer)
       and makes it."""
    if users_side == 'M':
        (location, direction) = get_users_move()
        if at(location) == 'M':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Musketeer", location, direction)
        else:
            print("You can't move there!")
            return move_musketeer(users_side)
    else: # Computer plays Musketeer
        (location, direction) = choose_computer_move('M')         
        make_move(location, direction)
        describe_move("Musketeer", location, direction)
        
def move_enemy(users_side):
    """Gets the enemy's move (from either the user or the computer)
       and makes it."""
    if users_side == 'R':
        (location, direction) = get_users_move()
        if at(location) == 'R':
            if is_legal_move(location, direction):
                make_move(location, direction)
                describe_move("Enemy", location, direction)
        else:
            print("You can't move there!")
            return move_enemy(users_side)
    else: # Computer plays enemy
        (location, direction) = choose_computer_move('R')         
        make_move(location, direction)
        describe_move("Enemy", location, direction)
        return board

def describe_move(who, location, direction):
    """Prints a sentence describing the given move."""
    new_location = adjacent_location(location, direction)
    print(who, 'moves', direction, 'from',\
          location_to_string(location), 'to',\
          location_to_string(new_location) + ".\n")

def start():
    """Plays the Three Musketeers Game."""
    users_side = choose_users_side()
    board = create_board()
    print_instructions()
    print_board()
    while True:
        if has_some_legal_move_somewhere('M'):
            board = move_musketeer(users_side)
            print_board()
            if is_enemy_win():
                print("Cardinal Richleau's men win!")
                break
        else:
            print("The Musketeers win!")
            break
        if has_some_legal_move_somewhere('R'):
            board = move_enemy(users_side)
            print_board()
        else:
            print("The Musketeers win!")
            break

# start()
