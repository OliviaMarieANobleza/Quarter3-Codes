prices = [
    [52, 85, 190],
    [50, 88, 185],
    [55, 82, 195],
    [53, 90, 200]
]
grocery_no = 1
for row in prices:
    total=sum(row)
    average=total/len(row)

    print(f"Grocery {grocery_no} prices: {row}")
    print(f"Total Price: {total}")
    print(f"Average Price: {average}")
    print()
    grocery_no += 1

all_prices = []
for row in prices:
    for item in row:
        all_prices.append(item)

print("Highest price among all groceries:", max(all_prices))
