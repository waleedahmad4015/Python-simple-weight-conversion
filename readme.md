# Python Weight Converter

This is a simple Python-based weight converter that allows you to convert between kilograms and pounds. The user can input their weight and specify the unit (Kilograms or Pounds), and the program will perform the conversion.

## Features

- Converts weight from **Kilograms (kg)** to **Pounds (lbs)** and vice versa.
- User-friendly input prompts to specify the weight and unit of measurement.
- Handles invalid unit input and informs the user if the unit is incorrect.
- Supports one decimal place for the output weight.

## Requirements

- Python 3.x installed on your system.

## How to Use

1. Run the Python script:
   ```bash
   python weight_converter.py
   ```
2. The program will prompt you to enter your weight.

3. Then, you will be asked whether your weight is in **Kilograms (K or k)** or **Pounds (L or l)**. 
   - If you input `K` or `k`, it will convert the weight from Kilograms to Pounds.
   - If you input `L` or `l`, it will convert the weight from Pounds to Kilograms.

4. The program will output the converted weight along with the unit.

## Example Usage

### Example 1: Kilograms to Pounds
```bash
Enter Your weight : 70
Kilograms or Pounds ? K or L : K
Your weight is : 154.4 Lbs.
```

### Example 2: Pounds to Kilograms
```bash
Enter Your weight : 150
Kilograms or Pounds ? K or L : L
Your weight is : 68.0 kg
```

## Error Handling

- If the user enters an invalid unit (anything other than `K`, `k`, `L`, or `l`), the program will display an error message:
  ```
  [unit] is not valid
  ```

## License

This project is open-source and free to use. Feel free to modify or distribute it.