#!/usr/bin/env python3
"""
Largest Prime Fibonacci Number

Write a program that takes a number as an argument, finds the *Fibonacci* numbers less than that number, and prints the largest prime number in the list. 

	- Use command-line arguments to specify the upper limit 
	- Implement a function to check if a number is prime
	- Import and use the Fibonacci generating function from problem 1 as a module

Task: Find the largest prime Fibonacci number less that 50000
"""

#Example use of the script: python largest_prime.py 50000        
import os
import sys
import argparse
from math import isqrt
from fibonnaci import fib_sequence  # Import the Fibonacci function


# Prime checking function
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Find the largest prime Fibonacci number below a given limit.")
    parser.add_argument('limit', type=int, help="Upper limit for Fibonacci sequence generation")
    args = parser.parse_args()

    # Generate Fibonacci sequence 
    fib_numbers = fib_sequence(args.limit)

    # Filter prime numbers from Fibonacci sequence
    prime_fibs = [num for num in fib_numbers if is_prime(num)]
    if prime_fibs:
        print(f"The largest prime Fibonacci number below {args.limit} is {max(prime_fibs)}")
    else:
        print(f"No prime Fibonacci numbers found below {args.limit}")

if __name__ == "__main__":
    main()