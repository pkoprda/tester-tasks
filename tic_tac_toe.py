#!/usr/bin/python3.9
# coding=utf-8

# Task 3 - Tic-tac-toe

from __future__ import annotations
import re
from argparse import ArgumentParser, ArgumentTypeError
from math import inf

def check_positive(value: str) -> int:
    """Checks if command line argument is integer greater than 2

    Parameters
    -------------------------------
    value : str
        value of input argument
    
    Returns
    -------------------------------
    value : int
        value of input argument
    """

    try:
        value = int(value)
        if value < 3:
            raise ValueError
    except ValueError:
        raise ArgumentTypeError(f"{value} must be an integer greater than 2")
    return value

def parse_arguments() -> tuple[int, int]:
    """Parse command line arguments

    Returns
    -------------------------------
    x : int
        x size of the grid
    y : int
        y size of the grid
    """

    parser = ArgumentParser(description="Tic-tac-toe game")
    parser.add_argument('x', metavar='X', type=check_positive, help='x size of the grid')
    parser.add_argument('y', metavar='Y', type=check_positive, help='x size of the grid')
    args = parser.parse_args()
    return args.x, args.y

def parse_command(x_size: int, y_size: int, grid: list):
    """Parses input command from user

    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid
    grid : list
        2d list of grid
    """

    player, robot = 'x', 'o'
    while(True):
        command = input('Insert command: ')
        if command == 'start':
            grid = create_grid(x_size, y_size)
            player, robot = 'o', 'x'
            robot_move(x_size, y_size, grid, robot)
        elif re.match(r'^\d* \d*$', command):
            player_won = opponent_move(x_size, y_size, grid, command, player)
            if player_won == False:
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

def create_grid(x_size: int, y_size: int) -> list:
    """Creates grid with size of `x_size` and `y_size` parameters

    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid

    Returns
    -------------------------------
    grid : list
        2d list of grid
    """

    grid = []
    for _ in range(y_size):
        row = [' '] * x_size
        grid.append(row)
        print('+---' * x_size + '+')
        print('|   ' * x_size + '|')
    print('+---' * x_size + '+\n')
    return grid

def update_grid(x_size: int, y_size: int, grid: list, x: int, y: int, player: str) -> bool:
    """Adds character `x` or character `o` to the grid

    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid
    grid : list
        2d list of grid
    x : int
        first coordinate
    y : int
        second coordinate
    player : str
        character `x` or `o`

    Returns
    -------------------------------
        True if Player x or Player o has won or it's a tie, otherwise False
    """

    if x >= x_size or y >= y_size or grid[x][y] != ' ':
        print('wrong')
        return False
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

def opponent_move(x_size: int, y_size: int, grid: list, command: str, player: str='x') -> bool:
    """Move of player 1

    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid
    grid : list
        2d list of grid
    command : str
        command from stdin with two integer values separated by whitespace
    player: (str, optional)
        Character `x` or `o` which specify player. Default value: `x`

    Returns
    -------------------------------
        True if Player x or Player o has won or it's a tie, otherwise False
    """

    x, y = int(command.split()[0]), int(command.split()[1])
    value = update_grid(x_size, y_size, grid, x, y, player)
    return value

def robot_move(x_size: int, y_size: int, grid: list, player: str='o') -> bool:
    """Move of player 2

    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid
    grid : list
        2d list of grid
    player : (str, optional)
        Character `x` or `o` which specify player. Default value: `o`

    Returns
    -------------------------------
        True if Player x or Player o has won or it's a tie, otherwise False
    """

    bestScore = -inf
    for i in range(y_size):
        for j in range(x_size):
            if grid[i][j] == ' ':
                grid[i][j] = player
                if player == 'o':
                    score = minimax(x_size, y_size, grid, 0, True)
                else:
                    score = minimax(x_size, y_size, grid, 0, False)
                grid[i][j] = ' '
                if score > bestScore:
                    bestScore = max(bestScore, score)
                    x, y = i, j
    print(f"Robot's move: {x} {y}")
    value = update_grid(x_size, y_size, grid, x, y, player)
    return value

def minimax(x_size: int, y_size: int, grid: list, depth: int, is_maximizing: bool) -> float:
    """Minimax algorithm

    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid
    grid : list
        2d list of grid
    depth : int
        current depth of minimax algorithm
    is_maximizing : bool
        specify if robot is first or second player
    
    Returns
    -------------------------------
    best_score : float
        best score for current `depth`
    """

    if is_maximizing:
        best_score = -inf
        for i in range(y_size):
            for j in range(x_size):
                if grid[i][j] == ' ':
                    grid[i][j] = 'x'
                    score = minimax(x_size, y_size, grid, depth + 1, False)
                    grid[i][j] = ' '
                    best_score = max(best_score, score)
        return best_score
    else:
        best_score = inf
        for i in range(y_size):
            for j in range(x_size):
                if grid[i][j] == ' ':
                    grid[i][j] = 'o'
                    score = minimax(x_size, y_size, grid, depth + 1, True)
                    grid[i][j] = ' '
                    best_score = min(best_score, score)
        return best_score

def new_game(x_size: int, y_size: int) -> list:
    """Creates new game if the user wants
    
    Parameters
    -------------------------------
    x_size : int
        x size of the grid
    y_size : int
        y size of the grid

    Returns
    -------------------------------
    grid : list
        empty grid
    """

    while(True):
        new_game = input('New game? (y/n): ')
        if new_game.lower() == 'y':
            grid = create_grid(x_size, y_size)
            return grid
        elif new_game.lower() == 'n':
            exit(0)

def has_won(grid: list, player: str) -> bool:
    """Finds out if one of the player has won

    Parameters
    -------------------------------
    grid : list
        2d list of grid
    player : str
        current player, `x` or `o`
    
    Returns
    -------------------------------
        True if current player has 3 marks in horizontal, vertical or diagonal row, otherwise False
    """

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
    x_size, y_size = parse_arguments()
    grid = create_grid(x_size, y_size)
    parse_command(x_size, y_size, grid)
