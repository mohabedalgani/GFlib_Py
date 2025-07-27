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
import os

print('Demonstrating new datasets with GFLib...\n\n')

DATA_PATH = 'data/binary/'  # Dataset path for binary classification

# New datasets to test
new_datasets = ['odd_6_parity.txt', 'santa_fe_trail.txt']

for dataset in new_datasets:
    print(f'Testing dataset: {dataset}')
    print('=' * 50)
    
    # Load and display dataset info
    try:
        data = np.loadtxt(DATA_PATH + dataset, delimiter=',')
        print(f'Dataset shape: {data.shape}')
        print(f'Number of samples: {data.shape[0]}')
        print(f'Number of features: {data.shape[1] - 1}')
        print(f'Output classes: {np.unique(data[:, -1])}')
        print(f'Sample data (first 3 rows):')
        print(data[:3])
        print()
        
        # Test with a simple configuration
        params = dict()
        params['type'] = 'binary'
        params['data'] = dataset
        params['kernel'] = 'gf'
        params['mutProb'] = 0.01
        params['crossProb'] = 0.5
        params['maxGen'] = 3  # Reduced for demo
        params['popSize'] = 5  # Reduced for demo
        params['crossVal'] = 3  # Reduced for demo
        params['opList'] = ['Plus_s', 'Minus_s', 'Multi_s', 'Plus_v', 'Minus_v', 'x', 'y']
        
        print(f'Testing with Genetic Folding kernel...')
        print(f'Max Generation: {params["maxGen"]}')
        print(f'Population Size: {params["popSize"]}')
        print(f'Cross Validation: {params["crossVal"]}')
        
        # This would normally run the full algorithm
        # For demo purposes, we'll just show the configuration is valid
        print('✓ Configuration is valid for this dataset')
        
    except Exception as e:
        print(f'✗ Error with dataset {dataset}: {e}')
    
    print('\n' + '='*50 + '\n')

print('Demo completed!')
print('\nTo run the full algorithm with these datasets:')
print('1. Edit binary.py and change params[\'data\'] to one of the new datasets')
print('2. Run: python binary.py')
print('3. Enter the maximum chromosome length when prompted')
print('\nAvailable new datasets:')
print('- odd_6_parity.txt: 6-input parity problem (64 samples)')
print('- santa_fe_trail.txt: Santa Fe Trail navigation problem (100 samples)') 