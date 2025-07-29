import sys
import os
import math
import sympy
from sympy import symbols
from sympy.solvers import solve

def add(a,b):
  print(a + b)

def subtract(a, b):
  print(a - b)

def multyply(a ,b):
  print(a*b)

def devide(a, b):
  print(a/b)

def prime_number(a):
  prime_or_comp = "prime"
  for test_number in range(2,a):
      if a % test_number == 0:
          prime_or_comp = "composite"
  print(prime_or_comp)

def generate_prime_factors(n):
  for test_number in range(1,n + 1):
      if n % test_number == 0:
          print(test_number)

def square_root(n):
  # use this variables
  upper_limit = math.floor(math.sqrt(n)) + 1
  max_factor = 1
  other_factor = 1
  square_factor = 1

  # find square factors
  for maybe_factor in range(1, upper_limit):
    if n % (maybe_factor**2) == 0:
      max_factor = maybe_factor**2

  # devide out the gratest square factor
  other_factor = n/max_factor

  # output variables
  square_root = int(math.sqrt(max_factor))
  other_factor = int(other_factor)
  output = square_root*sympy.sqrt(other_factor)

  print(output)


def solve_for_x(eq):
  x = symbols('x')
  solution = solve(eq, x)
  for s in solution:
    print("x = ", s)

  # Write your code here
def meniu():

    print("------ Commands -----")
    print("|     a = add       |")
    print("|   s = subtract    |")
    print("|   m = multiply    |")
    print("|   d = divide      |")
    print("| pm = prime nubmers|")
    print("| pf = prime factors|")
    print("|   sr = squareroot |")
    print("| x = solve equation|")
    print("|    q = quit       |")
    print("---------A.C--------")


while True:
  os.system('clear')
  meniu()
  choice = input("What do you want to do: ")
  if choice == "q":
       sys.exit()

  elif choice == "a":
    num = input("Enter the sum you want to do:  ")
    sp = num.split("+")
    a = float(sp[0])
    b = float(sp[1])
    add(a, b)

  elif choice == "s":
    num = input("Enter the subtraction you want to do:  ")
    sp = num.split("-")
    a = float(sp[0])
    b = float(sp[1])
    subtract(a ,b)

  elif choice == "m":
    num = input("Enter the multiplication you want to do using * :  ")
    sp = num.split("*")
    a = float(sp[0])
    b = float(sp[1])
    multyply(a ,b)

  elif choice == "d":
    num = input("Enter the devide you want to do using / :  ")
    sp = num.split("/")
    a = float(sp[0])
    b = float(sp[1])
    devide(a ,b)

  elif choice =="pm":
    num = input("Enter a number to test if its a prime number: ")
    a = int(num)
    prime_number(a)

  elif choice == "pf":
    num = input("Enter a number to find the prime factors: ")
    a = int(num)
    generate_prime_factors(a)

  elif choice == "sr":
    num = input("Enter a number to find the square root of it: ")
    a = float(num)
    square_root(a)


  elif choice == "x":
    eq = input("Enter equation: 0 = ")
    solve_for_x(eq)
