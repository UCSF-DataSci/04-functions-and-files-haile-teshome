#!/usr/bin/env python3
"""
Fibonacci Sequence

Create a program that generates Fibonacci numbers less than a limit and writes them to a file. The _Fibonacci_ sequence is a sequence in which each number is the sum of the two preceding ones: 

`0, 1, 1 (0+1), 2 (1+1), 3 (2+1), 5 (3+2), ...`

	- Use a function to generate Fibonacci numbers as a list
	- Use `with` statements for file operations
	- Handle potential file I/O errors with `try`/`except`
	- Use command-line arguments (via `argparse`) to specify the upper limit and output file name

Task: Generate the Fibonacci numbers less than 100 and write them to `fibonacci_100.txt`
"""

#Example use of the script: python fibonacci.py 100 
import argparse

def fib_sequence(limit):
    fib_numbers = []
    a, b = 0, 1
    while a < limit:
        fib_numbers.append(a)
        a, b = b, a + b
    return fib_numbers

def write_to_file(filename , data):
    try:
        with open(filename, 'w') as f:
            for number in data:
                f.write(f"{number}\n")
    except IOError as e:
        print(f"An error occurred while writing to the file: {e}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate Fibonacci numbers up to a limit and save to a file.")
    parser.add_argument('limit', type=int, help="Upper limit for Fibonacci sequence generation")
    parser.add_argument('output', nargs='?', default='fibonacci_100.txt', help="Output file name (default: fibonacci_100.txt)")
    args = parser.parse_args()

    # Generate Fibonacci sequence
    fib_numbers = fib_sequence(args.limit)
    write_to_file(args.output, fib_numbers)

if __name__ == "__main__":
    main()