# This program will perdict the profit a company will make from its sales
# 9/26/19
# CTI-110 P2T1 - Sales Prediction
# Anthony Johnson
#

#Get the projected total sales.
total_sales=float(input("Enter the projected sales: "))

#Calculate the profit as 23 percent of total sales
profit=total_sales*0.23

#Display the profit
print("The profit is $", format(profit,",.2f"))

