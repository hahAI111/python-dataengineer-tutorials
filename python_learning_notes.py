# -*- coding: utf-8 -*-
"""
Python Learning Notes
========================================
Author: jingwang1
Date: 2026-02-27
Description: Python fundamentals covering loops, data structures, functions, memory management, and more

Table of Contents:
1. Loops
2. Control Statements (pass, continue, break)
3. Data Structures
4. Set Operations
5. Functions (*args, **kwargs, lambda, decorators)
6. Memory Management (iterators, shallow copy, deep copy)
7. File Operations
8. Exception Handling
9. Module Imports
"""

# ============================================================================
# 1. Loops
# ============================================================================

# --- for loop ---
print("=" * 50)
print("1. Loops")
print("=" * 50)

# Basic for loop
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)

# range() function
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(2, 8):     # 2, 3, 4, 5, 6, 7
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step of 2)
    print(i)

# --- while loop ---
count = 0
while count < 5:
    print(count)
    count += 1

# --- enumerate() - get both index and value ---
colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")
# Output:
# Index 0: red
# Index 1: green
# Index 2: blue


# ============================================================================
# 2. Control Statements: pass, continue, break
# ============================================================================
"""
Comparison Table:
┌──────────┬────────────────────────────┬─────────────────┐
│ Keyword  │ Function                   │ Loop continues? │
├──────────┼────────────────────────────┼─────────────────┤
│ pass     │ Does nothing, placeholder  │ ✅ Continue code │
│ continue │ Skip remaining code        │ ✅ Next iteration│
│ break    │ Exit loop completely       │ ❌ Exit loop     │
└──────────┴────────────────────────────┴─────────────────┘
"""

print("\n" + "=" * 50)
print("2. Control Statements: pass, continue, break")
print("=" * 50)

# --- pass: does nothing, code continues ---
print("\n--- pass example ---")
for i in range(5):
    if i == 2:
        pass  # Does nothing, but code continues
    print(f"i = {i}")
# Output: 0, 1, 2, 3, 4 (all printed, including 2)

# pass is commonly used as a placeholder
class MyClass:
    pass  # To be implemented later

def my_function():
    pass  # To be implemented later

# --- continue: skip current iteration, go to next ---
print("\n--- continue example ---")
for i in range(5):
    if i == 2:
        continue  # Skip i=2
    print(f"i = {i}")
# Output: 0, 1, 3, 4 (skipped 2)

# --- break: exit loop completely ---
print("\n--- break example ---")
for i in range(5):
    if i == 2:
        break  # Exit when i=2
    print(f"i = {i}")
# Output: 0, 1 (2 and after not printed)


# ============================================================================
# 3. Data Structures
# ============================================================================
"""
Python's Four Main Data Structures:
┌────────┬─────────┬─────────┬────────────┬────────────────┐
│ Type   │ Mutable │ Ordered │ Duplicates │ Syntax         │
├────────┼─────────┼─────────┼────────────┼────────────────┤
│ list   │ ✅      │ ✅      │ ✅         │ [1, 2, 3]      │
│ tuple  │ ❌      │ ✅      │ ✅         │ (1, 2, 3)      │
│ set    │ ✅      │ ❌      │ ❌         │ {1, 2, 3}      │
│ dict   │ ✅      │ ✅      │ Unique keys│ {"a": 1}       │
└────────┴─────────┴─────────┴────────────┴────────────────┘
"""

print("\n" + "=" * 50)
print("3. Data Structures")
print("=" * 50)

# --- List ---
print("\n--- List ---")
my_list = [1, 2, 3, 4, 5]
my_list.append(6)        # Add element
my_list.insert(0, 0)     # Insert at index 0
my_list.remove(3)        # Remove element with value 3
popped = my_list.pop()   # Pop last element
my_list.reverse()        # Reverse list
my_list.sort()           # Sort list
print(my_list)

# List Comprehension
squares = [x**2 for x in range(10)]          # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
evens = [x for x in range(20) if x % 2 == 0] # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
print(f"Squares: {squares}")
print(f"Evens: {evens}")

# --- Tuple ---
print("\n--- Tuple ---")
my_tuple = (1, 2, 3)
# my_tuple[0] = 10  # ❌ Error! Tuples are immutable
print(f"First element of tuple: {my_tuple[0]}")
print(f"Tuple length: {len(my_tuple)}")

# Tuple unpacking
a, b, c = my_tuple
print(f"Unpacked: a={a}, b={b}, c={c}")

# --- Dictionary ---
print("\n--- Dictionary ---")
my_dict = {"name": "Alice", "age": 25, "city": "New York"}

# Access
print(my_dict["name"])          # Alice
print(my_dict.get("email", "N/A"))  # N/A (returns default if key doesn't exist)

# Modify/Add
my_dict["age"] = 26             # Modify
my_dict["email"] = "a@b.com"    # Add

# Iterate
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Dictionary Comprehension
squared_dict = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
print(f"Dict comprehension: {squared_dict}")

# --- Set ---
print("\n--- Set ---")
my_set = {1, 2, 3, 3, 4}  # Auto-deduplicates -> {1, 2, 3, 4}
my_set.add(5)             # Add element
my_set.remove(1)          # Remove element
print(f"Set: {my_set}")


# ============================================================================
# 4. Set Operations
# ============================================================================
"""
Set Operators and Methods:
┌────────────────────────────┬────────────┬────────────────────┐
│ Operation                  │ Operator   │ Method             │
├────────────────────────────┼────────────┼────────────────────┤
│ Union                      │ a | b      │ a.union(b)         │
│ Intersection               │ a & b      │ a.intersection(b)  │
│ Difference                 │ a - b      │ a.difference(b)    │
│ Symmetric Difference       │ a ^ b      │ a.symmetric_diff.. │
└────────────────────────────┴────────────┴────────────────────┘

Diagram:
     a = {1, 2, 3, 4}
     b = {3, 4, 5, 6}
     
     ┌───────────────────────────────────┐
     │        Set a          Set b       │
     │     ┌───────┐     ┌───────┐      │
     │     │ 1   2 │     │ 5   6 │      │
     │     │   ┌───┼─────┼───┐   │      │
     │     │   │ 3 │  4  │   │   │      │
     │     │   └───┼─────┼───┘   │      │
     │     └───────┘     └───────┘      │
     └───────────────────────────────────┘
     
     Intersection: {3, 4}         ← Common elements
     Difference:   {1, 2}         ← In a but not in b
     Symmetric:    {1, 2, 5, 6}   ← In either but not both
"""

print("\n" + "=" * 50)
print("4. Set Operations")
print("=" * 50)

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# Intersection - elements common to both sets
intersection = a.intersection(b)  # or a & b
print(f"Intersection a ∩ b: {intersection}")  # {3, 4}

# Union - all elements from both sets
union = a.union(b)  # or a | b
print(f"Union a ∪ b: {union}")  # {1, 2, 3, 4, 5, 6}

# Difference - elements in a but not in b
difference = a.difference(b)  # or a - b
print(f"Difference a - b: {difference}")  # {1, 2}

# Symmetric Difference - elements in either set but not both
symmetric_diff = a.symmetric_difference(b)  # or a ^ b
print(f"Symmetric Difference a △ b: {symmetric_diff}")  # {1, 2, 5, 6}

# Practical example
enrolled_students = {"Alice", "Bob", "Charlie", "David"}
submitted_homework = {"Bob", "David", "Eve"}

# Who submitted homework but is not enrolled?
print(f"Not enrolled but submitted: {submitted_homework - enrolled_students}")  # {'Eve'}

# Who is enrolled but didn't submit homework?
print(f"Enrolled but didn't submit: {enrolled_students - submitted_homework}")  # {'Alice', 'Charlie'}


# ============================================================================
# 5. Functions
# ============================================================================

print("\n" + "=" * 50)
print("5. Functions")
print("=" * 50)

# --- Basic function definition ---
def greet(name, greeting="Hello"):
    """Function with default parameter"""
    return f"{greeting}, {name}!"

print(greet("Alice"))             # Hello, Alice!
print(greet("Bob", "Hi"))         # Hi, Bob!


# --- *args: accepts any number of positional arguments (packed as tuple) ---
print("\n--- *args example ---")
def sum_all(*args):
    """Accepts any number of arguments and sums them"""
    print(f"args type: {type(args)}, value: {args}")
    return sum(args)

print(sum_all(1, 2, 3))           # 6
print(sum_all(1, 2, 3, 4, 5))     # 15


# --- **kwargs: accepts any number of keyword arguments (packed as dict) ---
print("\n--- **kwargs example ---")
def create_user(**kwargs):
    """Accepts any keyword arguments to create user"""
    print(f"kwargs type: {type(kwargs)}, value: {kwargs}")
    return kwargs

user = create_user(name="Alice", age=30, city="New York")
print(f"User info: {user}")


# --- Mixing *args and **kwargs ---
print("\n--- Mixed usage ---")
def mixed_example(required, *args, **kwargs):
    """Three types of parameters mixed"""
    print(f"Required param: {required}")
    print(f"Extra positional args: {args}")
    print(f"Extra keyword args: {kwargs}")

mixed_example("required", 1, 2, 3, name="Alice", age=30)


# --- Lambda (Anonymous Functions) ---
print("\n--- Lambda functions ---")
# Syntax: lambda parameters: expression
square = lambda x: x ** 2
add = lambda x, y: x + y

print(f"Square of 5: {square(5)}")    # 25
print(f"3 + 4 = {add(3, 4)}")         # 7

# Lambda often used with sorted, map, filter
students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]
sorted_by_score = sorted(students, key=lambda x: x[1], reverse=True)
print(f"Sorted by score: {sorted_by_score}")


# --- Decorator ---
print("\n--- Decorators ---")
import time

def timer(func):
    """Timer decorator"""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} execution time: {end - start:.4f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Simulates time-consuming operation"""
    time.sleep(0.1)
    return "Done"

result = slow_function()


# ============================================================================
# 6. Memory Management
# ============================================================================
"""
6.1 Iterator vs List Memory Usage
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Function        Return Type   Memory Usage    Feature
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
map()           Iterator      ~48 bytes       Lazy evaluation
filter()        Iterator      ~48 bytes       Lazy evaluation
zip()           Iterator      ~48 bytes       Lazy evaluation
enumerate()     Iterator      ~48 bytes       Lazy evaluation
range()         Range object  ~48 bytes       Lazy evaluation
list()          List          8n bytes        Stores all elements
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

6.2 Assignment vs Shallow Copy vs Deep Copy
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Operation     Syntax                New Object?  Nested Independent?  Memory
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Assignment    b = a                 ❌ Same      ❌                   Min
Shallow Copy  b = a.copy()          ✅ New       ❌ Shared nested     Medium
Deep Copy     b = copy.deepcopy(a)  ✅ New       ✅ Fully independent Max
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Diagram:
═══════════════════════════════════════════════════════════════
Assignment:     a ──┬──► [1, [2, 3]]      Two names, same object
                b ──┘

Shallow Copy:   a ────► [1, ─┬─► [2, 3]]  Outer new, inner shared
                b ────► [1, ─┘         ]

Deep Copy:      a ────► [1, ────► [2, 3]] Completely independent
                b ────► [1, ────► [2, 3]]
═══════════════════════════════════════════════════════════════
"""

print("\n" + "=" * 50)
print("6. Memory Management")
print("=" * 50)

import sys
import copy

# --- Iterator vs List ---
print("\n--- Iterator vs List memory comparison ---")

# Create large data
big_list = list(range(1000000))        # Immediately creates 1 million elements
big_range = range(1000000)             # Just a range object
big_map = map(lambda x: x*2, range(1000000))  # Just an iterator

print(f"list memory: {sys.getsizeof(big_list):,} bytes")  # ~8,000,000+ bytes
print(f"range memory: {sys.getsizeof(big_range)} bytes")   # ~48 bytes
print(f"map memory: {sys.getsizeof(big_map)} bytes")       # ~48 bytes


# --- Assignment vs Shallow Copy vs Deep Copy ---
print("\n--- Assignment vs Shallow Copy vs Deep Copy ---")

# Original list (contains nested list)
original = [1, 2, [3, 4]]

# 1. Assignment - just creates a reference, points to same object
assigned = original
print(f"Same id after assignment? {id(original) == id(assigned)}")  # True

# 2. Shallow copy - creates new object, but nested objects are still shared
shallow = original.copy()  # or list(original) or original[:]
print(f"Same id shallow copy? {id(original) == id(shallow)}")   # False
print(f"Same nested list id? {id(original[2]) == id(shallow[2])}")  # True!

# 3. Deep copy - completely independent copy
deep = copy.deepcopy(original)
print(f"Same id deep copy? {id(original) == id(deep)}")      # False
print(f"Same nested list id? {id(original[2]) == id(deep[2])}")  # False!

# Demonstrate modification effects
print("\nEffect after modifying nested list:")
original[2].append(5)
print(f"original: {original}")  # [1, 2, [3, 4, 5]]
print(f"assigned: {assigned}")  # [1, 2, [3, 4, 5]] - Affected!
print(f"shallow:  {shallow}")   # [1, 2, [3, 4, 5]] - Affected!
print(f"deep:     {deep}")      # [1, 2, [3, 4]]    - Not affected!


# ============================================================================
# 7. File Operations
# ============================================================================

print("\n" + "=" * 50)
print("7. File Operations")
print("=" * 50)

# --- Basic file read/write ---
# Write file
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("Hello, Python!\n")
    f.write("This is line two\n")

# Read file
with open("example.txt", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)

# Read line by line
with open("example.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(line.strip())

# --- CSV file ---
import csv

# Write CSV
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "Los Angeles"]
]
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(data)

# Read CSV
with open("data.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# --- JSON file ---
import json

# Write JSON
user_data = {"name": "Alice", "age": 25, "hobbies": ["reading", "coding"]}
with open("user.json", "w", encoding="utf-8") as f:
    json.dump(user_data, f, ensure_ascii=False, indent=2)

# Read JSON
with open("user.json", "r", encoding="utf-8") as f:
    loaded_data = json.load(f)
    print(loaded_data)


# ============================================================================
# 8. Exception Handling
# ============================================================================
"""
Python Exception Handling Structure:
┌─────────────────────────────────────────────┐
│  try:                                       │
│      Code that might raise an exception     │
│  except ExceptionType as e:                 │
│      Handle specific exception              │
│  except Exception as e:                     │
│      Handle other exceptions                │
│  else:                                      │
│      Runs if no exception                   │
│  finally:                                   │
│      Always runs (cleanup resources)        │
└─────────────────────────────────────────────┘
"""

print("\n" + "=" * 50)
print("8. Exception Handling")
print("=" * 50)

# Basic exception handling
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")
        return None
    except TypeError as e:
        print(f"Type error: {e}")
        return None
    else:
        print("Calculation successful")
        return result
    finally:
        print("Cleanup complete")

print(divide(10, 2))   # Normal: 5.0
print(divide(10, 0))   # ZeroDivisionError
print(divide("10", 2)) # TypeError

# Raising exceptions
def validate_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative")
    if age > 150:
        raise ValueError("Age is unreasonable")
    return True

try:
    validate_age(-5)
except ValueError as e:
    print(f"Validation failed: {e}")


# ============================================================================
# 9. Module Imports
# ============================================================================
"""
Import Methods:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
import math              # Import entire module
from math import sqrt    # Import specific function
from math import *       # Import all (not recommended)
import numpy as np       # Import with alias
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Common Standard Libraries:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Module      Purpose                 Example
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
os          OS interface            os.path, os.listdir()
sys         System related          sys.argv, sys.path
datetime    Date and time           datetime.now()
json        JSON handling           json.load(), json.dump()
re          Regular expressions     re.match(), re.search()
random      Random numbers          random.randint()
collections Advanced data structs   Counter, defaultdict
itertools   Iterator tools          chain, combinations
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

print("\n" + "=" * 50)
print("9. Module Imports")
print("=" * 50)

# Common module examples
import os
import datetime
import random
from collections import Counter

# os module
print(f"Current directory: {os.getcwd()}")

# datetime module
now = datetime.datetime.now()
print(f"Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}")

# random module
print(f"Random number (1-10): {random.randint(1, 10)}")

# collections.Counter
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
word_count = Counter(words)
print(f"Word count: {word_count}")
print(f"Most common 2: {word_count.most_common(2)}")


# ============================================================================
# 10. Recursion
# ============================================================================

print("\n" + "=" * 50)
print("10. Recursion")
print("=" * 50)

# Factorial
def factorial(n):
    """Calculate n! (recursive implementation)"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"5! = {factorial(5)}")  # 120

# Fibonacci sequence
def fibonacci(n):
    """Calculate the nth Fibonacci number"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print(f"First 10 Fibonacci: {[fibonacci(i) for i in range(10)]}")


# ============================================================================
# Cleanup temporary files
# ============================================================================
import os

# Delete temporary files created in examples
for f in ["example.txt", "data.csv", "user.json"]:
    if os.path.exists(f):
        os.remove(f)
        print(f"Cleaned up: {f}")


print("\n" + "=" * 50)
print("End of Learning Notes - Happy Coding! 🐍")
print("=" * 50)
