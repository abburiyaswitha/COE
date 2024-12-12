salary = int(input("Enter the employee's salary:"))
bill1 = int(input("Enter the first shopping bill amount:"))
bill2 = int(input("Enter the second shopping bill amount:"))
bill3 = int(input("Enter the third shopping bill amount:"))
total_shopping_amount = bill1 + bill2 + bill3
percentage_spent=(total_shopping_amount*100)/salary 
print("Total shopping amount:{total_shopping_amount}")
print("The percentage of salary spent on shopping:{percentage_spent}")
