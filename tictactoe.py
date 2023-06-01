game = [[0,0,0],
        [0,0,0],
        [0,0,0]]

game1 = [[1,1,1],
         [0,1,0],
         [0,1,0]]

game2 = [[2,0,1],
         [2,0,0],
         [2,2,1]]

game3 = [[1,0,0],
         [0,1,0],
         [0,0,1]]
'''
diags = []
for ix in range(len(game3)):
    diags.append(game3[ix][ix])
print(diags)
'''
diags = []
for col, row in enumerate(reversed(range(len(game3)))):
    diags.append(game3[row][col])

if game3[2][0] == game [1][1] == game3[0][2]:
    print("winner")

diags = []
for ix in range(game3[ix][ix]):
    diags.append(game3[ix][ix])
if game3[0][0] == game [1][1] == game[2][2]:
    print("winner")

def verticalWin(current_game):
    for col in range(len(current_game)):
        check = []
        for row in current_game:
            check.append(row[col])
        if check.count(check[0]) == len(check) and check[0] != 0:
            print("Winner!")

#verticalWin(game2)
#horizontal winner
def horizontalWin(current_game):
    for row in current_game:
        if row.count(row[0]) == len(row) and row[0] != 0:
            print(row)
            print("Winner!")

#horizontalWin(game1)

def game_board(game_map, player = 0, row = 0, column = 0, just_display=False):
    try:
        print("   0  1  2")
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)

        return game_map
    except IndexError as e:
        print("Error: make sure you input row/column as 0, 1, or 2?",e)
    except Exception as e:
        print("Something went very wrong!", e)

#game = game_board(game,just_display=True)
#game = game_board(game_board,player=1, row=3, column=1)


