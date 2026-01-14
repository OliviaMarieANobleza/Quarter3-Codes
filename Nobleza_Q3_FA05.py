names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]

total_per_day = []
for day_index in range(len(days)):
    total = sum(steps[person][day_index] for person in range(len(names)))
    total_per_day.append(total)

for day, total in zip(days, total_per_day):
    print(f"{day}: {total} steps")

max_steps = max(total_per_day)
max_day_index = total_per_day.index(max_steps)
print(f"Day with highest steps: {days[max_day_index]} with {max_steps} steps.")