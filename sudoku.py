#sudoku using backtracking
def find_next_empty(puzzle):
	#finds row,col which is not filled
	#return row,col tuple or None,None
	for r in range(9):
		for c in range(9):
			if puzzle[r][c] == -1:
				return r,c

	return None,None

def is_valid(puzzle,guess,row,col):
	#check if guess is already in that row,col or the 3X3 box
	#row
	row_vals=puzzle[row]
	if guess in row_vals:
		return False

	col_vals=[]
	for i in range(9):
		col_vals.append(puzzle[i][col])

	if guess in col_vals:
		return False
		
	row_start=(row//3)*3
	col_start=(col//3)*3

	for r in range(row_start,row_start+3):
		for c in range(col_start,col_start+3):
			if puzzle[r][c]==guess:
				return False

	#passes all checks, so guess is valid
	return True			

def solve_sudoku(puzzle):
	#puzzle is a list of lists
	#mutates puzzle to become the solutions since lists are mutable
	row,col=find_next_empty(puzzle)

	if row is None:
		return True #puzzle solved

	for guess in range(1,10):
		if is_valid(puzzle,guess,row,col):
			#if valid, place guess in puzzle
			puzzle[row][col]=guess #mutating

			#recurse
			if solve_sudoku(puzzle):
				return True

		#if not valid or if our guess does not solve the puzzle,
		#we need to backtrack and try a new number
		puzzle[row][col]=-1 #reset the guess

	#if none of the numbers we try work, then this puzzle is unsolvable
	return False

if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    if(solve_sudoku(example_board)):
    	print("\nThe puzzle is solvable! :)\n")
    	print(example_board)
    else:
    	print("\nThe puzzle is not solvable! :(\n")	



