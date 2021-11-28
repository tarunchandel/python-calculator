import art

#Calculator

def add(num1, num2):
  """Takes two mumbers and returns the addition of both."""
  return num1 + num2

def subtract(num1, num2):
  """Takes two mumbers and returns the difference of both."""
  return num1 - num2

def multiply(num1, num2):
  """Takes two mumbers and returns the product of both."""
  return num1 * num2

def divide(num1, num2):
  """Takes two mumbers and returns the divison of both."""
  return num1 / num2



def calculate(num1, num2, operation):
  function = operators[operation]
  return(function(num1, num2))

operators = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}


def calculator():
  continue_flag = True
  num1 = float(input("Enter the first number: "))
  art.print_calc(num1)
  while continue_flag:
    for symbol in operators:
      print(symbol)
    operation = input("Select an operation you want to conduct: ")
    num2 = float(input("Enter the next number: "))
    #art.print_calc(num2)
    result = calculate(num1, num2, operation)
    art.print_calc(result)
    print(result)
    flag_decision = input(f"Want to continue with {result}? Enter:\n'y' for yes\n'c' for starting fresh\nany other key to exit.\n")
    if flag_decision == 'y':
      num1 = result
    elif flag_decision =='c':
      calculator()
    else:
      continue_flag = False

print(art.logo)
art.print_calc()
calculator()