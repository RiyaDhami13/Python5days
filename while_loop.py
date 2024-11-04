tickets_sold = 0
max_capacity = 10

# Create a while loop
while tickets_sold < max_capacity:
  
  # Add one to tickets_sold in each iteration
  tickets_sold += 1

# Print the number of tickets sold
print("Sold out:", tickets_sold, "tickets sold!")


print(clf)

release_date = 26
current_date = 22

# Create a conditional loop while current_date is less than or equal to the release_date
while current_date <= release_date:
  
  # Increment current_date by one
  current_date += 1
  
  # Promote purchases
  if current_date <= 24:
    print("Purchase before the 25th for early access")
  
  # Check if the date is equal to the 25th
  elif current_date == 25:
    print("Coming soon")
  else:
    print("Available now!")