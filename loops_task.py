def calculate_total_price(price, quantity):
	total_cost = price * quantity
	return total_cost

def sum_total(totals):
	sum = 0
	for i in range(len(totals)):
		sum += totals[i]['total']
	return sum


cashier1= {'item_name': [], 'price': [], 'quantity': [], 'total_price': []}
cashier = []


while True:
	item_name = input("Item name (Enter 'Done' when finished):  ")
	if item_name.lower() == 'done':
		break
	else:
		item_price = float(input("Enter price:   "))
		item_quantity = int(input("Enter quantity:  "))
		item_total = calculate_total_price(item_price, item_quantity)
		cashier.append({'name': item_name, 'price': item_price, 'quantity': item_quantity, 'total': item_total})

print(cashier)	
print("""---------------------------------------------------------
recepit
---------------------------------------------------------""")

for item in cashier:
	print("%d %s %2.3f KD"%(item['quantity'],item['name'], item['total']))

total = sum_total(cashier)
print("---------------------------------------------------------")
print("Total = %2.3f KD"%(total))
