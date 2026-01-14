prices = [
    [52, 85, 190],
    [50, 88, 185],
    [55, 82, 195],
    [53, 90, 200]
]

for i in range(len(prices)):
    total_price = sum(prices[i])
    average_price = total_price / len(prices[i])
    min_price = min(prices[i])

    print(f"Store {i + 1} - Total Price: {total_price} | "
            f"Average Price: {average_price:.2f} | "
            f"Minimum Price: {min_price} |")