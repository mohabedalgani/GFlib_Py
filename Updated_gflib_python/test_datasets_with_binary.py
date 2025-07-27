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

def test_dataset_compatibility():
    """Test if the new datasets are compatible with the binary.py format"""
    
    print("Testing new datasets compatibility with binary.py format...\n")
    
    # Test datasets
    datasets = ['odd_6_parity.txt', 'santa_fe_trail.txt']
    
    for dataset in datasets:
        print(f"Testing dataset: {dataset}")
        print("-" * 40)
        
        try:
            # Load dataset using the same method as binary.py
            data = np.loadtxt(f'data/binary/{dataset}', delimiter=',')
            
            # Check if data format is correct
            if data.shape[1] < 2:
                print(f"✗ Error: Dataset must have at least 2 columns (features + output)")
                continue
                
            # Separate features and output (same as binary.py would do)
            X = data[:, :-1]  # All columns except last
            y = data[:, -1]    # Last column
            
            print(f"✓ Dataset loaded successfully")
            print(f"  Shape: {data.shape}")
            print(f"  Features (X): {X.shape}")
            print(f"  Output (y): {y.shape}")
            print(f"  Unique output values: {np.unique(y)}")
            
            # Check if it's binary classification
            unique_outputs = np.unique(y)
            if len(unique_outputs) == 2:
                print(f"✓ Binary classification dataset (outputs: {unique_outputs})")
            else:
                print(f"⚠ Warning: Dataset has {len(unique_outputs)} unique outputs")
            
            # Sample data
            print(f"  Sample data (first 3 rows):")
            print(f"    X: {X[:3]}")
            print(f"    y: {y[:3]}")
            
        except Exception as e:
            print(f"✗ Error loading dataset: {e}")
        
        print()
    
    print("=" * 50)
    print("COMPATIBILITY TEST COMPLETED")
    print("=" * 50)
    print("\nTo use these datasets with binary.py:")
    print("1. Edit binary.py and change params['data'] to:")
    print("   - 'odd_6_parity.txt' for 6-parity problem")
    print("   - 'santa_fe_trail.txt' for Santa Fe Trail problem")
    print("2. Install missing dependencies: pip install matplotlib scikit-learn")
    print("3. Run: python binary.py")

if __name__ == "__main__":
    test_dataset_compatibility() 