import random 
test_table = ['#','1','2','3','4','5','6','7','8','9']

print("This is a 2 player tic tac toe game on a 3x3 grid. Use the numpad on your keyboard to play")
print("")
print("The basic motive of the game is to use strategy to place your markers in a row of 3.")
print("")
print("This could be in a horizontal, vertical or diagonal line, below is a sample grid")
print("")

def display_table(table):

    print('   |   |')
    print(' ' + table[7] + ' | ' + table[8] + ' | ' + table[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + table[4] + ' | ' + table[5] + ' | ' + table[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + table[1] + ' | ' + table[2] + ' | ' + table[3])
    print('   |   |')


def game(): 

    picker = random.randint(1,3)
    if picker == 1:
        print("")
        print("Player 1 is X")
        print("")
        print("Player 2 is O")
        print("")
        p1marker = "X"
        p2marker = "O"
    else:
        print("")
        print("Player 1 is O")
        print("")
        print("Player 2 is X")
        print("")
        p2marker = "X"
        p1marker = "O"
    
    
    total = 9
    flag = False
    while True:
    
        print("Player 1's turn!")
        p1turn = int(input("Enter the position on which you want to put your marker in: "))
        print("")
        total -= 1
        test_table[p1turn] = p1marker
        display_table(test_table)
        print("")
        if total == 0:
            break
        elif total != 0:
             if (test_table[1] == 'X' and test_table[2] == "X" and test_table[3] == "X") or (test_table[4] == 'X' and test_table[5] == "X" and test_table[6] == "X") or (test_table[7] == "X" and test_table[8] == "X" and test_table[9] == "X"):
                flag = True
                print("X is Winner!")
                break
             
             elif (test_table[1] == 'O' and test_table[2] == "O" and test_table[3] == "O") or (test_table[4] == 'O' and test_table[5] == "O" and test_table[6] == "O") or (test_table[7] == "O" and test_table[8] == "O" and test_table[9] == "O"):
                flag = True
                print("O is Winner!")
                break
              
             elif (test_table[1] == "X" and test_table[4] == "X" and test_table[7] == "X") or (test_table[2] == "X" and test_table[5] == "X" and test_table[8] == "X") or (test_table[3] == "X" and test_table[6] == "X" and test_table[9] == "X"):
                  flag = True
                  print("X is Winner!")
                  break

             elif (test_table[1] == "O" and test_table[4] == "O" and test_table[7] == "O") or (test_table[2] == "O" and test_table[5] == "O" and test_table[8] == "O") or (test_table[3] == "O" and test_table[6] == "O" and test_table[9] == "O"):
                  flag = True
                  print("O is Winner!")
                  break
              
             elif (test_table[1] == "X" and test_table[5] == "X" and test_table[9] == "X") or (test_table[3] == "X" and test_table[5] == "X" and test_table[7] == "X"):
                  flag = True
                  print("X is Winner!")
                  break
              
             elif (test_table[1] == "O" and test_table[5] == "O" and test_table[9] == "O") or (test_table[3] == "O" and test_table[5] == "O" and test_table[7] == "O"):
                  flag = True
                  print("")
                  print("O is Winner!")
                  break
              
             elif total == 0 and flag == False:
                  print("TIE!")

             else:
                 pass
        
        print("Player 2's turn!")
        p2turn = int(input("Enter the position on which you want to put your marker in: "))
        print("")
        total -= 1
        test_table[p2turn] = p2marker
        display_table(test_table)
        print("")
        if total == 0:
            break
        elif total != 0:
              if (test_table[1] == 'X' and test_table[2] == "X" and test_table[3] == "X") or (test_table[4] == 'X' and test_table[5] == "X" and test_table[6] == "X") or (test_table[7] == "X" and test_table[8] == "X" and test_table[9] == "X"):
                flag = True
                print("X is Winner!")
                break
             
              elif (test_table[1] == 'O' and test_table[2] == "O" and test_table[3] == "O") or (test_table[4] == 'O' and test_table[5] == "O" and test_table[6] == "O") or (test_table[7] == "O" and test_table[8] == "O" and test_table[9] == "O"):
                flag = True
                print("O is Winner!")
                break
              
              elif (test_table[1] == "X" and test_table[4] == "X" and test_table[7] == "X") or (test_table[2] == "X" and test_table[5] == "X" and test_table[8] == "X") or (test_table[3] == "X" and test_table[6] == "X" and test_table[9] == "X"):
                  flag = True
                  print("X is Winner!")
                  break

              elif (test_table[1] == "O" and test_table[4] == "O" and test_table[7] == "O") or (test_table[2] == "O" and test_table[5] == "O" and test_table[8] == "O") or (test_table[3] == "O" and test_table[6] == "O" and test_table[9] == "O"):
                  flag = True
                  print("O is Winner!")
                  break
              
              elif (test_table[1] == "X" and test_table[5] == "X" and test_table[9] == "X") or (test_table[3] == "X" and test_table[5] == "X" and test_table[7] == "X"):
                  flag = True
                  print("X is Winner!")
                  break
              
              elif (test_table[1] == "O" and test_table[5] == "O" and test_table[9] == "O") or (test_table[3] == "O" and test_table[5] == "O" and test_table[7] == "O"):
                  flag = True
                  print("")
                  print("O is Winner!")
                  break
              
              elif total == 0 and flag == False:
                  print("TIE!")

              else:
                 pass
      
display_table(test_table)         
game()