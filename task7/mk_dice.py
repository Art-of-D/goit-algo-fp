import random

analytical_probabilities = {
    2: 0.0278,
    3: 0.0556,
    4: 0.0833,
    5: 0.1111,
    6: 0.1389,
    7: 0.1667,
    8: 0.1389,
    9: 0.1111,
    10: 0.0833,
    11: 0.0556,
    12: 0.0278
}

def dice_roll():
    roll_sum = random.randint(1, 6) + random.randint(1, 6)
    return roll_sum

def cycle_dice_rolls(num_rolls=100000):
    results = {}

    for _ in range(num_rolls):
        roll_sum = dice_roll()
        results[roll_sum] = results.get(roll_sum, 0) + 1

    return results

def mk_dice(num_rolls):
    
    results = cycle_dice_rolls(num_rolls)

    probabilities = {s: count / num_rolls for s, count in results.items()}
    sorted_probabilities = sorted(probabilities.items())
    print(f"{'Сума':^10}{'Ймовірність':^15}")
    print("-" * 25)
    for result, probability in sorted_probabilities:
        print(f"{result:^10}{probability:^.2%}({num_rolls*probability:.0f}/{num_rolls})")

    return sorted_probabilities

# main
user_input = input("Введіть кількість рухів: ")
while not user_input.isdigit():
    user_input = input("Введіть кількість рухів ЦИФРАМИ: ")
num_rolls = int(user_input)
results = mk_dice(num_rolls)

print("-" * 25)
print("Difference between analytical and experimental probabilities:")
for result, probability in results:
    print(f"{result:^10} {probability - analytical_probabilities[result]:.2%}")