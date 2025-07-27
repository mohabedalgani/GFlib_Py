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

def test_dataset_loading():
    """Test loading the new datasets"""
    
    # Test 6-parity dataset
    print("Testing 6-parity dataset...")
    try:
        data_6parity = np.loadtxt('data/binary/odd_6_parity.txt', delimiter=',')
        print(f"✓ 6-parity dataset loaded successfully: {data_6parity.shape}")
        print(f"  Sample data (first 5 rows):")
        print(data_6parity[:5])
    except Exception as e:
        print(f"✗ Error loading 6-parity dataset: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test Santa Fe Trail dataset
    print("Testing Santa Fe Trail dataset...")
    try:
        data_santa_fe = np.loadtxt('data/binary/santa_fe_trail.txt', delimiter=',')
        print(f"✓ Santa Fe Trail dataset loaded successfully: {data_santa_fe.shape}")
        print(f"  Sample data (first 5 rows):")
        print(data_santa_fe[:5])
    except Exception as e:
        print(f"✗ Error loading Santa Fe Trail dataset: {e}")
    
    print("\n" + "="*50 + "\n")
    
    # Test data format consistency
    print("Testing data format consistency...")
    datasets = ['odd_3_parity.txt', 'odd_6_parity.txt', 'odd_7_parity.txt', 'santa_fe_trail.txt']
    
    for dataset in datasets:
        try:
            data = np.loadtxt(f'data/binary/{dataset}', delimiter=',')
            print(f"✓ {dataset}: {data.shape[0]} samples, {data.shape[1]-1} inputs, 1 output")
        except Exception as e:
            print(f"✗ {dataset}: Error - {e}")

if __name__ == "__main__":
    test_dataset_loading() 