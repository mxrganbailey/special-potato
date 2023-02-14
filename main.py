print("Welcome!\n")
name = input("Enter the company name: ")
feet = input("\nEnter how many feet of fiber optic is to be installed: ")
feet = float(feet)

if feet <= 100:
  cost = feet * .87
elif feet <= 250:
  cost = feet * .8
elif feet <= 500:
  cost = feet * .7
else:
  cost = feet * .5
print(f"\nThe total cost is ${round(cost,2)} for {name.title()}.")
