# cot-4500-as3

# Numerical Methods Assignment

## Overview
This project uses Euler's Method and Runge-Kutta Method to solve the differential equation:

\[ \frac{dy}{dt} = t - y^2 \]

with the initial condition \( f(0) = 1 \), over the range \( 0 < t < 2 \) using 10 steps.

## Files
```
|-- src/
| |-- main/
| | |-- __init__.py
| | |-- assignment_3.py
| |-- test/
| | |-- __init__.py
| | |-- test_assignment_3.py
|-- requirements.txt
|-- README.md
```

## Setup
This project only requires NumPy. You can install it with:
```
pip install -r requirements.txt
```

## Running the Code
To run the program, use:
```
python src/main/assignment_3.py
```
This will print the results for both methods.

## Running Tests
To check if everything works correctly, run:
```
python -m unittest discover src/test
```

