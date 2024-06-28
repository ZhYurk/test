def print_hourglass(n):
    # Top half of the hourglass
    for i in range(n, 1, -1):
        # Calculate leading spaces
        leading_spaces = n - i
        # Print leading spaces
        print(' ' * leading_spaces, end='')
        # Print asterisks and spaces
        print(' '.join('*' * i))
    
    # Middle part of the hourglass
    print(' ' * (n - 1) + '-')
 
    # Bottom half of the hourglass
    for i in range(2, n + 1):
        # Calculate leading spaces
        leading_spaces = n - i
        # Print leading spaces
        print(' ' * leading_spaces, end='')
        # Print asterisks and spaces
        print(' '.join('*' * i))
 
# Set the height of the top half of the hourglass
height = 5
print_hourglass(height)
