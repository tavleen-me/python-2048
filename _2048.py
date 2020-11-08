import random

def areMatrixEqual(mat1, mat2):
    for row1, row2 in zip(mat1, mat2):
        for ele1, ele2 in zip(row1, row2):
            if ele1 != ele2:
                return False
    return True

"""
Create a board
"""
def createMatrix():
    return [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

def isMatrixFull(mat):
    for row in mat:
        for item in row:
            if item == 0:
                return False
    return True


def injectRandomValue(mat):
    if isMatrixFull(mat):
        return mat

    retMat = [
        [ mat[0][0], mat[0][1], mat[0][2], mat[0][3] ],
        [ mat[1][0], mat[1][1], mat[1][2], mat[1][3] ],
        [ mat[2][0], mat[2][1], mat[2][2], mat[2][3] ],
        [ mat[3][0], mat[3][1], mat[3][2], mat[3][3] ]
    ]

    while True:
        r = random.randrange(0, 4) # r is index value of row
        c = random.randrange(0, 4) # c is index value of column
        if retMat[r][c] == 0:
            retMat[r][c] = (random.randrange(0, 2) + 1) * 2
            return retMat


"""
Takes in in_arr array with possible int values being 0 and non zero values
Returns a copy of in_arr array with zero elements removed
0s kadd do in_arr vicho
"""
def compact(in_arr):
    return [ i for i in in_arr if i != 0 ]


"""
Returns the in_arr padded with 0s at the end to match target_len
Target length jinni len in_arr de banao by adding 0s at the end
"""
def addPadding(in_arr, target_len=4):
    if len(in_arr) < target_len:
        padding = target_len - len(in_arr)
        return in_arr + [0] * padding
    else:
        return in_arr


"""
Merge the adjacent values into a single value in in_arr when adjacent values are
equal by summing them
in_arr de array di adjacent equal elements de naal merge karna by summing them up
"""
def mergeAdjacentValues(in_arr):
    arr = in_arr[:]
    score = 0
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            arr[i] = arr[i] + arr[i+1]
            score = arr[i]
            arr[i+1] = 0
    return arr, score


"""
Shift left for 1d array
"""
def shiftLeft1DArray(in_arr):
    arr = in_arr[:]
    # print('A arr: ', arr)

    arr = compact(arr)
    # print('B arr: ', arr)

    arr, score = mergeAdjacentValues(arr)
    # print('C arr: ', arr)

    arr = compact(arr)
    # print('D arr: ', arr)

    arr = addPadding(arr, len(in_arr))
    # print('E arr: ', arr)

    return arr, score

"""
Shift right for 1d array
"""
def shiftRight1DArray(in_arr):
    arr = in_arr[:]
    arr.reverse()
    arr, score = shiftLeft1DArray(arr)
    arr.reverse()
    return arr, score


# # A: [2, 2, 2, 2]
# # B: [2, 2, 2, 2]
# # C: [4, 0, 4, 0]
# # D: [4, 4]
# # E: [4, 4, 0, 0]

# """
# Shift left Matrix
# """
def shiftMatrixLeft(in_mat):
    ret_mat = []
    score = 0
    for row in in_mat:
        arr, s = shiftLeft1DArray(row)
        score += s
        ret_mat.append(arr)

    return ret_mat, score


def printMatrix(mat, score):
    #print(f'Score: {score}')  #idk why ?
    print('Score: ' + str(score))
    for row in mat:
        for item in row:
            if item == 0:
                print('-\t', end='')
            else:
                print(str(item) + '\t', end='')
        print()
    print()



"""
Shift right Matrix
"""
def shiftMatrixRight(in_mat):
    ret_mat = []
    score = 0
    for row in in_mat:
        arr, s = shiftRight1DArray(row)
        score += s
        ret_mat.append(arr)

    return ret_mat, score


def rotateMatrixClockwise90(in_mat):
    return [
        [ in_mat[3][0], in_mat[2][0], in_mat[1][0], in_mat[0][0] ],
        [ in_mat[3][1], in_mat[2][1], in_mat[1][1], in_mat[0][1] ],
        [ in_mat[3][2], in_mat[2][2], in_mat[1][2], in_mat[0][2] ],
        [ in_mat[3][3], in_mat[2][3], in_mat[1][3], in_mat[0][3] ],
    ]

def rotateMatrixAntiClockwise90(in_mat):
    return (
        rotateMatrixClockwise90(
            rotateMatrixClockwise90(
                rotateMatrixClockwise90(
                    in_mat
                )
            )
        )
    )


"""
Shift bottom Matrix
"""
def shiftMatrixBottom(in_mat):
    # rotate matrix clockwise by 90 degree
    ret_mat = rotateMatrixClockwise90(in_mat)

    # left shift matrix
    ret_mat, score = shiftMatrixLeft(ret_mat)

    # rotate matrix clockwise by 90 degree
    ret_mat = rotateMatrixAntiClockwise90(ret_mat)

    # return
    return ret_mat, score


def shiftMatrixTop(in_mat):
    # rotate matrix clockwise by 90 degree
    ret_mat = rotateMatrixClockwise90(in_mat)

    # left shift matrix
    ret_mat, score = shiftMatrixRight(ret_mat)

    # rotate matrix clockwise by 90 degree
    ret_mat = rotateMatrixAntiClockwise90(ret_mat)

    # return
    return ret_mat, score


def isGameOver(mat):
    if not isMatrixFull(mat):
        return False
    else:
        # do adjacent values same ya return False
        for row in range(4):
            for col in range(4):
                # print(str(row), str(col))
                if col != 3 and mat[row][col] == mat[row][col+1]:
                    return False
                if row != 3 and mat[row][col] == mat[row+1][col]:
                    return False
    return True

