salary = int(input("Enter beginning salary : "))

change = 1 
for i in range(4):
    change *= 1.05

salary *= change 

print("New salary: ${:,.2}".format(salary))
print("Change: {:.2%}".format(change-1))
