# Description: This file contains the test cases for the application.
#Create a matrix of 3x3 and test the functions

matrix = [[1,2,32, 234, 45, 56,23, 34, 34, 34, 332, 43, 54, 33],[47,352,634],[73,18,29]]  #matrix of 3x3
print('Matriz ->', matrix)

print('--' * 20)
print("Numeros impares de la matriz")
print('--' * 20)
for element in matrix:
    for item in element:
        if item % 2 != 0:
            print(item, "esta en la posicion =>", "(", matrix.index(element), ",", element.index(item), ")") 
print('--' * 20)
print("Numeros pares de la matriz")
print('--' * 20)

for element in matrix:
    for item in element:
        if item % 2 == 0:
            print(item, "esta en la posicion =>", "(", matrix.index(element), ",", element.index(item), ")")