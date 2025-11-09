# Fractional Knapsack Problem using Greedy Method

def fractional_knapsack(weight, value, capacity):
    n = len(value)
    ratio = []  # value/weight ratio
    steps = 0

    # Calculate ratio
    for i in range(n):
        ratio.append(value[i] / weight[i])
        steps += 1

    # Combine all info
    items = list(zip(weight, value, ratio))
    # Sort items based on ratio (descending order)
    items.sort(key=lambda x: x[2], reverse=True)

    total_value = 0
    knapsack = []

    for w, v, r in items:
        steps += 1
        if capacity >= w:
            knapsack.append((w, v, 1))  # 1 means full item taken
            capacity -= w
            total_value += v
        else:
            fraction = capacity / w
            knapsack.append((w, v, round(fraction, 2)))  # fraction of item taken
            total_value += v * fraction
            capacity = 0
            break

    return total_value, knapsack, steps


# ---- Main Program ----
n = int(input("Enter number of items: "))

weight = []
value = []

for i in range(n):
    w = float(input(f"Enter weight of item {i+1}: "))
    v = float(input(f"Enter value of item {i+1}: "))
    weight.append(w)
    value.append(v)

capacity = float(input("Enter capacity of knapsack: "))

max_value, knapsack_items, steps = fractional_knapsack(weight, value, capacity)

print("\n--- Fractional Knapsack Solution ---")
print("Items considered (weight, value, fraction taken):")
for item in knapsack_items:
    print(item)

print("\nMaximum value in Knapsack =", round(max_value, 2))
print("Total steps taken =", steps)

# ---- Time & Space Complexity ----
"""
Time Complexity: O(n log n)  -> due to sorting by ratio
Space Complexity: O(n)
"""
