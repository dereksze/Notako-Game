board = {'A': [0,1,2,3,4,5,6,7,8], 'B': [0,1,2,3,4,5,6,7,8], 'C': [0,1,2,3,4,5,6,7,8]}
empty_list = ['A','B','C']
center = []
last_move = 'Z'

def print_board() -> None:
    for key in board:
        print(f'{key:<7}',end='')
    print('')
    for i in range(3):
        for key in board:
            for j in range(3):
                print(board[key][i*3+j], end=' ')
            print(' ', end='')
        print()
    
def kill_board(arr) -> bool:
    if (arr[0]=='X' and arr[1]=='X' and arr[2]=='X') or (arr[3]=='X' and arr[4]=='X' and arr[5]=='X') or (arr[6]=='X' and arr[7]=='X' and arr[8]=='X'):
        return True
    if (arr[0]=='X' and arr[3]=='X' and arr[6]=='X') or (arr[1]=='X' and arr[4]=='X' and arr[7]=='X') or (arr[2]=='X' and arr[5]=='X' and arr[8]=='X'):
        return True
    if (arr[0]=='X' and arr[4]=='X' and arr[8]=='X') or (arr[2]=='X' and arr[4]=='X' and arr[6]=='X'):
        return True
    return False

def validate_input(input_str: str) -> tuple:
    if input_str[1].isdigit():
        return input_str[0], int(input_str[1]) 
    else: 
        return '_', -1
        
def AI() -> None:
    global last_move
    target = 'Z'
    num = -1
    if len(empty_list)==3:
        target = empty_list.pop(0)
        num = 4
        center.append(target)
    elif len(empty_list)==2:
        for i in board:
            if i not in empty_list:
                target = i
                for j in range(9):
                    temp = board[i].copy()
                    temp[j] = 'X'
                    if kill_board(temp):
                        num = j
                        break
    elif len(empty_list)==1:
        target = empty_list.pop(0)
        if len(center)==2:
            num = 0
        else:
            num = 4
            center.append(target)
    else:
        target = last_move if last_move in board else next(iter(board))
        if target not in center:
            for j in range(9):
                temp = board[target].copy()
                temp[j] = 'X'
                if kill_board(temp):
                    num = j
                    break
            if num==-1:
                for j in range(9):
                    if temp[j]=='X':
                        continue
                    temp = board[last_move].copy()
                    temp[j] = 'X'
                    test_pass = True
                    for k in range(9):
                        if temp[k]=='X':
                            continue
                        temp_2 = temp.copy()
                        temp_2[k] = 'X'
                        if kill_board(temp_2):
                            test_pass = False
                            break
                    if test_pass:
                        num = j
                        break
        else:
            if len(board)==3:
                for j in range(9):
                    temp = board[target].copy()
                    temp[j] = 'X'
                    if kill_board(temp):
                        num = j
                        break
            else:
                moves = {0:6, 1:3, 2:8, 3:8, 5:0, 6:8, 7:0, 8:6}
                count = 0
                last_digit = -1
                for i in range(9):
                    if board[target][i]=='X':
                        count+=1
                        last_digit = i if i!=4 else last_digit
                if count==2:
                    num = moves[last_digit]
                else:
                    for j in range(9):
                        if board[target][j]=='X':
                            continue
                        temp = board[target].copy()
                        temp[j] = 'X'
                        if not kill_board(temp):
                            num = j
                            break

    board[target][num] = 'X'
    if kill_board(board[target]):
        print(f'Board {target} is killed')
        board.pop(target)
    print(f'AI: {target}{num}')

def player_2() -> None:
    global last_move
    player_input = str(input('Player 2:'))
    board_name, number = validate_input(player_input)
    while board_name not in board or not str(number).isdigit() or board[board_name][number]=='X':
        print('Invalid input, please input again')
        player_input = str(input('Player 2:'))
        board_name, number = validate_input(player_input)
    if number==4:
        center.append(board_name)
    board[board_name][number] = 'X'
    if board_name in empty_list:
        empty_list.remove(board_name)
    if kill_board(board[board_name]):
        print(f'Board {board_name} is killed')
        board.pop(board_name)
    last_move = board_name

def main():
    while True:
        print("#"*30)
        print_board()
        AI()
        if len(board)==0:
            print('Player 2 win the game')
            break
        print_board()
        player_2()
        if len(board)==0:
            print('AI win the game')
            break
        print(center)
main()
