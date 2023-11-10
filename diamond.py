def create_diamond(formula, num_lines):
  """Creates a diamond structure using the letters of the given formula.

  Args:
    formula: A string representing the formula to be used in the diamond.
    num_lines: An integer representing the number of lines for the spread of the diamond.

  Returns:
    A list of strings representing the lines of the diamond.
  """

  # Create a list of empty strings to store the lines of the diamond.
  diamond = []
  for i in range(num_lines):
    diamond.append('')

  # Calculate the center index of the diamond.
  center_index = num_lines // 2

  # Iterate over the formula and add each letter to the appropriate line of the diamond.
  for i in range(len(formula)):
    diamond[center_index - i] += formula[i]
    diamond[center_index + i] += formula[i]

  # Fill in the remaining lines of the diamond with spaces.
  for i in range(num_lines - 1, 0, -1):
    diamond[i] += ' ' * (len(formula) - i * 2)

  # Return the list of lines of the diamond.
  return diamond


# Get the number of lines for the spread of the diamond from the user.
num_lines = int(input('Enter the number of lines for the spread of the diamond: '))

# Create the diamond structure.
diamond = create_diamond('formulaQSolution', num_lines)

# Print the diamond structure.
for line in diamond:
  print(line)

