# Rubik's Cube State Calculator

This repository contains a Python script that calcultes the number of states of a Rubik's Cube.

## Table of Contents

- [Author](#)
- [Description](#description)
- [Sources](#)

## Programming Language

Python 3.11.2

## OS 

GNU/Linux

Kali Linux 6.1.0

## Author

**Juan Díaz** 
    * Personal [Github](https://github.com/Fuan200/) 
    * School [Github](https://github.com/JuanDiazuwu)

## Description

The Rubik's Cube State Calculator is a Python script that determines the total number of possible states for a Rubik's Cube with dimensions n x n x n, where `n` represents the size of each side of the cube. It utilizes a mathematical algorithm to compute the total number of unique configurations.

The script takes into account the dimensions of the cube to accurately calculate the number of states. Whether you have a 2x2x2, 3x3x3, or any other size of the Rubik's Cube, this script can calculate the total number of possible configurations.

The way in which the number of states is calculated, is as follows:

*   To even cubes:

```
    #n = 7! * 3⁶ * (24!)^k(k - 1) / (4!)^6(k-1)²
```

In which n = 2k, can you clear `k` and something like this would remain:

```
    k = n / 2
```

* To odd cubes: 

```
    #n = 8! * 3⁷ * 2^10 * (24!)^k(k - 2) / (4!)^6(k - 1)(k - 2)
```

In which n = 2k - 1, can you clear `k` and something like this would remain:

```
    k = (n + 1) / 2
```

## Requirements

- Python 3 or higher

- math library (included in the Python standard library)

## Usage

1. Clone the repository:

```
    $ git clone git@github.com:Fuan200/cube_states.git
```

2. Open the repository.

3. Run the script:

```
    $ python cube_states.py
```

4. You will be prompted to enter `n`.

5. Enter the value of `n` and press enter.

6. The script will calculate and output the number of possible states of those cube.

Note: The value `n` only can be between 2 and 8.