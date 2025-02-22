from timeit import timeit

AMOUNT = 300 # budget, change it if you want


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def find_optimal_food(items, budget):
    sorted_items = sorted(items.items(), key=lambda x: x[1]["calories"]/x[1]["cost"], reverse=True)
    optimal_food = {}
    total_cost = 0
    total_calories = 0
    for item, info in sorted_items:
        cost = info["cost"]
        calories = info["calories"]
        while total_cost + cost <= budget:
            optimal_food[item] = optimal_food.get(item, 0) + 1
            total_cost += cost
            total_calories += calories
    return total_cost,total_calories, optimal_food

  
cost, calories, food = find_optimal_food(items, AMOUNT)
print("Optimal food:")
print(f"Optimal food: {food}")
print(f"Total cost: {cost}")
print(f"Total calories: {calories}")

print(f"Time it: {timeit(lambda:find_optimal_food(items, AMOUNT), number=1):.6f} sec")

def knapsack(items, budget):
    names = list(items.keys())
    costs = [items[name]["cost"] for name in names]
    calories = [items[name]["calories"] for name in names]
    n = len(items)
    dp = [0] * (budget + 1)
    chosen_items = [{} for _ in range(budget + 1)]

    for b in range(budget + 1):
        for i in range(n):
            if costs[i] <= b:
                new_calories = dp[b - costs[i]] + calories[i]
                if new_calories > dp[b]:
                    dp[b] = new_calories
                    chosen_items[b] = chosen_items[b - costs[i]].copy()
                    chosen_items[b][names[i]] = chosen_items[b].get(names[i], 0) + 1

    total_calories = dp[budget]
    optimal_food = chosen_items[budget]
    total_cost = sum(items[item]["cost"] * count for item, count in optimal_food.items())

    return total_cost, total_calories, optimal_food


cost, calories, food = knapsack(items, AMOUNT)
print("\nKnapsack:")
print(f"Optimal food: {food}")
print(f"Total cost: {cost}")
print(f"Total calories: {calories}")

print(f"Time it: {timeit(lambda:knapsack(items, AMOUNT), number=1):.6f} sec")