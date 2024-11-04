# Create an empty list
authors_below_twenty_five = []

# Loop through the authors dictionary
for key, val in authors.items():
  
  # Check for values less than 25
  if val <= 25:
    
    # Append the author to the list
    authors_below_twenty_five.append(key)
    
print(authors_below_twenty_five)