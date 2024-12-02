# input statements
salary = float(input("Enter Annual Salary"))
numDependents = int(input("Enter total dependents"))

# calculate taxes here
stateTaxRate = 0.065
federalTaxRate = 0.28
dependentDeduction = 0.025
stateTax = salary * stateTaxRate
federalTax = salary * federalTaxRate
dependents = salary * (dependentDeduction * numDependents)
totalWithholding = stateTax + federalTax + dependents
takeHomePay = salary - totalWithholding
# output statements
print("Salary: $" + str(salary))
print("Take Home Pay: $" + str(takeHomePay))
print("State Tax: $" + str(stateTax))
print("Federal Tax: $" + str(federalTax))
print("Dependents: $" + str(dependents)) 