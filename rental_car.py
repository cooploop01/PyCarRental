import sys

'''
Section 1: Collect customer input
'''

# Set default rental charges
budget_charge = 40.00
daily_charge = 60.00
weekly_charge = 190.00

# Get rental details from the user
print("Welcome to the Car Rental Service!")

rentalCode = input("Enter rental code: (B)udget, (D)aily, or (W)eekly?\n").upper()

rentalPeriod = int(input("How many days do you plan to rent the car?\n"))

# Calculate rental charge based on the type of rental
if rentalCode == 'D':
    baseCharge = rentalPeriod * daily_charge

# Get odometer readings
odoStart = int(input("Enter the starting odometer reading:\n"))
odoEnd = int(input("Enter the ending odometer reading:\n"))

# Calculate total miles driven and average miles per day
totalMiles = odoEnd - odoStart
averageDayMiles = totalMiles / rentalPeriod

# Calculate extra mileage charge if average miles per day exceed 100
extraMiles = max(0, averageDayMiles - 100)
mileCharge = extraMiles * 0.25

# Calculate total amount due
amtDue = "%.2f" % (daily_charge + mileCharge)

# Print the rental summary in a more organized format
print('\nThank you for choosing our car rental service!\n')
print('Rental Summary:')
print(f'Rental Code:       {rentalCode}')
print(f'Rental Period:     {rentalPeriod} day(s)')
print(f'Starting Odometer: {odoStart}')
print(f'Ending Odometer:   {odoEnd}')
print(f'Miles Driven:      {totalMiles}')
print(f'Amount Due:        ${amtDue}\n')

print('We hope you enjoy your trip!')

