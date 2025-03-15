num_of_days=int(input("Enter no.of days: "))
years=num_of_days//365
remaining=num_of_days%365
print("no.of years= ",years)
weeks=remaining//7
remaining=remaining%7
print("no.of weeks= ",weeks)
print("no.of days= ", remaining)
