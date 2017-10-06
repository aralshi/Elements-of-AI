#!/usr/bin/env python
# a0.py : Solve the N-Queens and N-Rooks problem!
# Ankita Alshi, 2017
# 
# The N-queen/N-rooks problem is: Given an empty NxN chessboard, place N rooks/queens on the board such that they
# can't take each other. 
#
# Comments:
# I have referenced following youtube link to understand the concept of backtracking algorithm
# https://youtu.be/xouin83ebxE
# First I implemented this logic with N*N board for storing current state. but everytime I was using only poisition
# of exsting queens/rooks. So modified the program to store list of positions of existing pieces on the board
# instead of the complete board which improved the performance.

import sys

# Count # of pieces in given row
# Count 1 for each position of existing piece on board with row same as passed to this function.
def count_on_row(board, row):
    sum = 0
    for pos in board:
        if (pos[0] == row):
            sum += 1
    return sum 

# Count # of pieces in given column
# Count 1 for each position of existing piece on board with col same as passed to this function.
def count_on_col(board, col):
    sum = 0
    for pos in board:
        if (pos[1] == col):
            sum += 1
    return sum 

# Count total # of pieces on board
# Count number of positions of existing pieces currently placed on the board
def count_pieces(board):
    sum = 0
    for a in board:
        sum += 1
    return sum

# Return a string with the board rendered in a human-friendly format for nqueens
# If row and col is same as position of existing queen on the board print "Q"
# If row and col is same as the unavailable position on the board print "X"
# Otherwise print "_"
def printable_board(board):
    result = ""
    for row in range(N):
        for col in range(N):
            if [row, col] in board:
                result += "Q "
            else:
                if ((row == x_row) and (col == x_col)):
                    result += "X "
                else:
                    result += "_ "
        result += "\n"
    return result

# Return a string with the board rendered in a human-friendly format for nrooks
# If row and col is same as position of existing rook on the board print "R"
# If row and col is same as the unavailable position on the board print "X"
# Otherwise print "_"
def printable_rboard(board):
    result = ""
    for row in range(N):
        for col in range(N):
            if [row, col] in board:
                result += "R "
            else:
                if ((row == x_row) and (col == x_col)):
                    result += "X "
                else:
                    result += "_ "
        result += "\n"
    return result

# Add a piece by adding position of new piece to board, and return a new board (doesn't change original)
def add_piece(board, row, col):
    new_board = [a for a in board]
    new_board.append([row, col])
    return new_board

# Find whether given tile is under attack by existing queens
def under_attack(board, r, c):
    for pos in board:
        if (r == pos[0] or \
            c == pos[1] or \
            ((r - c) == (pos[0] - pos[1])) or \
            ((r + c) == (pos[0] + pos[1]))):
            return True
    return False

# Find whether given tile is under attack by existing rooks
def under_attack_rook(board, r, c):
    for pos in board:
        if (r == pos[0] or \
            c == pos[1]):
            return True
    return False

# Get list of successors of given board state for nqueens
# Check if a block is available to place a piece or is safe from other queens present on the board
# Successor is created by placing a new queen on one row at a time
def qsuccessors(board):
    row = count_pieces(board)
    s = []
    for col in range(0, N):
        next_board = board
        if (row == 0):
            if (no_unavailable):
                s.append(add_piece(board, row, col))
            else:
                if ((row != x_row) or (col != x_col)):
                    s.append(add_piece(board, row, col))
        else:
            if (not under_attack(board, row, col)):
                if (no_unavailable):
                    s.append(add_piece(board, row, col))
                else:
                    if ((row != x_row) or (col != x_col)):
                        s.append(add_piece(board, row, col))
    return s

# Get list of successors of given board state for nrooks
# Check if a block is available to place a piece or is safe from other rooks present on the board
# Successor is created by placing a new rook on one row at a time
def rsuccessors(board):
    row = count_pieces(board)
    s = []
    for col in range(0, N):
        next_board = board
        if (row == 0):
            if (no_unavailable):
                s.append(add_piece(board, row, col))
            else:
                if ((row != x_row) or (col != x_col)):
                    s.append(add_piece(board, row, col))
        else:
            if (not under_attack_rook(board, row, col)):
                if (no_unavailable):
                    s.append(add_piece(board, row, col))
                else:
                    if ((row != x_row) or (col != x_col)):
                        s.append(add_piece(board, row, col))
    return s

# Check if board is a goal state
def is_goal(board):
    return count_pieces(board) == N and \
        all( [ count_on_row(board, r) <= 1 for r in range(0, N) ] ) and \
        all( [ count_on_col(board, c) <= 1 for c in range(0, N) ] )

# Solve n-rooks / n-queens!
def solve(initial_board):
    fringe = [initial_board]
    if (piece == "nrook"):
        while len(fringe) > 0:
            for s in rsuccessors( fringe.pop() ):
                if is_goal(s):
                    return(s)
                fringe.append(s)
        return False
    if (piece == "nqueen"):
        while len(fringe) > 0:
            for s in qsuccessors( fringe.pop() ):
                if is_goal(s):
                    return(s)
                fringe.append(s)
        return False


# Input from command line: 1. piece type (nrook / nqueen) 2. Number of pieces 
#                         3. row of unavailable position 4. col of unavailable position
piece = sys.argv[1]
N = int(sys.argv[2])
x_row = int(sys.argv[3]) - 1
x_col = int(sys.argv[4]) - 1

no_unavailable = False
# if argument 3 and 4 is 0 means that no unavailable position on the board. Set flag for that.
if ((x_row == -1) or (x_col == -1)):
    no_unavailable = True

# The board is stored as a list-of-lists. Each inner list is position of existing piece on the board.
# one piece is placed at a time in the successor function.
# A zero in a given square indicates no piece, and a 1 indicates a piece.

initial_board = []
# Call function solve by passing initial board to find solution
solution = solve(initial_board)

# Print the N-queens board
if (piece == "nqueen"):
    print (printable_board(solution) if solution else "Sorry, no solution found. :(")

# Print the N-rooks board
if (piece == "nrook"):
    print (printable_rboard(solution) if solution else "Sorry, no solution found. :(")
