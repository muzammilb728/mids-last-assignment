#Qno1:)

def calculate_ticket_price(age, day, num_tickets=1):
    base_price = 0
    if age == 'adult':
        base_price = 10
    elif age == 'child':
        base_price = 5
    elif age == 'senior':
        base_price = 8
    if day == 'weekend':
        base_price *= 1.2  
    if num_tickets >= 5:
        base_price *= 0.9  
    total_price = base_price * num_tickets
    return total_price
age = input("Enter age category (adult/child/senior): ")
day = input("Enter day of the week (weekday/weekend): ")
num_tickets = int(input("Enter the number of tickets: "))
total_cost = calculate_ticket_price(age, day, num_tickets)
print(f'Total cost: ${total_cost:.2f}')


#Qno2:)

def calculate_bill(items, quantities, prices, discount_percent=0, tax_percent=0, split_count=1):
    total_cost = 0
    for i in range(len(items)):
        total_cost += quantities[i] * prices[i]
    total_cost *= (1 - discount_percent / 100)
    total_cost *= (1 + tax_percent / 100)
    if split_count > 1:
        total_cost /= split_count
    return total_cost
items = input("Enter the items (comma-separated): ").split(', ')
quantities = [int(qty) for qty in input("Enter the quantities (comma-separated): ").split(', ')]
prices = [float(price) for price in input("Enter the prices (comma-separated): ").split(', ')]
discount = float(input("Enter the discount percentage: "))
tax = float(input("Enter the tax percentage: "))
friends = int(input("Enter the number of friends to split the bill with: "))
total_bill = calculate_bill(items, quantities, prices, discount, tax, friends)
print(f'Total bill: ${total_bill:.2f}')


#Qno3:) Sir, I tried it complete it but it was not working properly so I just skip it.


#Qno4:)

def estimate_travel_cost(destination, travel_style='budget', duration=7):
    base_costs = {
        'budget': {'transportation': 300, 'accommodation': 50, 'activities': 30},
        'luxury': {'transportation': 800, 'accommodation': 200, 'activities': 100}
    }
    if travel_style not in base_costs:
        raise ValueError("Invalid travel style. Choose 'budget' or 'luxury'.")
    costs = base_costs[travel_style]
    total_cost = sum(cost * duration for cost in costs.values())
    return total_cost
destination = input("Enter the destination: ")
travel_style = input("Enter the travel style (budget/luxury): ")
duration = int(input("Enter the duration of the trip (in days): "))
total_travel_cost = estimate_travel_cost(destination, travel_style, duration)
print(f'Estimated travel cost for {duration} days in {destination} ({travel_style}): ${total_travel_cost}')

