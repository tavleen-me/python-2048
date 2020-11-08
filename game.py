from _2048 import (areMatrixEqual, injectRandomValue, isMatrixFull, createMatrix, printMatrix,
                   shiftMatrixBottom, shiftMatrixTop, shiftMatrixRight, shiftMatrixLeft, isGameOver)


def main():

    matrixChanged = True
    score = 0
    mat = createMatrix()

    while True:
        if isGameOver(mat):
            print("Game Over")
            printMatrix(mat, score)
            return

        if matrixChanged:
            mat = injectRandomValue(mat)

        if isGameOver(mat):
            print("Game Over")
            printMatrix(mat, score)
            return

        if matrixChanged:
            mat = injectRandomValue(mat)

        printMatrix(mat, score)

        print("Enter the input: ", end="")
        x = input()
        if x == 'w':
            shiftedMat, s = shiftMatrixTop(mat)
        elif x == 'a':
            shiftedMat, s = shiftMatrixLeft(mat)
        elif x == 's':
            shiftedMat, s = shiftMatrixBottom(mat)
        elif x == 'd':
            shiftedMat, s = shiftMatrixRight(mat)
        else:
            print("invalid input")

        score += s

        matrixChanged = not areMatrixEqual(mat, shiftedMat)
        mat = shiftedMat

        print('You entered ' + x)


main()
