# Author: Helen Hua
# Date: May 10, 2022
# Purpose: A virtual connect four game. First player to get 4 in a row before the other player wins

# Function that prints the playing board
def print_board():
  #Initiation of section a and d 
  section_a = "+---+---+---+---+---+---+---+"
  section_d = "+---+---+---+---+---+---+---+"
  
  # Print the first line of numbers
  print("  1   2   3   4   5   6   7  ")

  # Prints 6 boxed rows
  for row in range(6):
    print(section_a)
    
    #resets section_b to an empty string for each row
    section_b = ""

    # Prints 7 columns
    for col in range(7):
      section_b += ("| " + str(board[row][col]) + " ")
     
    # Prints row B the last line on the right of each B row
    print(section_b + "|")
   
  #After the loops iterate, print the final section d once to close the board off
  print(section_d)

# Checks the left of a piece on the board for same pieces and returns how many pieces in a row there are to the left of a piece
def left(array, row, col, x_or_o):
  counter = 0
  while col >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    col-=1
  
  return counter  

# Checks the top of a piece on the board for same pieces and returns how many pieces in a row there are above it
def up(array, row, col, x_or_o):
  counter = 0
  while row >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
 
  return counter  
  
# Checks the top left diagonal of a piece on the board for same pieces and returns how many pieces in a row there are diagonal to it
def top_left(array, row, col, x_or_o):
  counter = 0
  while row >= 0 and col >= 0:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
    col-=1
 
  return counter  

# Checks the top right diagonal of a piece on the board for same pieces and returns how many pieces in a row there are diagonal to it
def top_right(array, row, col, x_or_o):
  counter = 0
  while row >= 0 and col <= 6:
    if array[row][col] == x_or_o:
      counter+=1
    if array[row][col] != x_or_o:
      break
    row-=1
    col+=1
 
  return counter  

# Returns true if there is a 4 in a row, otherwise false
def win(array, x_or_o):
  # Initiate the win state as false to begin
  win = False

  # Traverses through the board array and looks for X or O depending on its argument then initiates a score keeping counter to 1. If there are ever 4 in a row horizontally, vertically or diagonally, win will become true
  for row in range(5, -1, -1):
    for col in range(0,7,1):
      
      if array[row][col] == x_or_o:
        counter =1
        
        if counter - 1  + left(array, row, col, x_or_o) >= 4:
          win = True

        if counter - 1 + up(array, row, col, x_or_o)  >= 4:
          win = True

        if counter - 1 + top_left(array, row, col, x_or_o) >= 4 or counter - 1 + top_right(array, row, col, x_or_o) >= 4:
          win = True

  return win            

  
#main code

#Initiation of board: 6 by 7 list of spaces
board = [
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' '], 
[' ', ' ',' ', ' ', ' ', ' ', ' ']]

#Initiates the round counter to 1
counter = 1
game_won = False
welcome_message = """Welcome to Helen's custom made connect 4 game! 

Connect 4 in a row before your opponent to win the game!

"""

# Starts the game off by printing a welcome message and the board by calling the print board function
print(welcome_message)
print_board()

# Continues iterating through the game until there is a winner or the entire board is filled after 42 turns
while(not game_won and counter <= 42):
  # Alternates between player O and player X's turns depending on the turn number
  if counter % 2 == 1:
    turn = 'O'
  else:
    turn = 'X'
  
  #scan col input from user
  user_input = input("Enter a column number: ")

  # Finds the index that corresponds to the input
  col = int(user_input) - 1

  # Checks the bottom most spot of the column on the playing board and the piece (either X or O) will fall into the first empty spot. If the entire column is full user's turn will be skipped
  for row in range(5,-1,-1):
    if board[row][col] == ' ':
      board[row][col] = turn
      break
  
  #Prints the board so the user can see what they inputted
  print_board()
  
  # Check for a winner
  game_won = win(board, turn)
  
  # If no winner, at the end of each turn, inrease the counter by one 
  counter+=1

# Prints the winner when the game ends with a 4 in a row
print("Game over! Player " + turn + " is the winner!")
