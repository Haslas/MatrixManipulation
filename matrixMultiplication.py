print("=====Matrix Multiplication=====")
print("Use CSV file to declare matrices.")
def multiplyMatrix(matrixA,matrixB):
    #Function used for two matrices
    matrixADimensions=(len(matrixA),len(matrixA[0]))
    matrixBDimensions=(len(matrixB),len(matrixB[0]))
    if matrixADimensions[1]==matrixBDimensions[0]:
        productMatrix=[]
        for row in matrixA:
            productMatrix.append([])
        for rowIndex, row in enumerate(matrixA):
            for columnIndex, column in enumerate(matrixB[rowIndex]):
                currentValue=0
                for num in range(matrixADimensions[1]):
                    currentValue+=matrixA[rowIndex][num]*matrixB[num][columnIndex]
                productMatrix[rowIndex].append(currentValue)
        return productMatrix
    else:
        print("Matrices non-commuteable.")
        return None

def multiplyMatrices(*matrices):
    #Function used for any number of matrices
    numberOfMatrices=len(matrices)
    currentMatrixIndex=0
    productMatrix=multiplyMatrix(matrices[currentMatrixIndex],matrices[currentMatrixIndex+1])
    currentMatrixIndex+=2
    while currentMatrixIndex < numberOfMatrices:
        productMatrix=multiplyMatrix(productMatrix,matrices[currentMatrixIndex])
        currentMatrixIndex+=1
    if productMatrix==None:
        print("Matrices non-commuteable.")
    return productMatrix
