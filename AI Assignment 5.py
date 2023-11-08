import random
import math

def objective_function(x):
    return x**2

initial_temperature = 100.0
cooling_rate = 0.95
min_temperature = 0.1
iterations = 5

x = random.uniform(-5, 5)
current_energy = objective_function(x)
best_x = x
best_energy = current_energy

for iteration in range(iterations):
    temperature = initial_temperature * math.pow(cooling_rate, iteration)
    neighbor_x = x + random.uniform(-1, 1)
    neighbor_x = max(-5, min(5, neighbor_x))
    neighbor_energy = objective_function(neighbor_x)
    energy_change = neighbor_energy - current_energy

    if energy_change < 0 or random.random() < math.exp(-energy_change / temperature):
        x = neighbor_x
        current_energy = neighbor_energy

    if current_energy < best_energy:
        best_x = x
        best_energy = current_energy

    print(f"Iteration {iteration + 1}: x = {x:.4f}, Energy = {current_energy:.4f}, Temperature = {temperature:.4f}")

print("Optimal solution: x =", best_x)
print("Minimum energy:", best_energy)