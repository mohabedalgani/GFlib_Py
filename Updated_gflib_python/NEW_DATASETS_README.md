# New Datasets Added to GFLib

This document describes the two new datasets that have been added to the GFLib binary classification data folder.

## 1. 6-Parity Problem (`odd_6_parity.txt`)

### Description
The 6-parity problem is a classic binary classification problem where the goal is to determine if the number of 1s in a 6-bit input is odd (output = 1) or even (output = 0).

### Dataset Details
- **File**: `data/binary/odd_6_parity.txt`
- **Samples**: 64 (all possible 6-bit combinations)
- **Features**: 6 binary inputs
- **Output**: 1 binary output (0 or 1)
- **Format**: CSV with comma delimiter

### Data Format
Each row contains 7 values: 6 input bits followed by 1 output bit.
Example:
```
0,0,0,0,0,0,0  # 0 ones = even → output 0
0,0,0,0,0,1,1  # 1 one = odd → output 1
0,0,0,0,1,0,1  # 1 one = odd → output 1
```

### Usage
To use this dataset with GFLib, modify `binary.py`:
```python
params['data'] = 'odd_6_parity.txt'
```

## 2. Santa Fe Trail Problem (`santa_fe_trail.txt`)

### Description
The Santa Fe Trail is a classic artificial life problem where an agent must navigate a trail to collect food. This is a simplified version adapted for binary classification.

### Dataset Details
- **File**: `data/binary/santa_fe_trail.txt`
- **Samples**: 100 (generated with controlled randomness)
- **Features**: 6 inputs (position x,y, direction, sensor readings)
- **Output**: 1 binary output (0 = turn, 1 = move forward)
- **Format**: CSV with comma delimiter

### Feature Description
1. **x**: Agent's x-coordinate (0-31)
2. **y**: Agent's y-coordinate (0-31)
3. **direction**: Current direction (0-3: North, East, South, West)
4. **food_ahead**: Food detected ahead (0 or 1)
5. **food_left**: Food detected to the left (0 or 1)
6. **food_right**: Food detected to the right (0 or 1)
7. **action**: Decision (0 = turn, 1 = move forward)

### Data Format
Each row contains 7 values: 6 input features followed by 1 output.
Example:
```
6,19,0,0,0,1,0   # Position(6,19), North, no food ahead/left, food right → turn
28,20,2,1,0,0,1   # Position(28,20), South, food ahead, no food left/right → move forward
```

### Usage
To use this dataset with GFLib, modify `binary.py`:
```python
params['data'] = 'santa_fe_trail.txt'
```

## Testing the New Datasets

### Quick Test
Run the test script to verify the datasets work correctly:
```bash
python test_new_datasets.py
```

### Demo
Run the demo script to see dataset information:
```bash
python demo_new_datasets_simple.py
```

### Full Algorithm Test
To run the full Genetic Folding algorithm with these datasets:

1. Edit `binary.py` and change the data parameter:
   ```python
   params['data'] = 'odd_6_parity.txt'  # or 'santa_fe_trail.txt'
   ```

2. Run the algorithm:
   ```bash
   python binary.py
   ```

3. Enter the maximum chromosome length when prompted.

## Dataset Generation

### 6-Parity Generation
The 6-parity dataset was generated manually following the same pattern as the existing 3-parity and 7-parity datasets. The generation code has been added to `logicdatagen.py`.

### Santa Fe Trail Generation
The Santa Fe Trail dataset was generated using the `generate_santa_fe_trail.py` script, which creates a simplified version of the classic artificial life problem.

## Compatibility

Both datasets are fully compatible with the existing GFLib framework:
- ✅ Load correctly with `np.loadtxt()`
- ✅ Compatible with binary classification format
- ✅ Work with all SVM kernels (poly, rbf, linear, gf)
- ✅ Compatible with Genetic Folding algorithm
- ✅ Follow the same CSV format as existing datasets

## File Locations

- `data/binary/odd_6_parity.txt` - 6-parity problem dataset
- `data/binary/santa_fe_trail.txt` - Santa Fe Trail problem dataset
- `generate_santa_fe_trail.py` - Script to regenerate Santa Fe Trail data
- `test_new_datasets.py` - Test script for new datasets
- `demo_new_datasets_simple.py` - Demo script for new datasets
- `logicdatagen.py` - Updated to include 6-parity generation

## Notes

- The 6-parity problem is deterministic and contains all possible 6-bit combinations
- The Santa Fe Trail problem uses a simplified rule-based approach for demonstration
- Both datasets maintain the same format as existing binary classification datasets
- The datasets are ready to use with the existing GFLib framework without any modifications 