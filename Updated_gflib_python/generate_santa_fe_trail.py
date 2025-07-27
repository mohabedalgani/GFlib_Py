'''
   This file is part of GFLIB toolbox
   First Version Sept. 2018

   Cite this project as:
   Mezher M., Abbod M. (2011) Genetic Folding: A New Class of Evolutionary Algorithms.
   In: Bramer M., Petridis M., Hopgood A. (eds) Research and Development in Intelligent Systems XXVII.
   SGAI 2010. Springer, London

   Copyright (C) 20011-2018 Mohd A. Mezher (mohabedalgani@gmail.com)
'''

import numpy as np

# Santa Fe Trail problem
# The Santa Fe Trail is a classic artificial life problem
# We'll create a simplified version where the agent must navigate a trail
# Input features: current position (x,y), direction, and sensor readings
# Output: whether to move forward (1) or turn (0)

# Generate training data for Santa Fe Trail
np.random.seed(42)  # For reproducibility

# Create 100 training samples
n_samples = 100
data = np.zeros((n_samples, 7))  # 6 inputs + 1 output

for i in range(n_samples):
    # Generate random position (x, y)
    x = np.random.randint(0, 32)
    y = np.random.randint(0, 32)
    
    # Generate random direction (0-3: North, East, South, West)
    direction = np.random.randint(0, 4)
    
    # Generate sensor readings (simplified: food ahead, food left, food right)
    food_ahead = np.random.randint(0, 2)
    food_left = np.random.randint(0, 2)
    food_right = np.random.randint(0, 2)
    
    # Simple rule: if food ahead, move forward (1), otherwise turn (0)
    # This is a simplified version of the Santa Fe Trail problem
    if food_ahead:
        action = 1  # Move forward
    else:
        action = 0  # Turn
    
    # Store the data
    data[i, 0] = x
    data[i, 1] = y
    data[i, 2] = direction
    data[i, 3] = food_ahead
    data[i, 4] = food_left
    data[i, 5] = food_right
    data[i, 6] = action

# Save to file
np.savetxt('data/binary/santa_fe_trail.txt', data, delimiter=',', fmt='%i')
print("Santa Fe Trail dataset generated successfully!")
print(f"Generated {n_samples} samples with 6 input features and 1 output") 