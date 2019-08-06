def calculate_total_price(price, quantity):
	total_cost = price * quantity
	return total_cost

def sum_total(totals = [] , *args):
	sum = 0
	for i in range(len(totals)):
		sum += totals[i]
	return sum


cashier= {'item_name': [], 'price': [], 'quantity': [], 'total_price': []}


while True:
	item_name = input("Item name (Enter 'Done' when finished):  ")
	if item_name.lower() == 'done':
		break
	else:
		cashier['item_name'].append(item_name)
		cashier['price'].append(float(input("Enter price:  ")))
		cashier['quantity'].append(float(input("Enter quantity:  ")))
		
print("""---------------------------------------------------------
	recepit
---------------------------------------------------------""")

#print (cashier)
for i in range(len(cashier['item_name'])):
	cashier['total_price'].append(calculate_total_price(cashier['price'][i],cashier['quantity'][i]))
	print("%d %s %2.3f KD"%(int(cashier['quantity'][i]),cashier['item_name'][i],cashier['total_price'][i]))

total = sum_total(cashier['total_price'])
print("---------------------------------------------------------")
print("Total = %2.3f KD"%(total))
