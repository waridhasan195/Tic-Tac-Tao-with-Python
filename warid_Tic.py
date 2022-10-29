

board = [".", ".", ".",
         ".", ".", ".",
         ".", ".", "."]

current_player = "x"
game_still_going = True

def display_board():
  print("\n")
  print(board[0] + " | " + board[1]+ " | " + board[2])
  print(board[3] + " | " + board[4]+ " | " + board[5])
  print(board[6] + " | " + board[7]+ " | " + board[8])
  print("\n")

def play_game():
  display_board()
  while game_still_going:
    current_player_input()
    who_won_game()
    flip_player()



def current_player_input():
  global current_player
  user_input = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
  player_input = input("Please input your poisiton(1-9): ")

  user_input_validity = True

  while user_input_validity:
    while player_input not in user_input:
      player_input = input("Please input your poisiton(1-9): ")
    player_input = int(player_input)-1
    if board[player_input] == '.':
      user_input_validity = False
    else:
      print("Your Input Make Vaiolate for Tic Tac Tao, Please Input Again.. . . .")
  board[player_input] = current_player
  display_board()



def who_won_game():
  row_winner = check_rows()
  columns_winner = chck_columns()
  diagonal_winner = check_diagonal()

  if row_winner:
    print(row_winner + " win.")
  elif columns_winner:
    print(columns_winner + " win.")
  elif diagonal_winner:
    print(diagonal_winner + " win.")
  else:
    None




def check_rows():

  global game_still_going
  row_1 = board[0] == board[1] == board[2] != '.'
  row_2 = board[3] == board[4] == board[5] != '.'
  row_3 = board[6] == board[7] == board[8] != '.'

  if row_1 or row_2 or row_3:
    game_still_going = False
  
  if row_1:
    return board[0]
  elif row_1:
    return board[3]
  elif row_1:
    return board[6]
  else:
    return None

def chck_columns():
  global game_still_going
  
  column_1 = board[0] == board[3] == board[6] != '.'
  column_2 = board[1] == board[4] == board[7] != '.'
  column_3 = board[2] == board[5] == board[8] != '.'

  if column_1 or column_2 or column_3:
    game_still_going = False

  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  else:
    return None

def check_diagonal():
  global game_still_going

  diagonal_1 = board[6] == board[4] == board[2] != '.'
  diagonal_2 = board[0] == board[4] == board[8] != '.'

  if diagonal_1 or diagonal_2:
    game_still_going = False
  
  if diagonal_1:
    return board[6]
  elif diagonal_2:
    return board[0]
  else:
    return None
  
def flip_player():
  global current_player

  if current_player == "x":
    current_player = "O"
  elif current_player == "O":
    current_player = "x"
  else:
    return None

play_game()