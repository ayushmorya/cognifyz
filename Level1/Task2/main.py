# Number of rows for the pyramid
rows = 9

# Outer loop for each row
for i in range(1, rows + 1):
    # Print spaces before the numbers to center the pyramid
    for j in range(rows - i):
        print(" ", end="")
    
    # Print numbers for the current row
    for k in range(1, i + 1):
        print(k, end=" ")
    
    # Move to the next line after each row
    print()