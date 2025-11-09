def knapsack_01_verbose(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    print("DP table initialization:")
    for row in dp:
        print(row)
    print()
    for i in range(1, n + 1):
        print(f"Considering item {i} (weight={weights[i-1]}, value={values[i-1]}):")
        for w in range(capacity + 1):
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i-1][w], values[i-1] + dp[i-1][w - weights[i-1]])
            else:
                dp[i][w] = dp[i -1][w]
        # Print DP table after this item
        for row in dp:
            print(row)
        print()
    max_value = dp[n][capacity]
    print(f"Maximum value achievable with capacity {capacity}: {max_value}")
    # Trace back to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
        # This item was included
            selected_items.append(i-1) # store index
            w -= weights[i-1]
    selected_items.reverse() # To list items in order they were added
    print("Selected items:")
    for idx in selected_items:
        print(f"Item {idx+1} - Weight: {weights[idx]}, Value: {values[idx]}")
    return max_value

weights = [2,3,4,5]
values = [1,2,5,6]
capacity = 8
knapsack_01_verbose(weights, values, capacity)