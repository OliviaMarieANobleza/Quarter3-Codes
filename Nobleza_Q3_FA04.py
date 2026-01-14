names = ["Me", "Lia", "Jake"]

steps = [

  [4500, 5200, 4800, 5000, 5300],

  [4000, 4100, 3900, 4200, 4600],

  [6000, 5800, 5900, 6100, 6200]

]

total_steps=[sum(steps[i]) for i in range(len(steps))]

max_steps = max(total_steps)
min_steps = min(total_steps)

top_performer_index = total_steps.index(max_steps)

print(f"Total steps per person: {total_steps}")
print(f"Top Performer: {names[top_performer_index]} with {max_steps} steps.")
print(f"Difference between highest and lowest steps: {max_steps - min_steps}")
