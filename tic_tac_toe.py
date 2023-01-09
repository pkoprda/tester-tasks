#!/usr/bin/python3.9
# coding=utf-8

# Task 3

import re
from argparse import ArgumentParser, ArgumentTypeError
from math import inf

def check_positive(value):
    try:
        value = int(value)
        if value <= 2:
            raise ValueError
    except ValueError:
        raise ArgumentTypeError(f"{value} must be an integer greater than 2")
    return value

def parse_arguments():        
    parser = ArgumentParser(description="Tic-tac-toe game")
    parser.add_argument('x', metavar='X', type=check_positive, help='x size of the grid')
    parser.add_argument('y', metavar='Y', type=check_positive, help='x size of the grid')
    args = parser.parse_args()
    if args.x != args.y:
        print("Size of the grid cannot be different for each dimension")
        exit(1)
    return args

def parse_command(x_size, y_size, grid):
    player, robot = 'x', 'o'
    while(True):
        command = input('Insert command: ')
        if command == 'start':
            grid = create_grid(x_size, y_size)
            player, robot = 'o', 'x'
            robot_move(x_size, y_size, grid, robot)
        elif re.match(r'^\d* \d*$', command):
            player_won = opponent_move(x_size, y_size, grid, command, player)
            if player_won == 'wrong':
                pass
            elif player_won:
                grid = new_game(x_size, y_size)
            else:
                player_won = robot_move(x_size, y_size, grid, robot)
                if player_won:
                    grid = new_game(x_size, y_size)
        elif command == 'exit':
            exit(0)
        else:
            print('Invalid command, try again')

def create_grid(x_size, y_size):
    grid = []
    for _ in range(y_size):
        row = [' '] * x_size
        grid.append(row)
        print('+---' * x_size + '+')
        print('|   ' * x_size + '|')
    print('+---' * x_size + '+\n')
    return grid

def update_grid(x_size, y_size, grid, x, y, player):
    if x >= x_size or y >= y_size or grid[x][y] != ' ':
        print('wrong')
        return 'wrong'
    grid[x][y] = player
    for i in range(y_size):
        print('+---' * x_size + '+')
        for j in range(x_size):
            print(f"| {grid[i][j]} ", end='')
        print('|')
    print('+---' * x_size + '+\n')
    if(has_won(grid, player)):
        print(f"Player {player} has won!\n")
        return True
    elif not ' ' in sum(grid, []):
        print(f"It's a tie!")
        return True

def opponent_move(x_size, y_size, grid, command, player='x'):
    x, y = int(command.split()[0]), int(command.split()[1])
    value = update_grid(x_size, y_size, grid, x, y, player)
    return value

def robot_move(x_size, y_size, grid, robot='o'):
    bestScore = -inf
    for i in range(y_size):
        for j in range(x_size):
            if grid[i][j] == ' ':
                grid[i][j] = robot
                if robot == 'o':
                    score = minimax(x_size, y_size, grid, 0, True)
                else:
                    score = minimax(x_size, y_size, grid, 0, False)
                grid[i][j] = ' '
                if score > bestScore:
                    bestScore = max(bestScore, score)
                    x, y = i, j
    print(f"Robot's move: {x} {y}")
    value = update_grid(x_size, y_size, grid, x, y, robot)
    return value

def minimax(x_size, y_size, grid, depth, is_maximizing):
    if is_maximizing:
        bestScore = -inf
        for i in range(y_size):
            for j in range(x_size):
                if grid[i][j] == ' ':
                    grid[i][j] = 'x'
                    score = minimax(x_size, y_size, grid, depth + 1, False)
                    grid[i][j] = ' '
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = inf
        for i in range(y_size):
            for j in range(x_size):
                if grid[i][j] == ' ':
                    grid[i][j] = 'o'
                    score = minimax(x_size, y_size, grid, depth + 1, True)
                    grid[i][j] = ' '
                    bestScore = min(bestScore, score)
        return bestScore

def new_game(x_size, y_size):
    while(True):
        new_game = input('New game? (y/n): ')
        if new_game.lower() == 'y':
            grid = create_grid(x_size, y_size)
            return grid
        elif new_game.lower() == 'n':
            exit(0)

def has_won(grid, player):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if j+2 < len(grid[i]) and grid[i][j] == grid[i][j+1] == grid[i][j+2] == player:
                return True
            if i+2 < len(grid) and grid[i][j] == grid[i+1][j] == grid[i+2][j] == player:
                return True
            if i+2 < len(grid) and j+2 < len(grid[i]):
                if grid[i][j+2] == grid[i+1][j+1] == grid[i+2][j] == player:
                    return True
                if grid[i][j] == grid[i+1][j+1] == grid[i+2][j+2] == player:
                    return True
    return False


if __name__ == "__main__":
    args = parse_arguments()
    grid = create_grid(args.x, args.y)
    parse_command(args.x, args.y, grid)
