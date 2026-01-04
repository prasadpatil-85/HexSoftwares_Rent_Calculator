def calculate_rent():
    print("Welcome to the Rent Calculator!")
    
    # Input: Total rent and number of people sharing the rent
    total_rent = float(input("Enter the total rent amount: ₹"))
    num_people = int(input("Enter the number of people sharing the rent: "))
    
    # Ask if this is the first time or recurring rent
    is_first_time = input("Is this the first time? (yes/no): ").lower()
    
    # Initialize total cost with rent
    total_cost = total_rent
    
    # If it's the first time, include security deposit
    if is_first_time == 'yes':
        security_deposit = float(input("Enter the security deposit: ₹"))
        total_cost += security_deposit
    
    # Water is mandatory
    water = float(input("Enter the water cost: ₹"))
    total_cost += water
    
    # Ask if user wants to include utilities and internet costs
    include_utilities = input("Do you want to include utilities and internet costs? (yes/no): ").lower()
    
    if include_utilities == 'yes':
        utilities = float(input("Enter the total utility costs (e.g., electricity): ₹"))
        internet = float(input("Enter the internet cost: ₹"))
        total_cost += utilities + internet
    
    # Ask if food should be included (optional)
    include_food = input("Do you want to include food costs? (yes/no): ").lower()
    
    if include_food == 'yes':
        food = float(input("Enter the total food cost: ₹"))
        total_cost += food
    
    # Calculate individual share
    individual_share = total_cost / num_people
    
    # Output: Display the total cost and individual share
    print("\nThe total rent and expenses are: ₹", total_cost)
    print(f"Each person should pay: ₹{individual_share:.2f}")
    
# Run the Rent Calculator
calculate_rent()
