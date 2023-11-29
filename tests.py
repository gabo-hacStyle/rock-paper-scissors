# This file contains the test cases for the application.

# Create a 3x3 matrix for testing
matrix = [[1,2,32, 234, 45, 56,23, 34, 34, 34, 332, 43, 54, 33],[47,352,634],[73,18,29]]
print('Matriz ->', matrix)

# Print a separator for clarity
print('--' * 20)

# Print the odd numbers in the matrix
print("Numeros impares de la matriz")
print('--' * 20)

# Iterate over each element in the matrix
for element in matrix:
    # Iterate over each item in the element
    for item in element:
        # If the item is odd (remainder of division by 2 is not 0)
        if item % 2 != 0:
            # Print the item and its position in the matrix
            print(item, "esta en la posicion =>", "(", matrix.index(element), ",", element.index(item), ")") 

# Print a separator for clarity
print('--' * 20)

# Print the even numbers in the matrix
print("Numeros pares de la matriz")
print('--' * 20)

# Iterate over each element in the matrix
for element in matrix:
    # Iterate over each item in the element
    for item in element:
        # If the item is even (remainder of division by 2 is 0)
        if item % 2 == 0:
            # Print the item and its position in the matrix
            print(item, "esta en la posicion =>", "(", matrix.index(element), ",", element.index(item), ")")