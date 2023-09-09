###Mean-Variance-Standard-Deviation-Calculator

his project is an assignment from the Data Analysis with Python Projects on freeCodeCamp.org.

**The Assignment**
Create a function named calculate() in mean_var_std.py that uses NumPy to calculate the mean, variance, standard deviation, maximum, minimum, and sum of the rows, columns, and elements in a 3x3 matrix.

The function should take a list of 9 numbers as input and convert it to a 3x3 NumPy array. It should then return a dictionary containing the calculated values, organized into the following three categories:

- Axis 1: The mean, variance, standard deviation, maximum, minimum, and sum of the rows in the matrix.
- Axis 2: The mean, variance, standard deviation, maximum, minimum, and sum of the columns in the matrix.
- Flattened: The mean, variance, standard deviation, maximum, minimum, and sum of the flattened matrix.


If the input list contains less than 9 elements, the function should raise a ValueError exception with the message "List must contain nine numbers."

For example, the following code should return the following dictionary:

calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])

```python

{
  'mean': [axis1, axis2, flattened],
  'variance': [axis1, axis2, flattened],
  'standard deviation': [axis1, axis2, flattened],
  'max': [axis1, axis2, flattened],
  'min': [axis1, axis2, flattened],
  'sum': [axis1, axis2, flattened]
}

```

If a list containing less than 9 elements is passed into the function, it should raise a ValueError exception with the message: "List must contain nine numbers." The values in the returned dictionary should be lists and not Numpy arrays.

For example, calculate([0,1,2,3,4,5,6,7,8]) should return:

```python

{
  'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0], 
  'variance': [[6.0, 6.0, 6.0], [0.6666666666666666, 0.6666666666666666, 0.6666666666666666], 6.666666666666667], 
  'standard deviation': [[2.449489742783178, 2.449489742783178, 2.449489742783178], [0.816496580927726, 0.816496580927726, 0.816496580927726], 2.581988897471611],
  'max': [[6, 7, 8], [2, 5, 8], 8],
  'min': [[0, 1, 2], [0, 3, 6], 0],
  'sum': [[9, 12, 15], [3, 12, 21], 36]}
}

```

The unit tests for this project are in test_module.py.

**Development**
For development, you can use main.py to test your calculate() function. Click the "run" button and main.py will run.

**Testing**
We imported the tests from test_module.py to main.py for your convenience. The tests will run automatically whenever you hit the "run" button.
