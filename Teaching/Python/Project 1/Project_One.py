# Here I wrote my constants
cost_day = 35.00 
distance_cost_per_km = 0.10
tax_rate = 0.15 


#Here I wrote my input statements, I needed to INT the ones I need to use in calculations
customer_name = input("Enter Your Name: ")
Phone_number = input("Enter Your Phone Number: ")
days_rented = int(input("Enter Amount Of Days Rented: "))
km_start = int(input("Enter Km At Rent Start: "))
km_end = int(input("Enter Km At Return: "))


#here I did my calcuations

#This one caluclates the kms traveled by subtracting the km at the end from the km at the beginning
km_traveled = km_end - km_start

#This one calcuates the cost for the daily part of the equation by multiplying the # of days rented by the cost per day
daily_cost_total = days_rented * cost_day

#This one calcuates the cost for the distance part of the equation by multiplying the km traveled by the cost per km
km_cost = km_traveled * distance_cost_per_km

#This one calcuates the full rental cost by adding the distance cost and the daily cost together
rental_cost =  daily_cost_total + km_cost

#This one cacluates the tax by multiplying the full rental cost by the tax rate (15%)
calculate_tax = tax_rate * rental_cost

#This one calcuates the complete final cost by adding the tax onto the rental cost
final_cost = rental_cost + calculate_tax


#Here I formatted the values for the money parts so they display with a "$" sign at the beginning and always has 2 decimal places
rental_cost_display = "${:,.2f}".format(rental_cost)

final_cost_display = "${:,.2f}".format(final_cost)

calculate_tax_display = "${:,.2f}".format(calculate_tax)

#This is where I finished by printing all the information
print()
print()
print(f"Customer Name: {customer_name}")
print(f"Phone Number: {Phone_number}")
print()
print(f"Number Of Days Rented: {days_rented}")
print(f"Km At Rent: {km_start}")
print(f"Km At Return: {km_end}")
print(f"Km Traveled: {km_traveled}")
print()
print(f"Rental Cost: {rental_cost_display}")
print(f"Tax: {calculate_tax_display}")
print(f"Total Cost: {final_cost_display}")











































